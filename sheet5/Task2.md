# Sheet 5 – Task 2: Bayesian Networks

## Variables
- **B** = Burglary
- **E** = Earthquake
- **A** = Alarm fires
- **C** = Call from neighbor

---

## Part 1: Bayesian Belief Network

```
B (Burglary)        E (Earthquake)
      \                 /
       \               /
        v             v
          A (Alarm)
              |
              v
          C (Call)
```

B and E are independent root causes. Both cause A. 
A is the sole cause of C.

---

## Part 2: Probabilities from the Story

| Probability | Value |
|---|---|
| P(B=1) | 1/1000 |
| P(E=1) | 2/1000 |
| P(A=1 \| B=0, E=0) | 1/1000 |
| P(A=1 \| B=0, E=1) | 20/100 |
| P(A=1 \| B=1, E=0) | 94/100 |
| P(A=1 \| B=1, E=1) | 99/100 |
| P(C=1 \| A=1) | 9/10 |
| P(C=1 \| A=0) | 0 |

---

## Part 3: CPT for A

| B | E | P(A=1) | P(A=0) |
|---|---|---|---|
| 0 | 0 | 0.001 | 0.999 |
| 0 | 1 | 0.20 | 0.80 |
| 1 | 0 | 0.94 | 0.06 |
| 1 | 1 | 0.99 | 0.01 |

---

## Part 4: Inference

### With earthquake known: P(B=1 | A=1, E=1)

C is conditionally independent of B and E given A, 
so it drops out:

```
P(B=1 | A=1, E=1, C=1) = P(B=1 | A=1, E=1)
```

Bayes' theorem:
```
P(B=1 | A=1, E=1) = P(A=1 | B=1, E=1) * P(B=1) / P(A=1 | E=1)
```

Law of total probability for the denominator:
```
P(A=1 | E=1) = P(A=1|B=1,E=1)*P(B=1) + P(A=1|B=0,E=1)*P(B=0)
             = (99/100)*(1/1000) + (20/100)*(999/1000)
             = 99/100000 + 19980/100000
             = 20079/100000 ≈ 0.20079
```

Result:
```
P(B=1 | A=1, E=1) = (99/100 * 1/1000) / (20079/100000)
                  = 99 / 20079 ≈ 0.0049 ≈ 0.49%
```

---

### Without earthquake known: P(B=1 | A=1)

```
P(B=1 | A=1) = P(A=1 | B=1) * P(B=1) / P(A=1)
```

First, P(A=1 | B=1) over E:
```
P(A=1|B=1) = (99/100)*(2/1000) + (94/100)*(998/1000)
           = 198/100000 + 93812/100000 ≈ 0.9401
```

Then, P(A=1) over all B and E:
```
= (99/100)*(1/1000)*(2/1000)    →   1.98e-6
+ (94/100)*(1/1000)*(998/1000)  → 938.12e-6
+ (20/100)*(999/1000)*(2/1000)  → 399.60e-6
+ (1/1000)*(999/1000)*(998/1000)→ 997.00e-6
                          Total ≈ 0.002337
```

Result:
```
P(B=1 | A=1) = 0.9401 * 0.001 / 0.002337 ≈ 0.402 ≈ 40.2%
```

---

## Summary

| Scenario | P(B=1) |
|---|---|
| Prior (no info) | 0.1% |
| Alarm fired, earthquake unknown | **40.2%** |
| Alarm fired, earthquake known | **0.49%** |

