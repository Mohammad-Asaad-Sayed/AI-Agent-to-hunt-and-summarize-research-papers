import streamlit as st
import asyncio
from agents import teamConfig, orchestrate
from autogen_agentchat.messages import TextMessage

st.title("Literature Review Agent")

desc = st.text_input("Describe your research topic:")

clicked = st.button("Find Papers", type="primary")

chat_container = st.container()

if clicked:
    async def main(desc):
        team = teamConfig()
        async for message in orchestrate(team, desc):  # <-- async for
            with chat_container:
                if isinstance(message, TextMessage):
                    if message.source.lower() == "arxivagent":
                        with st.chat_message("human"):
                            st.markdown(message.content)
                    elif message.source.lower() == "researcher":
                        with st.chat_message("assistant"):
                            st.markdown(message.content)
                    else:
                        st.markdown(message.content)
                else:
                    # For ToolCallRequestEvent or ToolCallExecutionEvent
                    with st.expander("Tool Call"):
                        st.markdown(str(message))

    asyncio.run(main(desc))
