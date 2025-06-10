from langchain.tools import tool
from src.Components.Duty_Calculator import DutyCalculator
from src.exception import CustomException
from src.logger import logging
import sys
import re

@tool
def calculate_tariff_duty(input_string: str) -> str:
    """
    Calculates the landed cost and import duties for a product based on HTS tariff data.

    This function parses an input string containing product details, including
    HTS code, cost, freight, insurance, weight, and quantity. It then uses
    the `DutyCalculator` to compute the applicable duties and returns the
    result as a formatted string (typically a DataFrame converted to string).

    The input string must adhere to the following format:
    "HTS:0101.30.00.00; cost:10000; freight:500; insurance:100; weight:500; qty:5"

    Args:
        input_string (str): A semicolon-separated string containing key-value
                            pairs of product details. Expected keys are:
                            "HTS", "cost", "freight", "insurance", "weight", "qty".

    Returns:
        str: A string representation of the calculation result, typically a
             DataFrame converted to a string, showing landed cost and duties.

    Raises:
        CustomException: If parsing of the input string fails, or if there's
                         an error during the duty calculation process within
                         the `DutyCalculator`. The original exception details
                         are captured and re-raised within `CustomException`.

    Example:
        >>> input_data = "HTS:0101.30.00.00; cost:10000; freight:500; insurance:100; weight:500; qty:5"
        >>> result = calculate_tariff_duty(input_data)
        >>> print(result)
        # Expected output will be a string representation of the DataFrame, e.g.:
        #   HTS Code  Product Cost  Freight  Insurance  ... Total Landed Cost
        # 0  0101.30.00.00         10000      500        100  ...              ...
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
