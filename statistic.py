import statistics
import matplotlib.pyplot as plt

data_set = [364, 373, 358, 394, 378, 379, 357, 364, 350, 363, 392, 368, 359, 375, 399, 365, 379, 357, 380]

# Середнє значення (mean)
mean = statistics.mean(data_set)

# Медіана (median)
median = statistics.median(data_set)

# Мода (mode)
mode = statistics.mode(data_set)

# Стандартне відхилення (standard deviation)
std_dev = statistics.stdev(data_set)

print(f"Среднє значення: {mean}")
print(f"Медіана: {median}")
print(f"Мода: {mode}")
print(f"Стандартне відхилення: {std_dev}")

plt.figure(figsize=(8, 6))
plt.plot(data_set, marker='o', linestyle='-', label='Данні')
plt.axhline(mean, color='red', linestyle='--', label=f'Середнє: {mean:.2f}')
plt.axhline(median, color='green', linestyle='-.', label=f'Медіана: {median}')
plt.axhline(mode, color='blue', linestyle=':', label=f'Мода: {mode}')
plt.axhline(mean + std_dev, color='purple', linestyle=':', label=f'+ Стандартне відхилення')
plt.axhline(mean - std_dev, color='purple', linestyle=':', label=f'- Стандартне відхилення')


plt.xlabel('Індекс')
plt.ylabel('Значення')
plt.title('Характеристики набору данних')
plt.legend()

plt.show()