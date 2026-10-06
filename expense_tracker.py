"""
DecodeLabs - Python Programming | Project 2: The Expense Tracker

Concepts covered (from the project brief):
  * IPO model          -> Input (amount) -> Process (add to total) -> Output (Total Spent)
  * Gatekeeper         -> convert raw text to a number before doing any math
                          ('100' + '50' = '10050' is a disaster; 100 + 50 = 150 is truth)
  * Defensive coding   -> try / except to reject invalid input like "ten"
  * Accumulator        -> total = total + new_expense   (same as total += new_expense)
  * State              -> `total` is initialized OUTSIDE the loop so it is never reset
  * Continuous loop    -> while True:
  * Kill switch        -> type "quit" (sentinel value) to stop and print the final total
  * Decoupling         -> MODEL (calculation logic) is separate from VIEW (print output)
"""

from decimal import Decimal

SENTINEL = "quit"   # typing this stops the program
CURRENCY = "$"      # change to "Rs." or anything you like


# ======================================================================
# MODEL  (Logic only - no input() or print() here)
# ======================================================================
def parse_expense(raw_text):
    """
    PHASE 1 - THE GATEKEEPER.
    Turn raw text into a number. Raise ValueError if the data is not valid.
    Decimal is used instead of float so money is exact (0.1 + 0.2 == 0.3).
    """
    try:
        amount = Decimal(raw_text.strip())
    except Exception:  # Decimal raises InvalidOperation for bad text
        raise ValueError("Invalid data. Please enter a number such as 100 or 49.99.")

    if not amount.is_finite():
        raise ValueError("Invalid data. Please enter a normal number.")
    if amount <= 0:
        raise ValueError("An expense must be greater than zero.")
    return amount


def add_expense(total, new_expense):
    """PHASE 2 - THE ACCUMULATOR: State(new) = State(old) + Input."""
    return total + new_expense


# ======================================================================
# VIEW  (Output only)
# ======================================================================
def money(amount):
    """Format a number as money, e.g. 1500 -> $1,500.00"""
    return f"{CURRENCY}{amount:,.2f}"


def show_welcome():
    print("=" * 40)
    print("        EXPENSE TRACKER")
    print("=" * 40)
    print(f"Enter an expense amount and press Enter.")
    print(f"Type '{SENTINEL}' when you are finished.\n")


def show_running_total(total):
    print(f"   Total so far: {money(total)}")


def show_summary(count, total):
    """PHASE 3 - OUTPUT: display the final result."""
    print("\n" + "=" * 40)
    print(f"Transactions entered : {count}")
    print(f"FINAL TOTAL SPENT    : {money(total)}")
    print("=" * 40)


# ======================================================================
# CONTROLLER  (ties Input -> Process -> Output together)
# ======================================================================
def main():
    total = Decimal("0")   # State is initialized OUTSIDE the loop (memory)
    count = 0

    show_welcome()

    while True:            # The continuous audit loop
        try:
            raw = input("Enter expense: ")
        except (EOFError, KeyboardInterrupt):
            print()        # Ctrl+C / Ctrl+D also shut down gracefully
            break

        # Kill switch (sentinel value)
        if raw.strip().lower() == SENTINEL:
            break

        # Defensive coding: invalid data never reaches the accumulator
        try:
            new_expense = parse_expense(raw)
        except ValueError as error:
            print(f"   {error}")
            continue

        total = add_expense(total, new_expense)
        count += 1
        show_running_total(total)

    show_summary(count, total)


if __name__ == "__main__":
    main()
