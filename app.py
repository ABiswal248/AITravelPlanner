import streamlit as st
from agents.travel_agent import run_travel_agent

st.set_page_config(
    page_title="AI Travel Planner",
    layout="centered"
)

st.title("AI Travel Planner")

st.markdown(
    "Helping travelers plan smarter trips with AI"
)

with st.expander("Suggested Prompts", expanded=True):
    st.markdown("""
- Plan a trip from Hyderabad to Goa
- Weekend trip under ₹10,000
- Best places to visit in Goa
- Family vacation itinerary
- Honeymoon trip planner
- Budget trip to Manali
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input(
    "Enter your travel request..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Planning your trip..."):

            response = run_travel_agent(
                prompt,
                st.session_state.messages
            )

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )