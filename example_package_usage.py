#!/usr/bin/env python3
"""
Example of using the installed investment-growth-calculator package
"""

# Now you can import from the installed package
from investment_growth_calculator import InvestmentCalculator


def main():
    """Demonstrate package usage"""
    print("Investment Growth Calculator Package Demo")
    print("=" * 42)
    
    # Create calculator instance
    calculator = InvestmentCalculator()
    
    # Example 1: Basic calculation
    print("\n1. Basic Investment (No additional contributions)")
    results = calculator.calculate_investment(
        starting_amount=10000,
        years=10,
        annual_return_rate=7
    )
    
    print(calculator.get_summary())
    
    # Example 2: With monthly contributions
    print("\n2. With Monthly Contributions")
    calculator2 = InvestmentCalculator()
    results2 = calculator2.calculate_investment(
        starting_amount=5000,
        years=5,
        annual_return_rate=8,
        additional_contribution=500,
        contribution_frequency="monthly",
        contribution_timing="end"
    )
    
    print(f"Ending Balance: ${results2['ending_balance']:,.2f}")
    print(f"Total Interest: ${results2['total_interest']:,.2f}")
    
    # Show first 3 years of breakdown
    print("\nFirst 3 Years:")
    for i, year_data in enumerate(calculator2.yearly_breakdown[:3]):
        print(f"Year {year_data['year']}: ${year_data['ending_balance']:,.2f}")


if __name__ == "__main__":
    main()