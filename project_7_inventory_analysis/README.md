# Inventory Analysis | Project 7

## Objective
Find fast- and slow-moving items using a **quarterly turnover ratio** and make a **Pareto-style chart** to see which products account for most sales volume.

## Data
`inventory.csv` is **synthetic practice data** for 30 products and one sample quarter, **not a real store export**. It includes opening stock, receipts, units sold, ending stock and unit price.

## Tools
Python, pandas and matplotlib.

## How to run
1. Open the project folder in VS Code.
2. Install dependencies: `pip install -r requirements.txt`
3. Run `python analyze.py` (or `py analyze.py` on Windows).
4. Find two charts and two CSV summaries inside `output`.

## Method
- Validate `opening stock + receipts - units sold = closing stock`.
- Calculate `average stock = (opening stock + closing stock) / 2`.
- Calculate `quarterly turnover ratio = units sold / average stock`. This is a simple unit-based **proxy** for inventory turnover in one period, not annual COGS-based inventory turnover.
- Flag fast movers with ratio **>= 1.5**, slow movers with **< 0.75**, and the remainder moderate. These thresholds are **practice assumptions**, not industry rules.
- Rank items by units sold and plot a Pareto-style bar chart with cumulative sales-volume percentage and an 80% reference line.

## Interpretation
- High-turnover items may need regular replenishment checks.
- Low-turnover items may need demand review to avoid excess stock.
- The Pareto chart shows whether sales volume is concentrated in a small number of products; **do not assume** an 80/20 pattern without checking the actual chart.

## My learning
I practised stock calculations, sorting, flags and a cumulative-percentage chart using Python.
