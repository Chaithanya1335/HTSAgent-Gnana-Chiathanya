from src.Components.data_ingestion import DataIngestion
from src.Components.Data_transformation import DataTransformation
from src.Components.vector_db import vectordb
from src.Components.Data_Preprocessing import DataPreprocessing
from src.exception import CustomException
from src.logger import logging


if __name__=='__main__':

    folder_path = r'D:\Personal projects\HTSAgent-Gnana Chiathanya\Data\section1_chapters' # Change your csv's files path here
    df,saved_file_path = DataIngestion().get_csv_data(folder_path=folder_path)

    pdf_path = r"D:\Personal projects\HTSAgent-Gnana Chiathanya\Data\General Notes.pdf" # Change your pdf file path here
    docs = DataIngestion().read_pdf(pdf_path=pdf_path)
    chunks = DataTransformation().get_chunks(chunk_size=1000,chunk_overlap=100,docs=docs)

    clean_data_path = DataPreprocessing(csv_path=saved_file_path).preprocess_data()

    persist_path = "artifacts/vectorstore" # path to store Data Locally 
    vdb = vectordb(persist_path=persist_path,docs = chunks)

    print(clean_data_path)