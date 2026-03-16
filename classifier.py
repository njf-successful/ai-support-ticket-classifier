import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_ticket(ticket_text):

    prompt = f"""
You are a support ticket classifier.

Analyze the following ticket and return:

Category
Priority (Low, Medium, High)
Sentiment
Recommended Team
Suggested Response

Ticket:
{ticket_text}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception:
        return """
Category: Billing
Priority: High
Sentiment: Frustrated
Recommended Team: Billing Support
Suggested Response: Thank you for reaching out. I'm sorry for the inconvenience regarding the duplicate charge. Our billing team will review your account and follow up shortly.

Note: Demo response shown because API credits are not currently enabled.
"""
