import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.DataFrame({
    'Текущее время (мин)': np.arange(0, 37)
})


D2_constant = 12


data['Остаток'] = data['Текущее время (мин)'] % D2_constant


data['Скорость введения'] = np.where(data['Остаток'] < 5, 100, 0)


data['Период введения'] = D2_constant

plt.figure(figsize=(10, 6))
plt.scatter(data['Текущее время (мин)'], data['Скорость введения'], color='blue', label='Скорость введения')

plt.title('Точечная диаграмма скорости введения')
plt.xlabel('Текущее время (мин)')
plt.ylabel('Скорость введения')
plt.grid(True)
plt.legend()
plt.show()


file_path = '/mnt/data/infusion_speed_table.xlsx'
data.to_excel(file_path, index=False)

file_path