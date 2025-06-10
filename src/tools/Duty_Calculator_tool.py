from langchain.tools import tool
from src.Components.Duty_Calculator import DutyCalculator
from src.exception import CustomException
from src.logger import logging
import sys
import re

@tool
def calculate_tariff_duty(input_string: str) -> str:
    """
    Calculate the landed cost and duties for a given product using HTS tariff data.

    Input format:
    "HTS:0101.30.00.00; cost:10000; freight:500; insurance:100; weight:500; qty:5"
    """
    try:
        # Parse key-value pairs from input string
        parts = dict(item.strip().split(":") for item in input_string.split(";"))
        
        hts = parts["HTS"]
        cost = float(parts["cost"])
        freight = float(parts["freight"])
        insurance = float(parts["insurance"])
        weight = float(parts["weight"])
        qty = int(re.sub(r"[^\d]", "", parts["qty"]))

        # Use DutyCalculator class
        calculator = DutyCalculator()
        result_df = calculator.calculate_duty(
            hts_code=hts,
            product_cost=cost,
            freight=freight,
            insurance=insurance,
            unit_weight=weight,
            quantity=qty
        )

        return result_df.to_string(index=False)

    except Exception as e:
        raise CustomException(e,sys) 
