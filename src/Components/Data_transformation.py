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
        Splits a list of LangChain Document objects into smaller chunks
        using recursive character splitting.

        This function is crucial for preparing large documents for
        processing by language models or for populating vector stores,
        as it breaks down content into manageable, contextually relevant pieces.
        It uses `RecursiveCharacterTextSplitter` to intelligently split text
        based on a hierarchy of separators, aiming to keep related content together.

        Args:
            chunk_size (int): The maximum size of each chunk in characters.
                            This determines the approximate length of the output chunks.
            chunk_overlap (int): The number of overlapping characters between consecutive chunks.
                                Overlap helps to preserve context across chunk boundaries,
                                reducing the chance of losing information at splits.
            docs (List[Document]): A list of LangChain Document objects to be chunked.
                                Each document in this list will be processed.

        Returns:
            List[Document]: A new list containing the smaller, chunked Document objects.
                            Each chunk will also retain metadata from its original parent document.

        Raises:
            CustomException: If an error occurs during the document splitting process,
                            such as issues with text splitter configuration or
                            unexpected input document formats.
        """
       
        logging.info("Data Transformation Started")

        try:
            splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)

            chunks = splitter.split_documents(docs)

            logging.info(f"Chunking of data completed and no of chunks created is {len(chunks)}")

            return chunks
        
    
        except Exception as e:
            raise CustomException(e,sys)