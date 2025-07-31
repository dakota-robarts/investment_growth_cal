#!/usr/bin/env python3
"""
Test the installed package
"""

def test_package_import():
    """Test that we can import the package"""
    try:
        from investment_growth_calculator import InvestmentCalculator
        print("[PASS] Package import successful")
        return True
    except ImportError as e:
        print(f"[FAIL] Package import failed: {e}")
        return False


def test_basic_calculation():
    """Test basic calculation functionality"""
    try:
        from investment_growth_calculator import InvestmentCalculator
        
        calculator = InvestmentCalculator()
        results = calculator.calculate_investment(
            starting_amount=10000,
            years=5,
            annual_return_rate=7,
            additional_contribution=500,
            contribution_frequency="monthly"
        )
        
        print(f"[PASS] Basic calculation successful")
        print(f"  Ending Balance: ${results['ending_balance']:,.2f}")
        print(f"  Total Contributions: ${results['total_contributions']:,.2f}")
        print(f"  Total Interest: ${results['total_interest']:,.2f}")
        return True
        
    except Exception as e:
        print(f"[FAIL] Basic calculation failed: {e}")
        return False


def test_package_attributes():
    """Test package attributes"""
    try:
        import investment_growth_calculator
        
        print(f"[PASS] Package version: {investment_growth_calculator.__version__}")
        print(f"[PASS] Package author: {investment_growth_calculator.__author__}")
        print(f"[PASS] Package exports: {investment_growth_calculator.__all__}")
        return True
        
    except Exception as e:
        print(f"[FAIL] Package attributes test failed: {e}")
        return False


def test_cli_import():
    """Test CLI module import"""
    try:
        from investment_growth_calculator.cli import main
        print("[PASS] CLI module import successful")
        return True
    except ImportError as e:
        print(f"[FAIL] CLI module import failed: {e}")
        return False


if __name__ == "__main__":
    print("Testing Investment Growth Calculator Package")
    print("=" * 45)
    
    tests = [
        test_package_import,
        test_basic_calculation,
        test_package_attributes,
        test_cli_import
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! Package is working correctly.")
    else:
        print("Some tests failed. Please check the errors above.")