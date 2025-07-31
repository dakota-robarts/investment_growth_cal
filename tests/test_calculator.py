#!/usr/bin/env python3
"""
Tests for the investment calculator
"""

import pytest
from investment_growth_calculator import InvestmentCalculator


class TestInvestmentCalculator:
    """Test cases for InvestmentCalculator class"""
    
    def test_basic_investment_no_contributions(self):
        """Test basic investment without additional contributions"""
        calculator = InvestmentCalculator()
        results = calculator.calculate_investment(
            starting_amount=10000,
            years=10,
            annual_return_rate=7
        )
        
        # Expected: 10000 * (1.07)^10 ≈ 19671.51
        assert abs(results['ending_balance'] - 19671.51) < 1
        assert results['total_contributions'] == 10000
        assert abs(results['total_interest'] - 9671.51) < 1
        assert len(calculator.yearly_breakdown) == 10
    
    def test_monthly_contributions_end(self):
        """Test with monthly contributions at end of month"""
        calculator = InvestmentCalculator()
        results = calculator.calculate_investment(
            starting_amount=1000,
            years=2,
            annual_return_rate=12,
            additional_contribution=100,
            contribution_frequency="monthly",
            contribution_timing="end"
        )
        
        # Should have starting amount + 24 monthly contributions
        expected_contributions = 1000 + (24 * 100)
        assert results['total_contributions'] == expected_contributions
        assert results['ending_balance'] > expected_contributions
        assert len(calculator.yearly_breakdown) == 2
    
    def test_annual_contributions_beginning(self):
        """Test with annual contributions at beginning of year"""
        calculator = InvestmentCalculator()
        results = calculator.calculate_investment(
            starting_amount=5000,
            years=3,
            annual_return_rate=8,
            additional_contribution=1000,
            contribution_frequency="annually",
            contribution_timing="beginning"
        )
        
        # Should have starting amount + 3 annual contributions
        expected_contributions = 5000 + (3 * 1000)
        assert results['total_contributions'] == expected_contributions
        assert results['ending_balance'] > expected_contributions
        assert len(calculator.yearly_breakdown) == 3
    
    def test_zero_return_rate(self):
        """Test with zero return rate"""
        calculator = InvestmentCalculator()
        results = calculator.calculate_investment(
            starting_amount=1000,
            years=5,
            annual_return_rate=0,
            additional_contribution=100,
            contribution_frequency="monthly"
        )
        
        # With 0% return, ending balance should equal total contributions
        expected_contributions = 1000 + (5 * 12 * 100)
        assert results['ending_balance'] == expected_contributions
        assert results['total_interest'] == 0
    
    def test_input_validation(self):
        """Test input validation"""
        calculator = InvestmentCalculator()
        
        # Test negative starting amount
        with pytest.raises(ValueError):
            calculator.calculate_investment(-1000, 10, 7)
        
        # Test zero years
        with pytest.raises(ValueError):
            calculator.calculate_investment(1000, 0, 7)
        
        # Test negative return rate
        with pytest.raises(ValueError):
            calculator.calculate_investment(1000, 10, -5)
        
        # Test invalid frequency
        with pytest.raises(ValueError):
            calculator.calculate_investment(1000, 10, 7, 100, "weekly")
        
        # Test invalid timing
        with pytest.raises(ValueError):
            calculator.calculate_investment(1000, 10, 7, 100, "monthly", "middle")
    
    def test_get_summary(self):
        """Test get_summary method"""
        calculator = InvestmentCalculator()
        
        # Test before calculation
        summary = calculator.get_summary()
        assert "No calculation performed" in summary
        
        # Test after calculation
        calculator.calculate_investment(1000, 1, 10)
        summary = calculator.get_summary()
        assert "Investment Calculator Results" in summary
        assert "Ending Balance" in summary
        assert "Total Contributions" in summary
        assert "Total Interest" in summary
    
    def test_yearly_breakdown_table(self):
        """Test get_yearly_breakdown_table method"""
        calculator = InvestmentCalculator()
        
        # Test before calculation
        breakdown = calculator.get_yearly_breakdown_table()
        assert breakdown == []
        
        # Test after calculation
        calculator.calculate_investment(1000, 2, 10)
        breakdown = calculator.get_yearly_breakdown_table()
        
        assert len(breakdown) == 2
        assert 'Year' in breakdown[0]
        assert 'Starting Balance' in breakdown[0]
        assert 'Contributions' in breakdown[0]
        assert 'Interest' in breakdown[0]
        assert 'Ending Balance' in breakdown[0]
        
        # Check formatting (should have $ signs)
        assert breakdown[0]['Starting Balance'].startswith('$')
        assert breakdown[0]['Ending Balance'].startswith('$')
    
    def test_contribution_timing_difference(self):
        """Test that contribution timing makes a difference"""
        calculator_beginning = InvestmentCalculator()
        calculator_end = InvestmentCalculator()
        
        # Calculate with contributions at beginning
        results_beginning = calculator_beginning.calculate_investment(
            starting_amount=1000,
            years=2,
            annual_return_rate=10,
            additional_contribution=1000,
            contribution_frequency="annually",
            contribution_timing="beginning"
        )
        
        # Calculate with contributions at end
        results_end = calculator_end.calculate_investment(
            starting_amount=1000,
            years=2,
            annual_return_rate=10,
            additional_contribution=1000,
            contribution_frequency="annually",
            contribution_timing="end"
        )
        
        # Beginning contributions should result in higher ending balance
        # because they have more time to compound
        assert results_beginning['ending_balance'] > results_end['ending_balance']
        
        # Both should have same total contributions
        assert results_beginning['total_contributions'] == results_end['total_contributions']
    
    def test_high_precision_calculation(self):
        """Test calculation precision with complex scenario"""
        calculator = InvestmentCalculator()
        results = calculator.calculate_investment(
            starting_amount=1234.56,
            years=15,
            annual_return_rate=7.25,
            additional_contribution=123.45,
            contribution_frequency="monthly",
            contribution_timing="beginning"
        )
        
        # Verify that results are reasonable
        expected_contributions = 1234.56 + (15 * 12 * 123.45)
        assert abs(results['total_contributions'] - expected_contributions) < 0.01
        assert results['ending_balance'] > results['total_contributions']
        assert results['total_interest'] > 0
        
        # Verify yearly breakdown adds up
        total_from_breakdown = sum(year['contributions'] for year in calculator.yearly_breakdown)
        total_from_breakdown += 1234.56  # Add starting amount
        assert abs(total_from_breakdown - results['total_contributions']) < 0.01