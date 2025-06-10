import pandas as pd
import re
from src.exception import CustomException
from src.logger import logging

class DutyCalculator:
    def __init__(self):
        self.csv_path = r"D:\Personal projects\HTSAgent-Gnana Chiathanya\artifacts\cleaned.csv"

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

    def calculate_duty(self,hts_code, product_cost, freight, insurance, unit_weight, quantity):
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



