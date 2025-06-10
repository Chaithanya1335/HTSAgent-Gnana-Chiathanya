from src.exception import CustomException
from src.logger import logging
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI

import pandas as pd
import os
import sys


def combine_all_csv(folder_path: str, out_path: str) -> pd.DataFrame:
    try:
        # List all CSV files in the folder
        chapter_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".csv")])

        if not chapter_files:
            logging.warning(f"No CSV files found in folder: {folder_path}")
            return pd.DataFrame()

        logging.info(f"Found {len(chapter_files)} CSV files to combine.")

        df_list = []
        for file in chapter_files:
            path = os.path.join(folder_path, file)
            logging.info(f"Reading file: {file}")
            df = pd.read_csv(path)
            df_list.append(df)

        # Combine all CSVs
        combined_df = pd.concat(df_list, ignore_index=True)

        # Save to output path
        combined_df.to_csv(out_path, index=False, header=True)
        logging.info(f"Successfully combined and saved to {out_path}")

        return combined_df

    except Exception as e:
        raise CustomException(e, sys)
    


def get_embedding_model(model_name:str,api_key:str):

        """
        Initializes and returns a Google Generative AI embedding model.

        Args:
            model_name (str): The name or path of the embedding model to load (e.g., 'models/embedding-001').
            api_key (str): The API key required to authenticate with Google's Generative AI service.

        Returns:
            GoogleGenerativeAIEmbeddings: An instance of the embedding model.

        Raises:
            CustomException: If there is an error during model initialization.
        """
        try:
            logging.info(f"Initializing embedding model: {model_name}")
            embedding_model = GoogleGenerativeAIEmbeddings(model= model_name,google_api_key=api_key)
            logging.info("Embedding model initialized successfully.")
            return embedding_model
        except Exception as e:
            raise CustomException(e, sys)

def get_llm(model_name,api_key):
     try:
        llm = ChatGoogleGenerativeAI(model = model_name,api_key=api_key)
        return llm
     except Exception as e:
         raise CustomException(e,sys)


