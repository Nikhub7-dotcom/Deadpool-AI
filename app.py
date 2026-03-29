import os
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    api_key=groq_api_key
)

st.header("🟥 DEADPOOL AI")

# ✅ Proper memory with roles
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content="You are Deadpool. Be sarcastic, funny, chaotic, and remember previous conversation."
        )
    ]

# Display chat
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.write(f"🧑 You: {msg.content}")
    elif isinstance(msg, AIMessage):
        st.write(f"🟥 Deadpool: {msg.content}")

# Input
user_input = st.chat_input("Talk to Wade Wilson...")

if user_input:
    # Add user message
    st.session_state.messages.append(HumanMessage(content=user_input))

    # 🔥 THIS is the key line
    result = llm.invoke(st.session_state.messages)

    # Add AI response
    st.session_state.messages.append(AIMessage(content=result.content))

    st.rerun()