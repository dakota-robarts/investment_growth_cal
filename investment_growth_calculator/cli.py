#!/usr/bin/env python3
"""
Investment Calculator CLI
Command-line interface for the investment calculator
"""

from .calculator import InvestmentCalculator


def main():
    """Main function to run the investment calculator interactively"""
    calculator = InvestmentCalculator()
    
    print("Investment Calculator")
    print("====================")
    
    try:
        # Get input from user
        starting_amount = float(input("Enter starting amount ($): "))
        years = int(input("Enter number of years: "))
        annual_return_rate = float(input("Enter annual return rate (%): "))
        
        # Additional contributions
        has_additional = input("Do you want to make additional contributions? (y/n): ").lower() == 'y'
        
        if has_additional:
            additional_contribution = float(input("Enter additional contribution amount ($): "))
            
            print("\nContribution frequency:")
            print("1. Monthly")
            print("2. Annually")
            freq_choice = input("Choose (1 or 2): ")
            contribution_frequency = "monthly" if freq_choice == "1" else "annually"
            
            print("\nContribution timing:")
            print("1. Beginning of period")
            print("2. End of period")
            timing_choice = input("Choose (1 or 2): ")
            contribution_timing = "beginning" if timing_choice == "1" else "end"
        else:
            additional_contribution = 0
            contribution_frequency = "monthly"
            contribution_timing = "end"
        
        # Calculate investment
        results = calculator.calculate_investment(
            starting_amount=starting_amount,
            years=years,
            annual_return_rate=annual_return_rate,
            additional_contribution=additional_contribution,
            contribution_frequency=contribution_frequency,
            contribution_timing=contribution_timing
        )
        
        # Display results
        print(calculator.get_summary())
        calculator.print_yearly_breakdown()
        
    except ValueError as e:
        print(f"Error: Please enter valid numeric values. {e}")
    except KeyboardInterrupt:
        print("\nCalculation cancelled.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()