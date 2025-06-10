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
        This Function takes folder path of multiple csv's and gives combined csv at out_path

        ARGS : Folder_path:str where all csv's contain

        Returns : combined csv,path of combined csv
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

        logging.info("Reading pdf file ")

        try:
            docs = PyPDFLoader(file_path=pdf_path).load()
            logging.info("pdf file read Successfully")
            logging.info("Data Ingestion Completed")
            return docs
        except Exception as e:
            raise CustomException(e,sys)
        


if __name__=='__main__':
    data_ingestion = DataIngestion()
    
    folder_path = 'Data/section1_chapters'
    df,csv_path = data_ingestion.get_csv_data(folder_path=folder_path)

    pdf_path  = Path("Data\General Notes.pdf")

    docs = data_ingestion.read_pdf(pdf_path=pdf_path)

    print(len(docs))
    print(type(docs))

    docs = DataTransformation().get_chunks(chunk_size=1000,chunk_overlap=100,docs=docs)

    print(len(docs))
    persist_path = "artifacts/vectorstore"
    vs = vectordb(persist_path=persist_path,docs=docs)
    