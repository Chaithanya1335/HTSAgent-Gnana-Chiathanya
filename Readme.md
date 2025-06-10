It's currently June 10, 2025. I cannot access external websites or local files, including GitHub repositories. Therefore, I cannot directly fetch the `README.md` content from the provided link or execute any Python files.

However, I can provide you with a **template for your `README.md` file**, following the format you requested, and assuming typical content for such a project. You will need to fill in the specific details where indicated.

---

# HTSAgent-Gnana-Chiathanya

A smart agent designed to assist with Harmonized Tariff Schedule (HTS) related queries and calculations.

## 1) About Project and Data

This project aims to develop an intelligent agent that leverages a combination of RAG (Retrieval-Augmented Generation) and specialized tools to answer questions related to the Harmonized Tariff Schedule (HTS) and calculate tariff duties. It's built to simplify the process of navigating complex HTS codes and understanding associated regulations and costs.

The data used in this project primarily consists of:
* **HTS Tariff Data (CSV/Excel):** This includes HTS codes, descriptions, various duty rates (General, Special, Column 2), units of quantity, and other relevant tariff information. This data is crucial for the `DutyCalculator` tool.
* **HTS General Notes (PDF):** These are official documents or sections that provide comprehensive guidelines and rules for interpreting and applying the HTS. This data is used as the knowledge base for the RAG system to answer interpretive questions.

## 2) Tech Stack

The project is built using the following key technologies and libraries:

* **Python:** The core programming language.
* **LangChain:** Framework for developing applications powered by language models, facilitating agent creation, tool integration, and RAG pipelines.
* **Streamlit:** For building the interactive web application user interface.
* **FAISS:** (Facebook AI Similarity Search) For efficient similarity search and retrieval within the RAG pipeline.
* **ChromaDB:** (Potentially, if used for vector storage instead of or in addition to FAISS)
* **Pandas:** For data manipulation and preprocessing of structured HTS tariff data.
* **PyPDFLoader:** For loading and parsing PDF documents (e.g., HTS General Notes).
* **Other relevant libraries:** `re` (for regex), `logging`, `sys`, etc.
* **Large Language Models (LLMs):** Utilizes powerful LLMs for understanding queries and generating responses (e.g., OpenAI models, Google Gemini, Hugging Face models, etc., depending on configuration).
* **Embedding Models:** For converting text into numerical vector representations (e.g., OpenAI Embeddings, Hugging Face embeddings).

## 3) Clone Repository

To get a copy of this project up and running on your local machine, follow these steps:

```bash
git clone https://github.com/Chaithanya1335/HTSAgent-Gnana-Chiathanya.git
cd HTSAgent-Gnana-Chiathanya
```

## 4) Get Data Ready

Before running the application, you need to prepare the HTS data. This involves preprocessing the raw HTS tariff data and likely creating a vector store from the HTS General Notes PDF.

Execute the following Python script to perform the necessary data preparation steps:

```bash
python src/Pipeline/Get_Data_Ready.py
```

This script will handle tasks such as:
* Reading raw HTS data.
* Cleaning and transforming the data.
* (Potentially) Reading PDF documents like HTS General Notes.
* (Potentially) Chunking documents and creating/persisting vector stores (e.g., FAISS index) in the `artifacts` directory.

Ensure you have the necessary raw data files in their expected locations (e.g., `data/raw/` or specified paths within `Get_Data_Ready.py`) before running this step.

## 5) Install Requirements

Install all the necessary Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 6) Run the Streamlit Application

Once the data is ready and all dependencies are installed, you can launch the Streamlit web application:

```bash
streamlit run app.py
```

This command will open the application in your default web browser, allowing you to interact with the HTS Agent.

---