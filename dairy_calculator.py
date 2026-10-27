"""
Dairy Co-op Payment Calculator
------------------------------
A farmer enters their name and the litres of milk they supplied, and the
tool shows how much the co-op owes them at this week's buying price.

The buying price is kept in price.txt (a single number, e.g. 55.00).
The co-op manager updates that one number each week - no code changes.

Usage:
    python dairy_calculator.py

Requirements:
    Python 3.8 or newer. No extra packages needed.
"""

from pathlib import Path

PRICE_FILE = Path(__file__).with_name("price.txt")
LINE = "-" * 40


class PriceError(Exception):
    """The price file is missing or doesn't contain a valid price."""


def get_current_price():
    """Read this week's buying price per litre from price.txt."""
    try:
        text = PRICE_FILE.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        raise PriceError(f"Price file not found. Create {PRICE_FILE.name} containing "
                         "this week's price per litre, e.g. 55.00")
    try:
        price = float(text.replace(",", ""))
    except ValueError:
        raise PriceError(f"{PRICE_FILE.name} should contain only a number, e.g. 55.00 "
                         f"(it currently says '{text}').")
    if price <= 0:
        raise PriceError(f"The price in {PRICE_FILE.name} must be more than zero.")
    return price


def calculate_payment(litres, price_per_litre):
    return round(litres * price_per_litre, 2)


def ask_litres():
    """Keep asking until the farmer enters a valid positive number."""
    while True:
        raw = input("Litres supplied: ").strip().replace(",", "")
        try:
            litres = float(raw)
        except ValueError:
            print("  Please enter a number, e.g. 12 or 12.5")
            continue
        if litres <= 0:
            print("  Litres must be more than zero.")
            continue
        if litres > 1000:
            print("  That seems too high for one farmer. Please check and re-enter.")
            continue
        return litres


def calculate_for_one_farmer(price):
    name = input("\nFarmer name (or press Enter to finish): ").strip()
    if not name:
        return False

    litres = ask_litres()
    total = calculate_payment(litres, price)

    print()
    print(LINE)
    print(f"  Farmer : {name.title()}")
    print(f"  Litres : {litres:,.1f}")
    print(f"  Price  : KES {price:,.2f} per litre")
    print(f"  Total  : KES {total:,.2f}")
    print(LINE)
    return True


def main():
    print("Kiambu Dairy Co-op Payment Calculator")
    print(LINE)
    try:
        price = get_current_price()
    except PriceError as err:
        print(f"Sorry: {err}")
        return

    print(f"This week's buying price: KES {price:,.2f} per litre")
    try:
        while calculate_for_one_farmer(price):
            pass
    except (KeyboardInterrupt, EOFError):
        print()
    print("\nGoodbye.")


if __name__ == "__main__":
    main()
