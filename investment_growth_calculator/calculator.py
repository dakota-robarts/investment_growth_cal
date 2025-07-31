#!/usr/bin/env python3
"""
Investment Calculator
Core calculator functionality for investment growth calculations
"""

from typing import Dict, List


class InvestmentCalculator:
    """
    Investment calculator with compound interest and additional contributions
    
    This class provides functionality to calculate investment growth over time
    with support for additional periodic contributions at the beginning or end
    of each period (monthly or annually).
    """
    
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
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        # Validate inputs
        if starting_amount < 0:
            raise ValueError("Starting amount cannot be negative")
        if years <= 0:
            raise ValueError("Years must be positive")
        if annual_return_rate < 0:
            raise ValueError("Annual return rate cannot be negative")
        if additional_contribution < 0:
            raise ValueError("Additional contribution cannot be negative")
        if contribution_frequency not in ["monthly", "annually"]:
            raise ValueError("Contribution frequency must be 'monthly' or 'annually'")
        if contribution_timing not in ["beginning", "end"]:
            raise ValueError("Contribution timing must be 'beginning' or 'end'")
        
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