# AI Support Ticket Classifier

A simple AI-powered tool that analyzes support tickets and classifies them by category, priority, and sentiment. It also suggests the appropriate support team and drafts a response.

## Why I Built This

I built this project as a portfolio example to demonstrate how AI can be used to automate repetitive support and operations workflows. This tool shows my ability to combine Python, API integration, error handling, and a user-facing interface into a practical business solution.

## Features

- Support ticket classification
- Priority detection
- Sentiment analysis
- Recommended support team
- Suggested response generation
- Demo fallback response when API credits are unavailable

## Tech Stack

- Python
- Streamlit
- OpenAI API
- python-dotenv

## Project Structure

- `app.py` — Streamlit user interface
- `classifier.py` — AI classification logic
- `requirements.txt` — project dependencies
- `.gitignore` — prevents sensitive files from being uploaded

## How to Run

```bash
pip3 install -r requirements.txt
python3 -m streamlit run app.py
