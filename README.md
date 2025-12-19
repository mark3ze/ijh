# Random Code Generator

A Python script that demonstrates various random generation algorithms and statistical calculations.

## Overview

`random_code.py` is a comprehensive random code generator that includes:

### Features

- **RandomGenerator Class**: A utility class for generating random data and performing calculations
  - `generate_random_list()`: Creates lists of random integers
  - `calculate_stats()`: Calculates mean, max, min, and sum of number lists
  - `random_pi_approximation()`: Uses Monte Carlo method to approximate π

- **Utility Functions**:
  - `fibonacci_generator()`: Generates Fibonacci sequence using a generator
  - `random_color_generator()`: Returns random colors from a predefined list

### Main Program

When run, the script:
1. Generates a list of 15 random numbers (1-100)
2. Calculates and displays statistics for those numbers
3. Approximates π using 50,000 Monte Carlo iterations
4. Displays the first 10 Fibonacci numbers
5. Shows 5 random color selections
6. Simulates random delays between 0.1-0.5 seconds

## Usage

Run the script directly:

```bash
python random_code.py
```

## Example Output

```
Random Code Generator - 2025-12-19 04:08:00
==================================================
Random numbers: [42, 17, 89, 3, 56, 91, 28, 74, 15, 33, 67, 8, 45, 92, 21]
Statistics: {'mean': 45.2, 'max': 92, 'min': 3, 'sum': 678}
Pi approximation: 3.14152 (actual: 3.141592653589793)
Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
Random colors: ['blue', 'yellow', 'green', 'purple', 'orange']
Simulating random delays...
  Delay 1: 0.23 seconds
  Delay 2: 0.47 seconds
  Delay 3: 0.15 seconds
```

## Dependencies

- Python 3.x
- Standard library modules: `random`, `math`, `time`, `datetime`

## Technical Details

- Uses seeded random generation for reproducible results
- Monte Carlo method for π approximation with configurable iterations
- Generator-based Fibonacci sequence for memory efficiency
- Object-oriented design with utility functions for modularity
