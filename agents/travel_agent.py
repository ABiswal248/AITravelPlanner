from dotenv import load_dotenv
import os
from groq import Groq

from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotels
from tools.places_tool import discover_places

# Load environment variables
load_dotenv()

# Get API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(
    api_key=GROQ_API_KEY
)

# Main AI Travel Planner Function
def run_travel_agent(user_prompt):

    try:
        # Get travel data
        flights = search_flights("Hyderabad", "Goa")

        hotels = recommend_hotels("Goa")

        places = discover_places("Goa")

        # Create prompt
        final_prompt = f"""
        You are an intelligent AI Travel Planner.

        User Request:
        {user_prompt}

        Available Flights:
        {flights}

        Recommended Hotels:
        {hotels}

        Tourist Places:
        {places}

        Create a detailed travel itinerary.
        """

        # Generate AI response
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": final_prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"