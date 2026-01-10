import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# 1. Loading settings
load_dotenv()

# Streamlit Page Configuration
st.set_page_config(page_title="AI Knowledge Assistant", page_icon="🧠")
st.title("🧠 Enterprise RAG Explorer")
st.markdown("Interactive Q&A system powered by LangChain and Vector Search.")

# 2. Initializing RAG engine (Runs only once!)
@st.cache_resource
def setup_qa_chain():
    loader = TextLoader("data.txt", encoding="utf-8")
    documents = loader.load()
    vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    # Define the prompt
    prompt = ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context:
    <context>
    {context}
    </context>
    Question: {input}
    """)

    # Create the chains
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(vectorstore.as_retriever(), combine_docs_chain)

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
            response = qa_chain.invoke({"input": prompt})
            answer = response["answer"]
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})