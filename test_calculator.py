#!/usr/bin/env python3
"""
Test script for the investment calculator
"""

from investment_calculator import InvestmentCalculator


def test_basic_investment():
    """Test basic investment without additional contributions"""
    print("Test 1: Basic Investment (No Additional Contributions)")
    print("=" * 55)
    
    calculator = InvestmentCalculator()
    results = calculator.calculate_investment(
        starting_amount=10000,
        years=10,
        annual_return_rate=7,
        additional_contribution=0
    )
    
    print(calculator.get_summary())
    calculator.print_yearly_breakdown()
    print()


def test_monthly_contributions_end():
    """Test with monthly contributions at end of month"""
    print("Test 2: Monthly Contributions at End of Month")
    print("=" * 45)
    
    calculator = InvestmentCalculator()
    results = calculator.calculate_investment(
        starting_amount=5000,
        years=5,
        annual_return_rate=8,
        additional_contribution=500,
        contribution_frequency="monthly",
        contribution_timing="end"
    )
    
    print(calculator.get_summary())
    calculator.print_yearly_breakdown()
    print()


def test_annual_contributions_beginning():
    """Test with annual contributions at beginning of year"""
    print("Test 3: Annual Contributions at Beginning of Year")
    print("=" * 50)
    
    calculator = InvestmentCalculator()
    results = calculator.calculate_investment(
        starting_amount=20000,
        years=8,
        annual_return_rate=6,
        additional_contribution=3000,
        contribution_frequency="annually",
        contribution_timing="beginning"
    )
    
    print(calculator.get_summary())
    calculator.print_yearly_breakdown()
    print()


def test_high_return_scenario():
    """Test with higher return rate"""
    print("Test 4: High Return Scenario")
    print("=" * 28)
    
    calculator = InvestmentCalculator()
    results = calculator.calculate_investment(
        starting_amount=1000,
        years=15,
        annual_return_rate=12,
        additional_contribution=200,
        contribution_frequency="monthly",
        contribution_timing="beginning"
    )
    
    print(calculator.get_summary())
    # Print only first 5 years to keep output manageable
    print("\nFirst 5 Years Breakdown:")
    print("=" * 80)
    print(f"{'Year':<6} {'Starting Balance':<16} {'Contributions':<14} {'Interest':<12} {'Ending Balance':<16}")
    print("-" * 80)
    
    for year_data in calculator.yearly_breakdown[:5]:
        print(f"{year_data['year']:<6} "
              f"${year_data['starting_balance']:<15,.2f} "
              f"${year_data['contributions']:<13,.2f} "
              f"${year_data['interest']:<11,.2f} "
              f"${year_data['ending_balance']:<15,.2f}")
    print("... (showing first 5 years only)")
    print()


if __name__ == "__main__":
    print("Investment Calculator Test Suite")
    print("================================\n")
    
    test_basic_investment()
    test_monthly_contributions_end()
    test_annual_contributions_beginning()
    test_high_return_scenario()
    
    print("All tests completed successfully!")