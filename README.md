# Linear Regression from Scratch

Мой учебный проект, где я разбирался, как работает линейная регрессия изнутри — без использования готового `LinearRegression` из sklearn.

## Что я изучил

- **Closed-form solution (нормальное уравнение)** — реализовал линейную регрессию через формулу `(XᵀX)⁻¹ Xᵀy`. Понял, как добавляется столбец единиц для intercept и как из полученного вектора вытащить коэффициенты и свободный член.
- **Gradient Descent** — реализовал обучение методом градиентного спуска: инициализация весов, вычисление предсказаний, градиента и обновление весов с learning rate по эпохам.
- Работа с матрицами в **NumPy** (`@`, `np.c_`, `.T`, `np.linalg.inv`).
- Оценка качества модели через **R²** (`r2_score`).

## Файлы

- `closed-formula-solution.py` — линейная регрессия через нормальное уравнение на датасете California Housing.
- `gradient Descent-solution.py` — та же идея, но обучение через градиентный спуск на `data/dataset.csv`.
- `data/dataset.csv` — учебный датасет (studytime, attendance, age → score).

## Запуск

```bash
python closed-formula-solution.py
python "gradient Descent-solution.py"
```
