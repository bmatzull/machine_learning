## 1.

Bayes' theorem:
```
P(h | D) = P(D | h) * P(h) / P(D)
```

MAP maximizes the posterior. Since P(D) does not depend on h, it can be dropped:
```
h_MAP = argmax_h  P(D | h) * P(h)
```

Taking the negative log2:
```
-log2[ P(D|h) * P(h) ] = -log2 P(D|h) - log2 P(h) = L(D|h) + L(h)
```

Therefore:
```
h_MAP = argmin_h  L(h) + L(D|h)
```

Minimizing the total description length is equivalent to MAP estimation.
- `L(h)` = cost of encoding the hypothesis (penalizes unlikely/complex hypotheses)
- `L(D|h)` = cost of encoding the data given the hypothesis (penalizes poor fit)

---

## 2.

`L(h) = -log2 P(h)` is small when P(h) is large, i.e. when the hypothesis is simple/common.
A complex hypothesis needs more bits to describe → higher L(h).

MDL therefore formalizes Occam's Razor: among hypotheses that explain the data well,
prefer the simplest one. The total cost L(h) + L(D|h) forces a trade-off — you cannot
just pick the most complex model that fits perfectly, because its L(h) penalty will be too high.

