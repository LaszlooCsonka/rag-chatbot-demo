<<<<<<< HEAD
**Minimal RAG Chatbot (LangChain + OpenAI)
A lightweight Retrieval-Augmented Generation (RAG) application designed to demonstrate document-based AI interaction. This project extracts information from a custom knowledge base (data.txt) and generates precise answers using OpenAI's GPT models.**

🏗️ **Project Management & Methodology**
      This project was developed using professional software engineering standards, focusing on transparency and process modeling.

📋 **Agile Development (Scrum)**
      The development followed the Scrum methodology, managed in Jira.

      - Planning: 1-week sprint with a defined Backlog and Story Point estimation.
      
      - Tracking: Tasks were organized into Epics and User Stories to ensure clear feature delivery.
      
      - Result: Successfully closed the sprint with all core RAG functionalities and documentation.
      
      Note: Check the assets/ folder for the Jira Board screenshot.

⚙️ **Business Process Modeling (BPMN 2.0)**
      The system's internal logic was modeled in Camunda to visualize the interaction between the user and the AI Engine.
      
      Figure 1: RAG Workflow - Separating User Interaction and System Logic.

🚀 **Features**
      - Document Loading: Processing of local plain text files.
      
      - Vector Search: Powered by FAISS (Facebook AI Similarity Search) for fast retrieval of relevant context.
      
      - Embeddings: Uses OpenAI models to convert text into mathematical vector representations.
      
      - RAG Chain: Seamless integration of retrieval and generation using LangChain.

🛠️ **Tech Stack**
      - Language: Python 3.12+
      
      - Orchestration: LangChain
      
      - LLM: OpenAI GPT-4o-mini
      
      - Vector Store: FAISS
      
      - Configuration: Python-dotenv
      
      - Process Modeling: Camunda (BPMN 2.0)
      
      - Task Management: Jira (Scrum)

📋 **Installation and Setup**
**1. Clone the Repository**

      Bash
      
      git clone <your-repository-link>
      cd rag-demo

**2. Configure Virtual Environment**
      Create the virtual environment:
      
      Bash
      
      py -m venv venv
      
      Activation on Windows (CMD or PowerShell):
      
      .\venv\Scripts\activate

**[!TIP]** Visual Studio Code Setup If the (venv) prefix does not appear in your terminal:

      - Select Interpreter: Press Ctrl + Shift + P, type Python: Select Interpreter, and select the one labeled ('venv': venv).

      - Open a New Terminal: Click the + (New Terminal) icon. VS Code will now automatically run the activation script.

      - Troubleshooting (PowerShell): If you receive a script execution error, run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

**3. Install Dependencies**
      Ensure your virtual environment is active, then run:
      
      Bash
      
      pip install -r requirements.txt

**4. API Key Configuration**
      Create a .env file in the root directory and add your OpenAI API key:
      
      Plaintext: 
      
      OPENAI_API_KEY=your_api_key_here

**5. 📖 Data Preparation (adat.txt)**
      To get the best results, structure your adat.txt file as follows:
      
      - Be Explicit: Use clear headings or bullet points.
      
      - Context Density: Keep related information close together.
      
      - Separation: Use double newlines between different topics.

**6. ⚡ Running the Application**

      The application can be run in two modes:

      - **Web Interface (Recommended):**
         ```bash
         streamlit run app.py

      This launches a modern, browser-based chat interface.

      - **Terminal Mode (Legacy): If you wish to run the original script:**

        ```bash      
        python app.py
=======
# Enterprise RAG Knowledge System (LangChain + OpenAI)

A professional-grade Retrieval-Augmented Generation (RAG) application that demonstrates how to transform static documents into interactive knowledge bases. This project features both a **User Interface (Streamlit)** and a **REST API (FastAPI)**, mimicking real-world AI deployments.

---

## 🏗️ Project Management & Methodology
This project was developed using professional software engineering standards, focusing on transparency and process modeling.

### 📋 Agile Development (Scrum)
The development followed the **Scrum methodology**, managed in **Jira**.
* **Planning:** 1-week sprint with a defined Backlog and Story Point estimation.
* **Tracking:** Tasks were organized into Epics and User Stories to ensure clear feature delivery.
* **Result:** Successfully delivered the RAG engine, Web UI, and API endpoints.
> *Note: Check the `assets/` folder for the Jira Board screenshots.*

### ⚙️ Business Process Modeling (BPMN 2.0)
The system's internal logic was modeled in **Camunda** to visualize the interaction between the user, the vector store, and the LLM.
* **Figure 1:** RAG Workflow - Clear separation between User Interaction and Backend Retrieval Logic.

---

## 🚀 Key Features
* **Dual-Interface Access:** User-friendly Web UI and developer-ready REST API.
* **Intelligent Retrieval:** Powered by **FAISS** (Facebook AI Similarity Search) for high-performance context fetching.
* **Advanced RAG Chain:** Seamless integration using **LangChain** for context-aware answering.
* **Optimized LLM:** Uses **GPT-4o-mini** for an ideal balance of speed, cost, and intelligence.

---

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **AI Orchestration:** LangChain
* **Web UI:** Streamlit (Rapid Prototyping)
* **API Framework:** FastAPI (Production-ready endpoints)
* **Vector Store:** FAISS
* **LLM:** OpenAI GPT-4o-mini
* **Task & Process:** Jira (Scrum), Camunda (BPMN 2.0)

---

## 📋 Installation and Setup

### 1. Clone & Environment
Bash

git clone <your-repository-link>
cd rag-demo
py -m venv venv
.\venv\Scripts\activate

#### 2. Install Dependencies

Bash

pip install -r requirements.txt

### 3. API Key Configuration

Create a .env file in the root directory:

Plaintext

OPENAI_API_KEY=your_actual_key_here

⚡ Running the Application
This project provides two primary ways to interact with the AI:

A. Web Interface (Streamlit)
Ideal for end-users to chat with the document.

Bash

streamlit run app.py

B. REST API (FastAPI)
Ideal for integrating the chatbot into other systems or mobile apps.

Bash

uvicorn api:app --reload

- Once running, access the interactive API documentation at: http://127.0.0.1:8000/docs

📖 Data Preparation (data.txt)
The system reads from data.txt. For best results:

Use clear headings and bullet points.

Keep related information in the same paragraph.

Use double newlines to separate distinct topics.
>>>>>>> 6cd78ef (Final project: Streamlit UI and FastAPI endpoints added)
