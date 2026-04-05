import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent

load_dotenv()
model_name = os.getenv("MODEL", "gemini-2.5-flash")

root_agent = Agent(
    model=model_name,
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
