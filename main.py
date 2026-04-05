import os
import json
import asyncio
from flask import Flask, request, jsonify
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from google.adk.agents.llm_agent import Agent

app = Flask(__name__)
session_service = InMemorySessionService()

root_agent = Agent(
    model='gemini-2.0-flash',
    name='news_analyzer',
    description='Analyzes news text and returns summary, sentiment and takeaway.',
    instruction="""You are a news analysis agent. When given any text or news:
1. Write a one-sentence SUMMARY
2. Classify SENTIMENT as exactly one of: Positive, Negative, or Neutral
3. Write a one-sentence TAKEAWAY

Always respond in this exact JSON format:
{
  "summary": "...",
  "sentiment": "Positive/Negative/Neutral",
  "takeaway": "..."
}
Respond with JSON only, no extra text."""
)

async def run_agent(user_text):
    runner = Runner(
        agent=root_agent,
        app_name="news_analyzer",
        session_service=session_service
    )
    session = await session_service.create_session(
        app_name="news_analyzer",
        user_id="user_1"
    )
    message = Content(parts=[Part(text=user_text)])
    response_text = ""
    async for event in runner.run_async(
        user_id="user_1",
        session_id=session.id,
        new_message=message
    ):
        if event.is_final_response() and event.content:
            for part in event.content.parts:
                if part.text:
                    response_text += part.text
    return response_text

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "News Analyzer Agent is running! Send POST to /analyze"})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Please provide 'text' field"}), 400
    user_text = data["text"]
    try:
        response_text = asyncio.run(run_agent(user_text))
        try:
            result = json.loads(response_text)
        except:
            result = {"raw_response": response_text}
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
