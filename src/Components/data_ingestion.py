from src.utils import combine_all_csv
from src.logger import logging
from src.exception import CustomException
from src.Components.Data_transformation import DataTransformation
from src.Components.vector_db import vectordb

from dataclasses import dataclass
from langchain_community.document_loaders import PyPDFLoader
from langchain.docstore.document import Document
from typing import Tuple,List
from pathlib import Path
import os
import pandas as pd
import sys
@dataclass
class DataIngestionConfig:
    save_data_path =  Path(os.path.join("artifacts",'final.csv'))


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def get_csv_data(self,folder_path)->Tuple[pd.DataFrame,str]:
        """
        Reads a PDF file from the given path and returns a list of LangChain Document objects.

        This method utilizes `PyPDFLoader` to parse the content of a PDF file,
        converting each page or section into a LangChain Document. It's an
        essential step for ingesting unstructured PDF data into a format
        suitable for downstream NLP tasks, such as RAG (Retrieval-Augmented Generation).

        Args:
            pdf_path (str): The absolute or relative path to the PDF file
                            that needs to be read.

        Returns:
            List[Document]: A list of parsed LangChain Document objects, where
                            each document typically represents a page or a
                            logical section of the PDF content.

        Raises:
            CustomException: If an error occurs during the PDF reading or parsing
                             process (e.g., file not found, corrupted PDF,
                             or issues with the `PyPDFLoader`). The original
                             exception details are captured and re-raised.
        """
        logging.info("Data Ingestion Started")

        try:
            os.makedirs(os.path.dirname(self.config.save_data_path),exist_ok=True)
            df = combine_all_csv(folder_path=folder_path,out_path=self.config.save_data_path)
            logging.info("all csv's Combined")
            return (df,self.config.save_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)

        
    
    def read_pdf(self,pdf_path:str)->list[Document]:
        """
        Reads a PDF file from the given path and returns a list of LangChain Document objects.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            list[Document]: A list of parsed documents from the PDF.

        Raises:
            CustomException: If reading or parsing the PDF fails.
        """

        logging.info("Reading pdf file ")

        try:
            docs = PyPDFLoader(file_path=pdf_path).load()
            logging.info("pdf file read Successfully")
            logging.info("Data Ingestion Completed")
            return docs
        except Exception as e:
            raise CustomException(e,sys)
        



    