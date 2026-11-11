"""Beginner inventory turnover and Pareto analysis, sample quarter."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
OUT = BASE / "output"
OUT.mkdir(exist_ok=True)
df = pd.read_csv(BASE / "inventory.csv")
assert (df["opening_stock"] + df["units_received"] - df["units_sold"] == df["closing_stock"]).all(), "Stock quantities do not balance"
# Average inventory is a simple approximation for this sample quarter.
df["average_stock"] = (df["opening_stock"] + df["closing_stock"]) / 2
df["turnover_ratio"] = (df["units_sold"] / df["average_stock"]).round(2)
def label(ratio):
    if ratio >= 1.5: return "Fast-moving"
    if ratio < 0.75: return "Slow-moving"
    return "Moderate"
df["movement"] = df["turnover_ratio"].apply(label)
df["sales_value_inr"] = (df["units_sold"] * df["unit_price_inr"]).round(2)
df.sort_values("turnover_ratio", ascending=False).to_csv(OUT / "inventory_turnover_summary.csv",index=False)
print("Inventory items:", len(df))
print("Total units sold:", df["units_sold"].sum())
print("\nMovement categories:")
print(df["movement"].value_counts().to_string())
print("\nTop 10 by turnover:\n", df.nlargest(10,"turnover_ratio")[["item_name","turnover_ratio","movement"]].to_string(index=False))

fig, ax=plt.subplots(figsize=(9,5))
top=df.nlargest(10,"turnover_ratio").sort_values("turnover_ratio")
ax.barh(top["item_name"],top["turnover_ratio"])
ax.set_xlabel("Quarterly turnover ratio (units sold / avg stock)")
ax.set_title("Top 10 inventory items by turnover")
fig.tight_layout(); fig.savefig(OUT/"top_10_turnover.png",dpi=150); plt.close(fig)

# Pareto: sort by units sold, then plot bars plus cumulative %.
pareto=df.sort_values("units_sold",ascending=False).copy()
pareto["cumulative_pct"] = (pareto["units_sold"].cumsum()/pareto["units_sold"].sum()*100).round(1)
pareto[["item_id","item_name","units_sold","cumulative_pct"]].to_csv(OUT/"pareto_units_sold.csv",index=False)
fig, ax=plt.subplots(figsize=(11,5))
ax.bar(range(len(pareto)),pareto["units_sold"],label="Units sold")
ax.set_xlabel("Items ranked by units sold")
ax.set_ylabel("Units sold")
ax.set_title("Pareto analysis: sales volume by item")
ax2=ax.twinx()
ax2.plot(range(len(pareto)),pareto["cumulative_pct"],marker="o",markersize=2,label="Cumulative %")
ax2.axhline(80,linestyle="--",linewidth=1)
ax2.set_ylim(0,105)
ax2.set_ylabel("Cumulative share (%)")
fig.tight_layout(); fig.savefig(OUT/"pareto_chart.png",dpi=150); plt.close(fig)

print("\nSaved summary, Pareto table, and charts in output folder.")
