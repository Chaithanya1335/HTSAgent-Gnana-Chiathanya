import pandas as pd
import re
from src.exception import CustomException
from src.logger import logging

class DutyCalculator:
    def __init__(self):
        self.csv_path = r"D:\Personal projects\HTSAgent-Gnana Chiathanya\artifacts\cleaned.csv"

    def parse_duty_advanced(self,duty_str, cif_value, unit_weight=None, quantity=None):
        """
        Parses a duty rate string and calculates the corresponding duty based on the given CIF value,
        unit weight, or quantity. Handles different formats including percentages, ¢/kg, and $/unit.

        Args:
            duty_str (str): Duty rate string (e.g., "5%", "2.3 ¢/kg", "$3/unit", "Free").
            cif_value (float): Cost, Insurance, and Freight value used for % based calculations.
            unit_weight (float, optional): Weight in kilograms used for ¢/kg based calculations.
            quantity (int, optional): Quantity used for $/unit based calculations.

        Returns:
            float: Calculated duty amount in USD. Returns 0.0 if duty is "Free" or invalid format.
        """
        if pd.isna(duty_str) or duty_str.strip() == "":
            return 0.0

        duty_str = duty_str.strip().lower()

        if "free" in duty_str:
            return 0.0

        if "%" in duty_str:
            match = re.search(r"([\d.]+)\s*%", duty_str)
            if match:
                return float(match.group(1)) / 100 * cif_value

        if "¢/kg" in duty_str:
            match = re.search(r"([\d.]+)\s*¢/kg", duty_str)
            if match and unit_weight:
                cents_per_kg = float(match.group(1))
                return (cents_per_kg * unit_weight) / 100

        if "$" in duty_str and "/unit" in duty_str:
            match = re.search(r"\$([\d.]+)/unit", duty_str)
            if match and quantity:
                dollars_per_unit = float(match.group(1))
                return dollars_per_unit * quantity

        return 0.0

    def calculate_duty(self,hts_code:str, product_cost:float, freight:float, insurance:float, unit_weight:float, quantity:int)->pd.DataFrame:
        """
        Calculates the duties and total landed cost for a given HTS code based on CIF value.

        Args:
            hts_code (str): The Harmonized Tariff Schedule code to look up.
            product_cost (float): The product's base cost in USD.
            freight (float): The freight cost in USD.
            insurance (float): The insurance cost in USD.
            unit_weight (float): Total weight of the product (in kg) for ¢/kg calculations.
            quantity (int): Number of units for $/unit duty calculations.

        Returns:
            pd.DataFrame: A DataFrame with detailed breakdown including:
                - HTS Code
                - Description
                - CIF Value
                - General Duty, Special Duty, Column 2 Duty
                - Total Landed Cost under each duty type

            str: If the HTS code is not found, returns an error message.
        """
        df = pd.read_csv(self.csv_path)
        cif_value = product_cost + freight + insurance

        match = df[df["HTS Number"].astype(str).str.strip() == hts_code]
        if match.empty:
            return f"No HTS record found for {hts_code}"

        row = match.iloc[0]

        general = self.parse_duty_advanced(row["General Rate of Duty"], cif_value, unit_weight, quantity)
        special = self.parse_duty_advanced(row["Special Rate of Duty"], cif_value, unit_weight, quantity)
        col2 = self.parse_duty_advanced(row["Column 2 Rate of Duty"], cif_value, unit_weight, quantity)

        return pd.DataFrame([{
            "HTS Code": hts_code,
            "Description": row["Description"],
            "CIF Value": cif_value,
            "General Duty": general,
            "Special Duty": special,
            "Column 2 Duty": col2,
            "Total Landed Cost (General)": cif_value + general,
            "Total Landed Cost (Special)": cif_value + special,
            "Total Landed Cost (Column 2)": cif_value + col2
        }])



