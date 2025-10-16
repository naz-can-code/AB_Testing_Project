# 🧪 A/B Testing Project — Comparing Bidding Methods

## 🎯 Objective
To determine whether a new bidding method (Test Group) increases purchase conversions compared to the existing method (Control Group).

## 📊 Dataset
Synthetic dataset with:
- 40 rows for **Control Group**
- 40 rows for **Test Group**
- Columns: `Impression`, `Click`, `Purchase`, `Earning`, `Group`

File: `ab_testing_simple.csv`

## 🧠 Methodology
1. **Normality Check** → Shapiro–Wilk test  
2. **Variance Check** → Levene’s test  
3. **A/B Hypothesis Test** → Independent Two-Sample t-test  

**Hypotheses:**
- H₀: No difference between Control and Test mean purchases  
- H₁: There is a difference between Control and Test mean purchases  

## 🧩 Libraries Used
`pandas`, `scipy.stats`, `matplotlib`, `numpy`

## 🧾 Results
| Group | Mean Purchase |
|--------|----------------|
| Control | (≈550) |
| Test | (≈580) |

**p-value = 0.34 > 0.05**  
→ No statistically significant difference.  

**Conclusion:** The new bidding method does not significantly improve purchases.

## 📈 Visualization
A bar chart comparing mean purchases is saved as `ab_result.png`.

## 💻 How to Run
1. Clone or download this repository  
2. Install requirements:  
   ```bash
   pip install pandas scipy matplotlib
