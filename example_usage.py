#!/usr/bin/env python3
"""
Example of how to use the InvestmentCalculator in another Python script
"""

from investment_calculator import InvestmentCalculator


def example_1_basic_usage():
    """Simple example with basic parameters"""
    calculator = InvestmentCalculator()
    
    # Calculate investment growth
    results = calculator.calculate_investment(
        starting_amount=10000,
        years=10,
        annual_return_rate=7
    )
    
    # Access results
    print(f"Ending Balance: ${results['ending_balance']:,.2f}")
    print(f"Total Interest: ${results['total_interest']:,.2f}")
    
    # Get formatted summary
    print(calculator.get_summary())


def example_2_with_monthly_contributions():
    """Example with monthly contributions"""
    calculator = InvestmentCalculator()
    
    results = calculator.calculate_investment(
        starting_amount=5000,
        years=5,
        annual_return_rate=8,
        additional_contribution=500,
        contribution_frequency="monthly",
        contribution_timing="end"
    )
    
    # Print yearly breakdown
    calculator.print_yearly_breakdown()
    
    # Or get data as list of dictionaries for custom processing
    yearly_data = calculator.get_yearly_breakdown_table()
    print(f"\nYear 3 ending balance: {yearly_data[2]['Ending Balance']}")


def example_3_multiple_scenarios():
    """Compare different investment scenarios"""
    scenarios = [
        {"name": "Conservative", "rate": 5, "contribution": 300},
        {"name": "Moderate", "rate": 7, "contribution": 300},
        {"name": "Aggressive", "rate": 10, "contribution": 300}
    ]
    
    print("Scenario Comparison (10 years, $10k start, $300/month)")
    print("=" * 60)
    
    for scenario in scenarios:
        calculator = InvestmentCalculator()
        results = calculator.calculate_investment(
            starting_amount=10000,
            years=10,
            annual_return_rate=scenario["rate"],
            additional_contribution=scenario["contribution"],
            contribution_frequency="monthly",
            contribution_timing="end"
        )
        
        print(f"{scenario['name']:<12} ({scenario['rate']}%): "
              f"${results['ending_balance']:>10,.2f} "
              f"(Interest: ${results['total_interest']:>8,.2f})")


def example_4_access_individual_years():
    """Access data for individual years"""
    calculator = InvestmentCalculator()
    
    calculator.calculate_investment(
        starting_amount=1000,
        years=5,
        annual_return_rate=8,
        additional_contribution=100,
        contribution_frequency="monthly"
    )
    
    # Access individual year data
    print("Year-by-year growth:")
    for year_data in calculator.yearly_breakdown:
        print(f"Year {year_data['year']}: "
              f"Started with ${year_data['starting_balance']:,.2f}, "
              f"added ${year_data['contributions']:,.2f}, "
              f"earned ${year_data['interest']:,.2f}, "
              f"ended with ${year_data['ending_balance']:,.2f}")


def example_5_save_to_csv():
    """Example of saving results to CSV (if you need that)"""
    calculator = InvestmentCalculator()
    
    calculator.calculate_investment(
        starting_amount=5000,
        years=3,
        annual_return_rate=6,
        additional_contribution=200,
        contribution_frequency="monthly"
    )
    
    # Write to CSV manually (since we removed pandas dependency)
    with open('investment_results.csv', 'w') as f:
        f.write("Year,Starting Balance,Contributions,Interest,Ending Balance\n")
        for year_data in calculator.yearly_breakdown:
            f.write(f"{year_data['year']},"
                   f"{year_data['starting_balance']:.2f},"
                   f"{year_data['contributions']:.2f},"
                   f"{year_data['interest']:.2f},"
                   f"{year_data['ending_balance']:.2f}\n")
    
    print("Results saved to investment_results.csv")


if __name__ == "__main__":
    print("Investment Calculator Usage Examples")
    print("=" * 40)
    
    print("\n1. Basic Usage:")
    example_1_basic_usage()
    
    print("\n2. With Monthly Contributions:")
    example_2_with_monthly_contributions()
    
    print("\n3. Multiple Scenarios:")
    example_3_multiple_scenarios()
    
    print("\n4. Access Individual Years:")
    example_4_access_individual_years()
    
    print("\n5. Save to CSV:")
    example_5_save_to_csv()