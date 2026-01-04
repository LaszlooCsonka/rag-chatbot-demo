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
