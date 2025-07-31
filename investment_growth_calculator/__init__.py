"""
Investment Growth Calculator

A Python package for calculating investment growth with compound interest
and additional contributions.

Example usage:
    >>> from investment_growth_calculator import InvestmentCalculator
    >>> calculator = InvestmentCalculator()
    >>> results = calculator.calculate_investment(
    ...     starting_amount=10000,
    ...     years=10,
    ...     annual_return_rate=7,
    ...     additional_contribution=500,
    ...     contribution_frequency="monthly"
    ... )
    >>> print(f"Ending balance: ${results['ending_balance']:,.2f}")
"""

from .calculator import InvestmentCalculator

__version__ = "0.1.0"
__author__ = "dakota-robarts"
__email__ = "cody.robarts@yahoo.com"

__all__ = ["InvestmentCalculator"]