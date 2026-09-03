# Linear Regression from Scratch

A learning project where I explored how linear regression works under the hood — without using sklearn's ready-made `LinearRegression`.

## What I learned

- **Closed-form solution (Normal Equation)** — implemented linear regression using the formula `(XᵀX)⁻¹ Xᵀy`. Learned how the bias column of ones is added for the intercept and how to extract the coefficients and intercept from the resulting vector.
- **Gradient Descent** — implemented training via gradient descent: weight initialization, computing predictions, the gradient, and updating weights with a learning rate over epochs.
- Working with matrices in **NumPy** (`@`, `np.c_`, `.T`, `np.linalg.inv`).
- Evaluating model quality with **R²** (`r2_score`).

## Files

- `closed-formula-solution.py` — linear regression via the Normal Equation on the California Housing dataset.
- `gradient Descent-solution.py` — same idea, but trained with gradient descent on `data/dataset.csv`.
- `data/dataset.csv` — practice dataset (studytime, attendance, age → score).

## Run

```bash
python closed-formula-solution.py
python "gradient Descent-solution.py"
```
