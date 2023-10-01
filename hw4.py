def correlation_of_pearson(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(x_i ** 2 for x_i in x)
    sum_y_squared = sum(y_i ** 2 for y_i in y)
    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2)) ** 0.5
    if denominator == 0:
        return 0
    correlation = numerator / denominator
    return correlation
array1 = [8, -9, 4, 6, 2]
array2 = [3, 7, 1, 0, 9]
print(f"Коэффициент корреляции Пирсона: {correlation_of_pearson(array1, array2)}")

import numpy as np
x = np.array([8, -9, 4, 6, 2])
y= np.array([3, 7, 1, 0, 9])
corr = np.corrcoef(x, y)[0,1]

print(f"Коэффициент корреляции Пирсона: {corr}")
