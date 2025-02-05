import streamlit as st 
# from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os 
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPEN_API_KEY")

# # if you use LangSmith tracking, so apply this
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACKING_V2"] = "true"
# os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

arxiv_wrapper = ArxivAPIWrapper(
    top_k_results = 1,
    doc_content_chars_max = 400
)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=300
)
wikipedia = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun(name="Search")

# search engine title 
st.title("🔎 Xarvis - AI Search Engine")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain & Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

# sidebar settings 
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your api key:",type="password")

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant", "content":"Hi, i am a chatbot who can search the web. how can i assist you today?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt:=st.chat_input(placeholder="what is machien learning?"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)

    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key, streaming=True)
    tools = [search, arxiv, wikipedia]

    search_agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_passing_error=True)

    with st.chat_message("assistant"):
        st_call = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_call])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)
