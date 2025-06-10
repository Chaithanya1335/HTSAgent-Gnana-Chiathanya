from langchain_community.vectorstores import FAISS
from src.exception import CustomException
from src.logger import logging
from src.utils import get_embedding_model
from dotenv import load_dotenv
import os,sys


load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')



def vectordb(persist_path,docs):
        """
        Creates and saves a Chroma vector store locally from the given list of documents.

        Args:
            persist_path (str): Directory path where the vector store should be saved.
            docs (List[Document]): A list of LangChain Document objects to be embedded and stored.

        Returns:
            Chroma: The Chroma vector store object created from the input documents.

        Raises:
            CustomException: If any error occurs during embedding or vector store creation.
        """
        try:
            logging.info("Initializing embedding model for vector DB.")
            embedding_model = get_embedding_model(
                model_name='models/embedding-001',
                api_key=GEMINI_API_KEY
            )

            logging.info("Creating Chroma vector store from documents.")
            vector_store = FAISS.from_documents(
                documents=docs,
                embedding=embedding_model,
            )

            vector_store.save_local(persist_path)
            logging.info(f"Vector store successfully saved at: {persist_path}")

            return vector_store

        except Exception as e:
            
            raise CustomException(e, sys)