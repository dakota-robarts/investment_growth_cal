# Investment Growth Calculator

A Python package for calculating investment growth with compound interest and additional contributions. This package mimics the functionality of online investment calculators, providing detailed year-by-year breakdowns of investment growth.

## Features

- **Compound Interest Calculations**: Calculate investment growth with compound interest
- **Additional Contributions**: Support for monthly or annual additional contributions
- **Flexible Timing**: Contributions can be made at the beginning or end of each period
- **Detailed Breakdown**: Year-by-year analysis showing contributions, interest, and ending balances
- **Command Line Interface**: Easy-to-use CLI for quick calculations
- **Python API**: Clean programmatic interface for integration into other applications

## Installation

### Using Poetry (Recommended)

```bash
poetry add investment-growth-calculator
```

### Using pip

```bash
pip install investment-growth-calculator
```

### Local Development

```bash
git clone https://github.com/dakota-robarts/investment-growth-calculator
cd investment-growth-calculator
poetry install
```

## Usage

### Python API

```python
from investment_growth_calculator import InvestmentCalculator

# Create calculator instance
calculator = InvestmentCalculator()

# Calculate investment growth
results = calculator.calculate_investment(
    starting_amount=10000,
    years=10,
    annual_return_rate=7,
    additional_contribution=500,
    contribution_frequency="monthly",  # "monthly" or "annually"
    contribution_timing="end"  # "beginning" or "end"
)

# Access results
print(f"Ending Balance: ${results['ending_balance']:,.2f}")
print(f"Total Contributions: ${results['total_contributions']:,.2f}")
print(f"Total Interest: ${results['total_interest']:,.2f}")

# Get formatted summary
print(calculator.get_summary())

# Print year-by-year breakdown
calculator.print_yearly_breakdown()
```

### Command Line Interface

```bash
# Run the interactive calculator
investment-calculator

# Or if installed locally
python -m investment_growth_calculator.cli
```

### Example Output

```
Investment Calculator Results
============================
Ending Balance:      $72,022.06
Total Contributions: $46,000.00
Total Interest:      $26,022.06

Yearly Breakdown
================================================================================
Year   Starting Balance Contributions  Interest     Ending Balance  
--------------------------------------------------------------------------------
1      $10,000.00       $6,000.00      $984.15      $16,984.15      
2      $16,984.15       $6,000.00      $1,410.71    $24,394.86      
3      $24,394.86       $6,000.00      $1,876.36    $32,271.22      
...
```

## API Reference

### InvestmentCalculator

The main calculator class that handles all investment calculations.

#### Methods

##### `calculate_investment(starting_amount, years, annual_return_rate, additional_contribution=0, contribution_frequency="monthly", contribution_timing="end")`

Calculate investment growth with the given parameters.

**Parameters:**
- `starting_amount` (float): Initial investment amount
- `years` (int): Number of years to invest
- `annual_return_rate` (float): Annual return rate as percentage (e.g., 7 for 7%)
- `additional_contribution` (float, optional): Additional contribution amount. Defaults to 0.
- `contribution_frequency` (str, optional): "monthly" or "annually". Defaults to "monthly".
- `contribution_timing` (str, optional): "beginning" or "end" of period. Defaults to "end".

**Returns:**
- `dict`: Dictionary with keys 'ending_balance', 'total_contributions', 'total_interest'

**Raises:**
- `ValueError`: If invalid parameters are provided

##### `get_summary()`

Returns a formatted string summary of the calculation results.

##### `print_yearly_breakdown()`

Prints a formatted table showing year-by-year breakdown of the investment growth.

##### `get_yearly_breakdown_table()`

Returns the yearly breakdown data as a list of dictionaries for custom processing.

## Examples

### Basic Investment (No Additional Contributions)

```python
calculator = InvestmentCalculator()
results = calculator.calculate_investment(
    starting_amount=10000,
    years=10,
    annual_return_rate=7
)
# Results: ~$19,671 ending balance
```

### Monthly Contributions

```python
calculator = InvestmentCalculator()
results = calculator.calculate_investment(
    starting_amount=5000,
    years=5,
    annual_return_rate=8,
    additional_contribution=500,
    contribution_frequency="monthly",
    contribution_timing="end"
)
# Results: ~$44,188 ending balance
```

### Annual Contributions at Beginning of Year

```python
calculator = InvestmentCalculator()
results = calculator.calculate_investment(
    starting_amount=20000,
    years=8,
    annual_return_rate=6,
    additional_contribution=3000,
    contribution_frequency="annually",
    contribution_timing="beginning"
)
# Results: ~$63,351 ending balance
```

### Scenario Comparison

```python
scenarios = [
    {"name": "Conservative", "rate": 5},
    {"name": "Moderate", "rate": 7},
    {"name": "Aggressive", "rate": 10}
]

for scenario in scenarios:
    calculator = InvestmentCalculator()
    results = calculator.calculate_investment(
        starting_amount=10000,
        years=10,
        annual_return_rate=scenario["rate"],
        additional_contribution=300,
        contribution_frequency="monthly"
    )
    print(f"{scenario['name']}: ${results['ending_balance']:,.2f}")
```

## Development

### Running Tests

```bash
poetry run pytest
```

### Code Formatting

```bash
poetry run black .
```

### Type Checking

```bash
poetry run mypy investment_growth_calculator
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### Version 0.1.0
- Initial release
- Basic investment calculation functionality
- Support for monthly and annual contributions
- Command line interface
- Comprehensive documentation and examples