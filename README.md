# Weighted Random Generator

Number generator that given a set of numbers and their respective probabilities will generate numbers
according to their weights.

## Requirements

- Python 2.7

## Usage

```
from RandomGen import RandomGen


# Define the numbers to been generated and their respective weight
numbers = [-1, 0, 1, 2, 3]
numbers_probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

# Create the generator
rg = RandomGen(numbers, numbers_probabilities)

# Generate a random number
generated_number = rg.next_num()
```

## Tests

`$ python -m unittest discover -s tests/ -p RandomGenTest.py`
