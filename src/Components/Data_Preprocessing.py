from src.exception import CustomException
from src.logger import logging
import os,sys
import pandas as pd
from pathlib import Path



class DataPreprocessing:
    def __init__(self,csv_path:str):
        self.save_path = os.path.join("artifacts",'cleaned.csv')
        self.csv_path = csv_path
    
    def preprocess_data(self)->str:
        """
        Reads the HTS CSV file, cleans and preprocesses the data, and saves it to a new CSV file.

        Processing steps:
        - Strips whitespace from 'HTS Number' and 'Description' columns.
        - Fills missing values in duty rate columns ('General Rate of Duty', 
        'Special Rate of Duty', 'Column 2 Rate of Duty') with the string 'Free'.
        - Extracts the unit from 'Unit of Quantity' field if it contains values like '["kg"]' → 'kg'.
        - Filters and retains only relevant columns for further processing.
        - Saves the cleaned data to `self.save_path`.

        Returns:
            str: The file path where the cleaned CSV is saved.

        Raises:
            CustomException: If any error occurs during preprocessing.
        """
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
    

