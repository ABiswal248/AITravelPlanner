# AI Travel Planner Chatbot

An AI-powered travel planning assistant built using Python, Streamlit, and Groq AI.

This project helps users generate personalized travel itineraries, hotel recommendations, tourist place suggestions, and travel guidance through an interactive chatbot interface.

---

# Features

* AI-based travel planning
* Smart travel itinerary generation
* Hotel recommendations
* Tourist place suggestions
* Flight information
* Interactive chatbot interface
* Streamlit web application
* Groq AI integration
* Beginner-friendly project structure

---

# Technologies Used

* Python
* Streamlit
* Groq AI
* dotenv
* JSON
* Git & GitHub

---

# Project Structure

```text
AITravelPlanner/
│
├── agents/
│   └── travel_agent.py
│
├── tools/
│   ├── flight_tool.py
│   ├── hotel_tool.py
│   └── places_tool.py
│
├── data/
│   ├── flights.json
│   ├── hotels.json
│   └── places.json
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/ABiswal248/AITravelPlanner.git
```

---

## Step 2: Open Project Folder

```bash
cd AITravelPlanner
```

---

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
.\venv\Scripts\Activate.ps1
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root folder.

Add:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Run The Project

```bash
streamlit run app.py
```

---

# Sample User Prompts

* Plan a Goa trip for 3 days
* Suggest hotels in Goa
* Create a family vacation itinerary
* Recommend tourist places in Hyderabad

---

# Future Improvements

* Real flight APIs
* Google Maps integration
* User login system
* Database integration
* AI memory
* Travel budget calculator
* Voice assistant support
* Deployment on cloud

---

# Author

Arjya Biswal

---

# License

This project is developed for learning and educational purposes.
