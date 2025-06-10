from src.logger import logging
from src.exception import CustomException
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from typing import List
import sys,os


class DataTransformation:
    def __init__(self):
        pass

    def get_chunks(self,chunk_size,chunk_overlap,docs)->List[Document]:

        """
            Splits a list of LangChain Document objects into smaller chunks using recursive character splitting.

            Args:
                chunk_size (int): Maximum size of each chunk in characters.
                chunk_overlap (int): Number of overlapping characters between consecutive chunks.
                docs (List[Document]): List of LangChain Document objects to be chunked.

            Returns:
                List[Document]: A list of chunked Document objects.

            
            """
       
        logging.info("Data Transformation Started")

        try:
            splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)

            chunks = splitter.split_documents(docs)

            logging.info(f"Chunking of data completed and no of chunks created is {len(chunks)}")

            return chunks
        
    
        except Exception as e:
            raise CustomException(e,sys)