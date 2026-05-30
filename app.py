import streamlit as st

from agents.travel_agent import run_travel_agent

st.set_page_config(
    page_title="AI Travel Planner"
)

st.title("AI Travel Planner Chatbot")

st.write(
    "Ask me to plan your travel."
)

# Chat history

if "messages" not in st.session_state:

    st.session_state.messages = []

# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# User input

prompt = st.chat_input(
    "Enter your travel request..."
)

if prompt:

    # Store user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show user message

    with st.chat_message("user"):

        st.markdown(prompt)

    # AI response

    with st.chat_message("assistant"):

        response = run_travel_agent(prompt)

        st.markdown(response)

    # Store AI response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )