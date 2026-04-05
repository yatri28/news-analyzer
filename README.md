# News Analyzer Agent 🤖

An AI-powered news analysis agent built with Google ADK and Gemini, deployed on Google Cloud Run.

## What it does
Send any news text and get back:
- **Summary** — One sentence summary of the news
- **Sentiment** — Positive, Negative, or Neutral
- **Takeaway** — One line actionable insight

## Tech Stack
- Google ADK (Agent Development Kit)
- Gemini 2.0 Flash (via Vertex AI)
- Google Cloud Run
- Flask + Gunicorn
- Python 3.11
- Docker

## Live Demo
🌐 **Cloud Run URL:** https://news-analyzer-agent-606772292791.us-central1.run.app

## API Usage

### Health Check
GET https://news-analyzer-agent-606772292791.us-central1.run.app/

### Analyze News
POST https://news-analyzer-agent-606772292791.us-central1.run.app/analyze
Content-Type: application/json
{
"text": "Google Cloud launched new AI tools for developers at Google Next 2025"
}

### Sample Response
```json
{
  "summary": "Google Cloud unveiled new AI developer tools at Google Next 2025",
  "sentiment": "Positive",
  "takeaway": "Great opportunity for developers building on Google Cloud"
}
```

## Project Structure
news-analyzer/
├── agent.py          # ADK Agent definition
├── main.py           # Flask HTTP server
├── requirements.txt  # Python dependencies
├── Dockerfile        # Container configuration
└── .env              # Environment variables

## Deployment
Built and deployed using ADK CLI:
```bash
uvx --from google-adk==1.14.0 \
adk deploy cloud_run \
  --project=$PROJECT_ID \
  --region=us-central1 \
  --service_name=news-analyzer-agent \
  --with_ui \
  .
```

## Built For
Google Cloud Gen AI Academy APAC Edition - Cohort 1 - Track 1
