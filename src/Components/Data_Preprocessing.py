from src.exception import CustomException
from src.logger import logging
import os,sys
import pandas as pd
from pathlib import Path



class DataPreprocessing:
    def __init__(self):
        self.save_path = os.path.join("artifacts",'cleaned.csv')
        self.csv_path = r"D:\Personal projects\HTSAgent-Gnana Chiathanya\artifacts\final.csv"
    
    def preprocess_data(self)->str:
        try:
            df = pd.read_csv(self.csv_path)

            # Clean HTS Number and Description
            df["HTS Number"] = df["HTS Number"].astype(str).str.strip()
            df["Description"] = df["Description"].astype(str).str.strip()

            # Fill missing duty rate values with 'Free'
            duty_columns = ["General Rate of Duty", "Special Rate of Duty", "Column 2 Rate of Duty"]
            df[duty_columns] = df[duty_columns].fillna("Free")

            # Flatten Unit of Quantity like '["kg"]' to 'kg'
            if "Unit of Quantity" in df.columns:
                df["Unit of Quantity"] = df["Unit of Quantity"].astype(str).str.extract(r'"([^"]+)"')

            # Keep only the necessary columns
            cleaned_df = df[[
                "HTS Number", "Description", "Unit of Quantity",
                "General Rate of Duty", "Special Rate of Duty", "Column 2 Rate of Duty"
            ]]

            # Save cleaned data
            cleaned_df.to_csv(self.save_path, index=False,header=True)
            print(f"Cleaned data saved to: {self.save_path}")

            return self.save_path
       
        except Exception as e:
            raise CustomException(e,sys)
    


if __name__=='__main__':
   saved_path =  DataPreprocessing().preprocess_data()