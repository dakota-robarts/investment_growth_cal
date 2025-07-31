#!/usr/bin/env python3
"""
Investment Calculator
Mimics functionality from calculator.net investment calculator
"""

from typing import Dict, List


class InvestmentCalculator:
    def __init__(self):
        self.results = {}
        self.yearly_breakdown = []
    
    def calculate_investment(
        self,
        starting_amount: float,
        years: int,
        annual_return_rate: float,
        additional_contribution: float = 0,
        contribution_frequency: str = "monthly",  # "monthly" or "annually"
        contribution_timing: str = "end"  # "beginning" or "end"
    ) -> Dict[str, float]:
        """
        Calculate investment growth with compound interest and additional contributions
        
        Args:
            starting_amount: Initial investment amount
            years: Number of years to invest
            annual_return_rate: Annual return rate as percentage (e.g., 7 for 7%)
            additional_contribution: Additional contribution amount
            contribution_frequency: "monthly" or "annually"
            contribution_timing: "beginning" or "end" of period
        
        Returns:
            Dictionary with total balance, total contributions, and total interest
        """
        # Convert percentage to decimal
        annual_rate = annual_return_rate / 100
        
        # Initialize variables
        balance = starting_amount
        total_contributions = starting_amount
        self.yearly_breakdown = []
        
        # Determine contribution parameters
        if contribution_frequency == "monthly":
            periods_per_year = 12
            periodic_rate = annual_rate / 12
            periodic_contribution = additional_contribution
        else:  # annually
            periods_per_year = 1
            periodic_rate = annual_rate
            periodic_contribution = additional_contribution
        
        # Calculate for each year
        for year in range(1, years + 1):
            year_start_balance = balance
            year_contributions = 0
            year_interest = 0
            
            # Calculate for each period in the year
            for period in range(periods_per_year):
                # Add contribution at beginning of period if specified
                if contribution_timing == "beginning" and additional_contribution > 0:
                    balance += periodic_contribution
                    year_contributions += periodic_contribution
                    total_contributions += periodic_contribution
                
                # Calculate interest for this period
                period_interest = balance * periodic_rate
                balance += period_interest
                year_interest += period_interest
                
                # Add contribution at end of period if specified
                if contribution_timing == "end" and additional_contribution > 0:
                    balance += periodic_contribution
                    year_contributions += periodic_contribution
                    total_contributions += periodic_contribution
            
            # Store yearly breakdown
            self.yearly_breakdown.append({
                'year': year,
                'starting_balance': year_start_balance,
                'contributions': year_contributions,
                'interest': year_interest,
                'ending_balance': balance
            })
        
        total_interest = balance - total_contributions
        
        self.results = {
            'ending_balance': balance,
            'total_contributions': total_contributions,
            'total_interest': total_interest
        }
        
        return self.results
    
    def get_summary(self) -> str:
        """Return formatted summary of results"""
        if not self.results:
            return "No calculation performed yet."
        
        summary = f"""
Investment Calculator Results
============================
Ending Balance:      ${self.results['ending_balance']:,.2f}
Total Contributions: ${self.results['total_contributions']:,.2f}
Total Interest:      ${self.results['total_interest']:,.2f}
"""
        return summary
    
    def get_yearly_breakdown_table(self) -> List[Dict]:
        """Return yearly breakdown as a list of dictionaries"""
        if not self.yearly_breakdown:
            return []
        
        formatted_data = []
        for row in self.yearly_breakdown:
            formatted_row = {
                'Year': row['year'],
                'Starting Balance': f"${row['starting_balance']:,.2f}",
                'Contributions': f"${row['contributions']:,.2f}",
                'Interest': f"${row['interest']:,.2f}",
                'Ending Balance': f"${row['ending_balance']:,.2f}"
            }
            formatted_data.append(formatted_row)
        
        return formatted_data
    
    def print_yearly_breakdown(self):
        """Print formatted yearly breakdown table"""
        if not self.yearly_breakdown:
            print("No yearly breakdown available.")
            return
        
        print("\nYearly Breakdown")
        print("=" * 80)
        print(f"{'Year':<6} {'Starting Balance':<16} {'Contributions':<14} {'Interest':<12} {'Ending Balance':<16}")
        print("-" * 80)
        
        for year_data in self.yearly_breakdown:
            print(f"{year_data['year']:<6} "
                  f"${year_data['starting_balance']:<15,.2f} "
                  f"${year_data['contributions']:<13,.2f} "
                  f"${year_data['interest']:<11,.2f} "
                  f"${year_data['ending_balance']:<15,.2f}")


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