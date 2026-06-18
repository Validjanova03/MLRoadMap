# Linear Regression

> One of the simplest ML algorithms — predict a continuous value using a straight line.

---

## What it's used for

Anytime the output is a **number**, not a category.

| Example | Input (x) | Output (y) |
|---------|-----------|------------|
| House price | Size (m²) | Price ($) |
| Salary | Years of experience | Annual salary ($) |
| Rent | Location score | Monthly rent ($) |
| Temperature | Month | Degrees (°C) |

---

## Core Formula

$$y = wx + b$$

| Symbol | Name | Meaning |
|--------|------|---------|
| `y` | Prediction | The value we want to predict |
| `x` | Input feature | The data we feed in |
| `w` | Weight (slope) | How much `y` changes when `x` increases by 1 |
| `b` | Bias (intercept) | Starting value when `x = 0` |

---

## How to remember w and b 

Think of a **taxi fare**:

```
Price = 2 × Distance + 5
```

- `w = 2` → every extra kilometer costs **$2 more**
- `b = 5` → there's always a **$5 starting fee**, even at 0 km

### The rule

| | |
|-|-|
| `w` | **Growth rate** — how fast y rises |
| `b` | **Starting value** — where y begins |

---

## Goal of Linear Regression

> Find the best values of `w` and `b` so predictions are as accurate as possible.

---

## Making a Prediction

Given `y = 7x + 3`, predict when `x = 10`:

```
y = 7(10) + 3 = 73
```

**Prediction = 73**

---

## Error

> How wrong is the prediction?

```
Error = Actual − Predicted
```

**Example:** Actual = 70, Predicted = 65 → Error = **5**

---

## Cost Function — MSE

We need **one number** to answer: *"How bad is the model overall?"*

For Linear Regression that number is **Mean Squared Error (MSE)**:

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

**Steps:**

1. Calculate each error
2. Square it (removes negatives, punishes big mistakes more)
3. Average them all

**Example:**

| Error | Squared |
|-------|---------|
| 5 | 25 |
| −2 | 4 |
| −2 | 4 |
| **Sum** | **33** |

$$MSE = \frac{33}{3} = 11$$

---

## Training — How the Model Learns

**Goal:** find `w` and `b` that minimize MSE — the line that makes the smallest mistakes.

**Algorithm: Gradient Descent**

```
1. Start with random w and b
2. Calculate the error (MSE)
3. Adjust w and b slightly in the right direction
4. Repeat until error is very small
```

Think of it as walking downhill — each step brings you closer to the lowest point (lowest MSE).

---

## Measuring Quality — R²

> How well does the line fit the data?

| R² value | Meaning |
|----------|---------|
| 1.0 | Perfect fit |
| 0.8+ | Good model |
| 0.5 | Weak model |
| 0 or below | Model is useless |
