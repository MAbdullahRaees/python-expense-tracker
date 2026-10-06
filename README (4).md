# Expense Tracker (Python)

DecodeLabs Python Programming - Project 2 (Batch 2026).

A command-line expense tracker. Enter expense amounts one after another; the
program adds them up and shows the **Total Spent** when you type `quit`.

## Features
- Accumulator pattern: `total = total + new_expense`
- Input validation with `try / except` (rejects text like "ten", zero and negative amounts)
- Continuous `while True` loop with a `quit` kill switch
- Uses `Decimal` for exact money calculations
- Calculation logic (model) separated from display (view)

## Run
Requires Python 3.8+.

```bash
python expense_tracker.py
```

## Example
```
Enter expense: 100
   Total so far: $100.00
Enter expense: 50
   Total so far: $150.00
Enter expense: ten
   Invalid data. Please enter a number such as 100 or 49.99.
Enter expense: 20
   Total so far: $170.00
Enter expense: quit

========================================
Transactions entered : 3
FINAL TOTAL SPENT    : $170.00
========================================
```

## Concepts practiced
Accumulators, `while` loops, sentinel values, type conversion, exception handling, `if __name__ == "__main__"`.
