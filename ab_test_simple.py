
import pandas as pd
import numpy as np
from scipy.stats import shapiro, levene, ttest_ind
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("ab_testing_simple.csv")

# Split
control = df[df["Group"]=="control"]
test = df[df["Group"]=="test"]

# Quick sanity checks
print("Rows:", len(df), "| Control:", len(control), "| Test:", len(test))
print("Columns:", list(df.columns))
print("\nHead:\n", df.head())

# 1) Compare mean Purchases
control_mean = control["Purchase"].mean()
test_mean    = test["Purchase"].mean()
print(f"\nMean Purchase - Control: {control_mean:.2f}, Test: {test_mean:.2f}")

# 2) Assumption checks
# Normality (Shapiro)
_, p_control = shapiro(control["Purchase"])
_, p_test    = shapiro(test["Purchase"])
print(f"Shapiro p-values -> Control: {p_control:.4f}, Test: {p_test:.4f}")

# Variance homogeneity (Levene)
_, p_var = levene(control["Purchase"], test["Purchase"])
print(f"Levene p-value -> {p_var:.4f}")

# 3) Two-sample t-test
equal_var = p_var > 0.05
t_stat, p_val = ttest_ind(test["Purchase"], control["Purchase"], equal_var=equal_var)
print(f"T-test -> t={t_stat:.4f}, p={p_val:.4f} (equal_var={equal_var})")

# 4) Friendly summary
print("\n=== SUMMARY ===")
if p_val < 0.05:
    print("Significant difference: The Test group is different from Control.")
    winner = "test" if test_mean > control_mean else "control"
    print(f"Winner appears to be: {winner}")
else:
    print("No significant difference: The new version did not outperform the old one.")

# 5) Simple chart
means = [control_mean, test_mean]
labels = ["Control", "Test"]

plt.figure()
plt.bar(labels, means)
plt.title("Average Purchases by Group")
plt.ylabel("Average Purchases")
plt.savefig("ab_result.png", bbox_inches="tight")
print("\nSaved chart to ab_result.png")
