

# **HTSAgent-Gnana-Chiathanya**

A smart agent designed to assist with Harmonized Tariff Schedule (HTS) related queries and calculations.

## 1\) About Project and Data

This project aims to develop an intelligent agent that leverages a combination of RAG (Retrieval-Augmented Generation) and specialized tools to answer questions related to the Harmonized Tariff Schedule (HTS) and calculate tariff duties. It's built to simplify the process of navigating complex HTS codes and understanding associated regulations and costs.

The data used in this project primarily consists of:

  * **HTS Tariff Data (CSV/Excel):** This includes HTS codes, descriptions, various duty rates (General, Special, Column 2), units of quantity, and other relevant tariff information. This data is crucial for the `DutyCalculator` tool.
  * **HTS General Notes (PDF):** These are official documents or sections that provide comprehensive guidelines and rules for interpreting and applying the HTS. This data is used as the knowledge base for the RAG system to answer interpretive questions.

## 2\) Tech Stack

The project is built using the following key technologies and libraries:

  * **Python:** The core programming language.
  * **LangChain:** Framework for developing applications powered by language models, facilitating agent creation, tool integration, and RAG pipelines.
  * **Streamlit:** For building the interactive web application user interface.
  * **FAISS:** (Facebook AI Similarity Search) For efficient similarity search and retrieval within the RAG pipeline.
  * **Pandas:** For data manipulation and preprocessing of structured HTS tariff data.
  * **PyPDFLoader:** For loading and parsing PDF documents (e.g., HTS General Notes).
  * **Google Gemini Models:**
      * **GoogleGenerativeAI (LLM):** Used for understanding complex queries, generating conversational responses, and driving the agent's reasoning.
      * **GoogleGenerativeAIEmbeddings (Embedding Model):** Utilized for converting text into numerical vector representations, which is essential for semantic search in the RAG system.
  * **External Tools:**
      * **Wikipedia Search Tool:** Integrated to fetch general knowledge and factual information from Wikipedia, broadening the agent's ability to answer diverse questions not directly covered by HTS data.
      * **DuckDuckGo Search Tool:** Provides real-time web search capabilities, enabling the agent to access up-to-the-minute information from the internet.
  * **Other relevant libraries:** `re` (for regex), `logging`, `sys`, etc.

## 3\) Clone Repository

To get a copy of this project up and running on your local machine, follow these steps:

```bash
git clone https://github.com/Chaithanya1335/HTSAgent-Gnana-Chiathanya.git
cd HTSAgent-Gnana-Chiathanya
```

## 4\) Obtain Google Gemini API Key

To use the Google Gemini models for both the LLM and embeddings, you need a Google API Key.

**Steps to get your API Key:**

1.  Go to the [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Log in with your Google account.
3.  Click on "Get API key in a new project" or "Create API key" if you have an existing project.
4.  Copy the generated API key.

**Set the API Key as an Environment Variable:**
It's recommended to set your API key as an environment variable named `GOOGLE_API_KEY` to keep it secure and avoid hardcoding it in your code.

  * **For Linux/macOS:**

    ```bash
    export GOOGLE_API_KEY="your_api_key_here"
    ```

    (You might want to add this to your `~/.bashrc`, `~/.zshrc`, or equivalent file for permanent access.)

  * **For Windows (Command Prompt):**

    ```bash
    set GOOGLE_API_KEY="your_api_key_here"
    ```

  * **For Windows (PowerShell):**

    ```powershell
    $env:GOOGLE_API_KEY="your_api_key_here"
    ```

## 5\) Get Data Ready

Before running the application, you need to prepare the HTS data. This involves preprocessing the raw HTS tariff data and creating a vector store from the HTS General Notes PDF using Gemini Embeddings.

Execute the following Python script to perform the necessary data preparation steps:

```bash
python src/Pipeline/Get_Data_Ready.py
```

This script will handle tasks such as:

  * Reading raw HTS data.
  * Cleaning and transforming the data.
  * Reading PDF documents like HTS General Notes.
  * Chunking documents and creating/persisting vector stores (e.g., FAISS index) in the `artifacts` directory, *using GoogleGenerativeAIEmbeddings*.

Ensure you have the necessary raw data files in their expected locations (e.g., `data/raw/` or specified paths within `Get_Data_Ready.py`) before running this step.

## 6\) Install Requirements

Install all the necessary Python packages, including the LangChain integration for Google Generative AI models and other tools:

```bash
pip install -r requirements.txt
```

**Note:** Your `requirements.txt` should include `langchain-google-genai`, `langchain-community`, `wikipedia`, `duckduckgo_search`, `pandas`, `pypdf`, `faiss-cpu` (or `faiss-gpu`), `streamlit`, etc.

## 7\) Run the Streamlit Application

Ensure your `GOOGLE_API_KEY` environment variable is set (as shown in Step 4). Then, launch the Streamlit web application:

```bash
streamlit run app.py
```

This command will open the application in your default web browser, allowing you to interact with the HTS Agent powered by Gemini models and its integrated tools.

-----