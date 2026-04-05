import os
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
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
