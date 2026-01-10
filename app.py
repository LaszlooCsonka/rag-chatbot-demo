import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
#from langchain.chains import RetrievalQA
from langchain_community.chains import RetrievalQA

# 1. Loading settings
load_dotenv()

# Streamlit Page Configuration
st.set_page_config(page_title="AI Knowledge Assistant", page_icon="🧠")
st.title("🧠 Enterprise RAG Explorer")
st.markdown("Interactive Q&A system powered by LangChain and Vector Search.")

# 2. Initializing RAG engine (Runs only once!)
@st.cache_resource
def setup_qa_chain():
    # Your code's logic:
    loader = TextLoader("data.txt", encoding="utf-8")
    documents = loader.load()
    
    # Creating vector store
    vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())
    
    # Assembling the chain
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=vectorstore.as_retriever()
    )

qa_chain = setup_qa_chain()

# 3. Managing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Displaying previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Handling user input
if prompt := st.chat_input("Ask something about data.txt..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            response = qa_chain.invoke(prompt)
            answer = response["result"]
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})