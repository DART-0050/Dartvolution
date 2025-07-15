# Understanding the Chain Rule (StatQuest)

<https://www.youtube.com/watch?v=wl1myxrtQHQ&list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1&index=3>

## Goal

- To clearly understand the **chain rule**, a fundamental concept in calculus and backpropagation.

---

## Chain Rule Concept – Simple Example

- Predicting Shoe Size from Weight:
  - Weight → Height (slope = 2)
  - Height → Shoe Size (slope = 0.25)
  - Overall change:  
    `d(shoe size)/d(weight) = (ds/dh) × (dh/dw) = 0.25 × 2 = 0.5`

---

## Chain Rule with Nonlinear Functions

- Time Since Last Snack → Hunger (quadratic)
- Hunger → Ice Cream Craving (square root)
- Chain Rule lets us compute:  
  `d(craving)/d(time) = (d(craving)/d(hunger)) × (d(hunger)/d(time))`

---

## Nested Functions (Stuff Inside Trick)

- Craving = √(time² + ½)  
- Let `stuff = time² + ½`  
- Apply chain rule:  
  `d(craving)/d(time) = d(craving)/d(stuff) × d(stuff)/d(time)`

---

## Application in Machine Learning – Loss Function

### Residual Sum of Squares (RSS)

- Residual = Observed − Predicted
- Predicted = Intercept + (1 × weight)

### Chain Rule on RSS

- `d(RSS)/d(intercept) = d(RSS)/d(residual) × d(residual)/d(intercept)`
- First derivative: `2 × residual`
- Second derivative: `-1` (from residual expression)

---

## Solving for Best Fit (Minimizing Loss)

- Plug values into the derivative of RSS  
- Set derivative = 0  
- Solve for intercept → gives best-fitting line

---

## Summary

- Chain rule links changes in input to output through intermediate variables.
- Vital for **gradient-based learning** in neural networks.
- Lets us **break down complex derivatives** step-by-step.
