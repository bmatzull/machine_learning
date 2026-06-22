Closed-form OLS solution: `w = (X^T X)^-1 X^T y`

---

## Without Intercept => y_hat = w1*x1 + w2*x2

```
X^T X = [[66, 79],    X^T y = [[275],
          [79, 126]]             [417]]
```

```
w = [0.8227, 2.7937]
```

Predictions and residuals:

| i | y  | y_hat   | residual |
|---|----|---------|----------|
| 1 | 6  | 6.4101  | -0.4101  |
| 2 | 11 | 12.4945 | -1.4945  |
| 3 | 20 | 21.2014 | -1.2014  |
| 4 | 29 | 27.2858 |  1.7142  |

```
SSE = 6.7836
MSE = 1.6959
```

---

## With Intercept => y_hat = w0 + w1*x1 + w2*x2

=> prepend a column of ones to X.

```
X_int^T X_int = [[ 4, 14, 20],    X_int^T y = [[ 66],
                 [14, 66, 79],                  [275],
                 [20, 79, 126]]                 [417]]
```

```
w = [-2, 1, 3]   →   y_hat = -2 + 1*x1 + 3*x2
```

Predictions and residuals:

| i | y  | y_hat | residual |
|---|----|-------|----------|
| 1 | 6  | 5     | +1       |
| 2 | 11 | 12    | -1       |
| 3 | 20 | 21    | -1       |
| 4 | 29 | 28    | +1       |

```
SSE = 4.0
MSE = 1.0
```

---

## Part 3: Comparison

| Model           | MSE |
|-----------------|-----|
| Without intercept | 1.6959 |
| With intercept  | 1.0 |

The model **with intercept fits better** (lower MSE).

The no-intercept model is forced through the origin, which is an unnecessary constraint here.
Adding w0 gives the model one extra degree of freedom to shift the plane, reducing the error.
