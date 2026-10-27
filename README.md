# Dairy Co-op Payment Calculator

A simple program for a dairy co-op. A farmer enters their name and how many litres of milk they supplied, and it shows the total the co-op owes them at this week's buying price. It replaces phoning or WhatsApping each farmer when the price changes.

## Setup

1. Install Python 3.8 or newer from [python.org](https://www.python.org/downloads/). On Windows, tick **"Add Python to PATH"** during installation.
2. Download this folder (on GitHub: **Code → Download ZIP**) and unzip it.

There's nothing else to install.

## Update the weekly price

Open `price.txt` in Notepad. It contains one number, the buying price per litre in KES:

```
55.00
```

Change it to this week's price, save, and close. You don't need to edit any code.

## Run it

Open a terminal in the folder and run:

```bash
python dairy_calculator.py
```

Enter each farmer's name and litres. Press **Enter** on an empty name when you're done.

## Example output

```
Kiambu Dairy Co-op Payment Calculator
----------------------------------------
This week's buying price: KES 55.00 per litre

Farmer name (or press Enter to finish): Wanjiru Kamau
Litres supplied: 12.5

----------------------------------------
  Farmer : Wanjiru Kamau
  Litres : 12.5
  Price  : KES 55.00 per litre
  Total  : KES 687.50
----------------------------------------

Farmer name (or press Enter to finish): John Mwangi
Litres supplied: abc
  Please enter a number, e.g. 12 or 12.5
Litres supplied: 20

----------------------------------------
  Farmer : John Mwangi
  Litres : 20.0
  Price  : KES 55.00 per litre
  Total  : KES 1,100.00
----------------------------------------

Farmer name (or press Enter to finish):

Goodbye.
```

## Input checks

| Situation | What happens |
|---|---|
| Letters instead of litres | Asks again: "Please enter a number" |
| Zero or negative litres | Asks again |
| More than 1,000 litres | Asks the user to check, since it's likely a typing mistake |
| `price.txt` missing | Explains how to create it |
| `price.txt` contains words or a negative number | Explains what it should contain |

## Assumptions

- One buying price applies to all farmers for the week.
- The price is kept in `price.txt` and updated by the co-op manager.
- The tool calculates the amount owed. It doesn't record or store payments (see Version).

## Version

**v1.0** (27 October 2026): first delivered release.

