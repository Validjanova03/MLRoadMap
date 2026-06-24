# Decision Tree

> A decision tree is just a game of 20 Questions. Every split is a Yes/No question. It keeps asking until each group is pure.

---

## Mental model

Every split = one yes/no question about the data.
The tree keeps asking questions, going deeper, until each group contains only one class — that group is **pure**.

Purity is measured with **Gini Impurity** or **Entropy**.

---

## Key terms

| Term | Meaning |
|------|---------|
| **Root node** | The very first split |
| **Internal node** | Any split in the middle |
| **Leaf node** | Final answer — no more splits |
| **Pure node** | All one class (all Yes or all No) |
| **Depth** | How many splits deep you go |
| **Maximum depth** | Maximum number of branches between the top and the bottom |
| **Branch / subtree** | A subsection of the entire tree |

---

## When to stop splitting?

| Variable type | Method |
|---------------|--------|
| Categorical | Entropy + Information Gain (IG) |
| Continuous | Reduction in variance |

> **Rule:** always aim for low impurity → Gini = 0.00

---

## Gini impurity

> **Question it asks:** "If I randomly pick 2 candies from this bowl, what is the chance they are different colours?"

| Result | Meaning |
|--------|---------|
| High chance of different | Messy → High Gini |
| Low chance of different | Organised → Low Gini |

### Formula

```
Gini = 1 − (p_red² + p_blue²)
```

### Example — 3 red, 1 blue (4 total)

```
p_red  = 3/4 = 0.75
p_blue = 1/4 = 0.25

Gini = 1 − (0.75² + 0.25²)
     = 1 − (0.5625 + 0.0625)
     = 1 − 0.625
     = 0.375
```

**0.375 → moderately impure.** Not terrible, but not clean either.
A decision tree would continue splitting.

---

## Entropy

Measures how *surprised* you'd be picking a random candy — pure bowl = never surprised, 50/50 = always surprised.

```
Entropy = −(p_red × log₂(p_red)) − (p_blue × log₂(p_blue))
```

| Bowl | Entropy | Verdict |
|------|---------|---------|
| All red (pure) | 0.00 | Perfect |
| 50/50 split | 1.00 | Worst possible |
| 3 red, 1 blue | 0.81 | Still not good |

---

## Information Gain (IG)

> **Question it asks:** "How much did this split clean up the mess?"

Before the split → one messy bowl.
After the split → two smaller bowls.
If the two smaller bowls are cleaner than the original → the split was useful.

### Formula

```
IG = Gini(before) − Weighted_Average_Gini(after)
```

| IG value | Meaning |
|----------|---------|
| High | Split cleaned up a lot → good split |
| Low | Split barely helped → bad split |

---

### Worked example

**Dataset: 10 samples — 6 Red, 4 Blue**

**Step 1 — Parent Gini (before split)**

```
p_red  = 6/10 = 0.6
p_blue = 4/10 = 0.4

Gini(parent) = 1 − (0.6² + 0.4²)
             = 1 − (0.36 + 0.16)
             = 0.48
```

**Step 2 — Split into 2 child nodes**

```
Child A → 4 Red, 1 Blue (5 total)
Gini(A) = 1 − ((4/5)² + (1/5)²)
        = 1 − (0.64 + 0.04)
        = 0.32

Child B → 2 Red, 3 Blue (5 total)
Gini(B) = 1 − ((2/5)² + (3/5)²)
        = 1 − (0.16 + 0.36)
        = 0.48
```

**Step 3 — Weighted average Gini (after split)**

```
Weighted Gini = (5/10 × 0.32) + (5/10 × 0.48)
              = 0.16 + 0.24
              = 0.40
```

**Step 4 — Information Gain**

```
IG = 0.48 − 0.40 = 0.08
```

> **Verdict:** reduced impurity a little, but not dramatically.
> We need a higher IG — try a different split.
