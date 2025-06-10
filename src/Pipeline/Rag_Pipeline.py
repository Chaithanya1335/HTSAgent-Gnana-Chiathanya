from src.exception import CustomException
from src.logger import logging
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import PromptTemplate
from src.utils import get_llm,get_embedding_model
from dotenv import load_dotenv
import os,sys


load_dotenv()
class Ragpipeline:
    def __init__(self):
        self.GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        self.embedding_model = get_embedding_model(model_name='models/embedding-001',api_key=self.GEMINI_API_KEY)
        self.llm = get_llm(model_name='models/gemini-1.5-flash',api_key=self.GEMINI_API_KEY)
    
    def pipeline(self):
        """
        Constructs and returns a Retrieval-Augmented Generation (RAG) chain using FAISS for retrieval
        and a language model for response generation.

        Returns:
            rag_chain (RunnableSequence): A composed chain that:
                - Retrieves relevant context using a FAISS vector store
                - Formats the input using a prompt template
                - Generates an answer using the initialized language model (self.llm)
                - Parses and returns the final string output

        Raises:
            CustomException: If there is an error during any part of the pipeline setup.
        """
        try:
            logging.info("Initializing RAG pipeline.")

            # Step 1: Create prompt template
            prompt = PromptTemplate.from_template(
                template="you are question answering bot need to answer the question:\n {question} based availble context:\n {context}",
                input_variables=['question', 'context']
            )
            logging.info("Prompt template created.")

            # Step 2: Load FAISS retriever
            retriever = FAISS.load_local(
                folder_path=r'D:\Personal projects\HTSAgent-Gnana Chiathanya\artifacts\vectorstore',
                embeddings=self.embedding_model,
                allow_dangerous_deserialization=True
            ).as_retriever()
            logging.info("FAISS retriever loaded successfully.")

            # Step 3: Load LLM and parser
            llm = self.llm
            parser = StrOutputParser()
            logging.info("LLM and output parser initialized.")

            # Step 4: Define RAG chain
            rag_chain = (
                {'context': retriever, 'question': RunnablePassthrough()}
                | prompt
                | llm
                | parser
            )
            logging.info("RAG pipeline successfully constructed.")

            return rag_chain

        except Exception as e:
            raise CustomException(e, sys)



if __name__ =='__main__':
    rag = Ragpipeline().pipeline()

    print(rag.invoke("According to General Rule of Interpretation 2(a), under what condition can an incomplete or unfinished article be classified as a complete or finished article in the tariff schedule?"))

