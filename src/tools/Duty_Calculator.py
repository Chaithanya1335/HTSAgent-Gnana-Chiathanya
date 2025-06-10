import pandas as pd
import re
from src.exception import CustomException
from src.logger import logging
from langchain.agents.tools import tool
import sys

def parse_duty_advanced(self,duty_str, cif_value, unit_weight=None, quantity=None):
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

@tool
def calculate_tariff_duty(input_str: str) -> str:
    """
    Calculates duties for a product. 
    Input format: 
    'HTS:0101.30.00.00; cost:10000; freight:500; insurance:100; weight:500; qty:5'
    """
    try:
        CSV_PATH = r"D:\Personal projects\HTSAgent-Gnana Chiathanya\artifacts\cleaned.csv"
        parts = dict([x.strip().split(":") for x in input_str.split(";")])
        hts = parts["HTS"]
        cost = float(parts["cost"])
        freight = float(parts["freight"])
        insurance = float(parts["insurance"])
        weight = float(parts["weight"])
        qty = int(parts["qty"])

        df = pd.read_csv(CSV_PATH)
        cif = cost + freight + insurance

        match = df[df["HTS Number"].astype(str).str.strip() == hts]
        if match.empty:
            return f"No HTS record found for {hts}"

        row = match.iloc[0]

        general = parse_duty_advanced(row["General Rate of Duty"], cif, weight, qty)
        special = parse_duty_advanced(row["Special Rate of Duty"], cif, weight, qty)
        col2 = parse_duty_advanced(row["Column 2 Rate of Duty"], cif, weight, qty)

        return (
            f"HTS Code: {hts}\n"
            f"Description: {row['Description']}\n"
            f"CIF Value: {cif}\n"
            f"General Duty: ${general:.2f}\n"
            f"Special Duty: ${special:.2f}\n"
            f"Column 2 Duty: ${col2:.2f}\n"
            f"Landed Cost (General): ${cif + general:.2f}\n"
            f"Landed Cost (Special): ${cif + special:.2f}\n"
            f"Landed Cost (Column 2): ${cif + col2:.2f}"
        )
    except Exception as e:
        raise CustomException(e,sys)



