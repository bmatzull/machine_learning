# Task 2: ROC Curve

## Data

| Class | Prediction |
|-------|------------|
| N     | 0.85       |
| N     | 0.51       |
| P     | 0.66       |
| N     | 0.55       |
| P     | 0.40       |
| N     | 0.60       |
| P     | 0.55       |
| P     | 0.78       |
| N     | 0.52       |
| P     | 0.95       |

Total: 5 positives (P), 5 negatives (N)

---

## ROC Curve Calculation

Sort all instances by prediction score in descending order, then sweep the threshold from high to low. At each step, compute:

- **TPR** (True Positive Rate) = TP / total positives = TP / 5  
- **FPR** (False Positive Rate) = FP / total negatives = FP / 5

| Threshold | Class | TP | FP | TPR  | FPR   |
|-----------|-------|----|----|------|-------|
| 0.95      | P     | 1  | 0  | 0.20 | 0.00  |
| 0.85      | N     | 1  | 1  | 0.20 | 0.20  |
| 0.78      | P     | 2  | 1  | 0.40 | 0.20  |
| 0.66      | P     | 3  | 1  | 0.60 | 0.20  |
| 0.60      | N     | 3  | 2  | 0.60 | 0.40  |
| 0.55      | N     | 3  | 3  | 0.60 | 0.60  |
| 0.55      | P     | 4  | 3  | 0.80 | 0.60  |
| 0.52      | N     | 4  | 4  | 0.80 | 0.80  |
| 0.51      | N     | 4  | 5  | 0.80 | 1.00  |
| 0.40      | P     | 5  | 5  | 1.00 | 1.00  |

ROC curve points (FPR, TPR):  
`(0.0, 0.0) → (0.0, 0.2) → (0.2, 0.2) → (0.2, 0.6) → (0.4, 0.6) → (0.6, 0.6) → (0.6, 0.8) → (0.8, 0.8) → (1.0, 0.8) → (1.0, 1.0)`

---

## AUC Calculation

Using the trapezoidal rule over the ROC points:

| Segment         | Width (ΔFPR) | Avg Height (TPR) | Area   |
|-----------------|--------------|------------------|--------|
| 0.0 → 0.0       | 0.0          | 0.10             | 0.000  |
| 0.0 → 0.2       | 0.2          | 0.20             | 0.040  |
| 0.2 → 0.2       | 0.0          | 0.40             | 0.000  |
| 0.2 → 0.4       | 0.2          | 0.60             | 0.120  |
| 0.4 → 0.6       | 0.2          | 0.60             | 0.120  |
| 0.6 → 0.6       | 0.0          | 0.70             | 0.000  |
| 0.6 → 0.8       | 0.2          | 0.80             | 0.160  |
| 0.8 → 1.0       | 0.2          | 0.80             | 0.160  |
| 1.0 → 1.0       | 0.0          | 0.90             | 0.000  |

**AUC = 0.04 + 0.12 + 0.12 + 0.16 + 0.16 = 0.68**

---

## Evaluation

**Is the classifier good?**

With an AUC of **0.68**, the classifier performs *moderately* better than a random classifier (AUC = 0.50), but is not strong. Key observations:

- The ROC curve bows above the diagonal, confirming the classifier has real predictive power.
- However, the first false positive occurs early: the instance with the highest score (0.85) is actually a negative. This hurts early-stage precision.
- An AUC of 0.68 is generally considered **"fair"** — usable as a baseline, but a well-performing classifier typically achieves AUC ≥ 0.80.

**Conclusion:** The classifier is better than random but not yet reliable enough for high-stakes applications.