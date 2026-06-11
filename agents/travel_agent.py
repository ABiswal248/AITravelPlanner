from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def run_travel_agent(user_prompt, chat_history):

    try:

        system_prompt = """
You are AI Travel Planner.

Your ONLY purpose is helping users with travel planning.

You can assist with:

- Flights
- Hotels
- Tourist Attractions
- Travel Itineraries
- Travel Budgets
- Travel Recommendations
- Transportation
- Travel Safety
- Travel Documentation

IMPORTANT RULES:

1. Never act as a general-purpose chatbot.

2. If a user asks about politics, history, current affairs,
sports, programming, funny facts, science, education,
health, finance, or entertainment topics,
politely redirect them back to travel planning.

3. Do not become a general chatbot.

4. If the user mentions a destination,
collect:

- Source City
- Destination City
- Travel Date
- Number of Travelers
- Budget
- Hotel Preference
- Transportation Preference

5. Do not generate an itinerary until sufficient information is collected.

6. Stay focused on travel planning.

7. Do not use emojis.

8. Maintain a professional tone.
"""

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        for message in chat_history:

            if message["role"] in ["user", "assistant"]:

                messages.append(
                    {
                        "role": message["role"],
                        "content": message["content"]
                    }
                )

        response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"