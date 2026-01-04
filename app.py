import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.chains import RetrievalQA

# Load the API key from the .env file
load_dotenv()

# Load the text content from data.txt
loader = TextLoader("data.txt", encoding="utf-8")
documents = loader.load()

# 3. Split the text into smaller chunks and save them to a FAISS vector store 
# # Use OpenAIEmbeddings to transform text into vector representations
vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())

# 4. Assemble the RAG chain 
# # Using gpt-4o-mini for cost-efficiency (your $10 credit will go a long way)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=vectorstore.as_retriever()
)

# 5. Query the bot about information contained in data.txt
query = "Which technologies does László Kovács prefer?"
response = qa_chain.invoke(query)

print("\n--- Artificial Intelligence Response: ---")
print(response["result"])