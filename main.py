import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

# Функция для расчета кинетической, потенциальной и полной энергии
def calculate_energies(mass, stiffness, damping, initial_displacement, initial_velocity, time_steps=1000, dt=0.01):
    # Начальные параметры
    x = initial_displacement  # Начальное смещение
    v = initial_velocity      # Начальная скорость
    t = 0.0                   # Начальное время

    times = []
    kinetic_energies = []
    potential_energies = []
    total_energies = []

    for _ in range(time_steps):
        # Расчет сил и ускорений
        spring_force = -stiffness * x
        damping_force = -damping * v
        net_force = spring_force + damping_force
        a = net_force / mass

        # Обновление скорости и положения
        v += a * dt
        x += v * dt

        # Обновление времени
        t += dt

        # Энергетические расчеты
        kinetic_energy = 0.5 * mass * v**2
        potential_energy = 0.5 * stiffness * x**2
        total_energy = kinetic_energy + potential_energy

        # Запись данных для графика
        times.append(t)
        kinetic_energies.append(kinetic_energy)
        potential_energies.append(potential_energy)
        total_energies.append(total_energy)

    return times, kinetic_energies, potential_energies, total_energies

# Функция для отображения графиков
def plot_energies(mass, stiffness, damping, initial_displacement, initial_velocity):
    times, kinetic_energies, potential_energies, total_energies = calculate_energies(
        mass, stiffness, damping, initial_displacement, initial_velocity
    )

    plt.figure(figsize=(10, 6))
    plt.plot(times, kinetic_energies, label='Кинетическая энергия', color='blue')
    plt.plot(times, potential_energies, label='Потенциальная энергия', color='red')
    plt.plot(times, total_energies, label='Полная механическая энергия', color='green')

    plt.xlabel('Время (с)')
    plt.ylabel('Энергия (Дж)')
    plt.title('Энергетические превращения при колебаниях')
    plt.legend()
    plt.grid(True)
    plt.show()

# Функция, вызываемая при нажатии кнопки
def on_calculate():
    try:
        mass = float(mass_entry.get())
        stiffness = float(stiffness_entry.get())
        damping = float(damping_entry.get())
        initial_displacement = float(displacement_entry.get())
        initial_velocity = float(velocity_entry.get())
        plot_energies(mass, stiffness, damping, initial_displacement, initial_velocity)
    except ValueError:
        result_label.config(text="Ошибка: введите числовые значения.")

# Создание интерфейса
root = tk.Tk()
root.title("Энергетические превращения при колебаниях")

# Поле для ввода массы
mass_label = ttk.Label(root, text="Масса груза (кг):")
mass_label.grid(row=0, column=0, padx=10, pady=5)
mass_entry = ttk.Entry(root)
mass_entry.grid(row=0, column=1, padx=10, pady=5)

# Поле для ввода коэффициента жесткости
stiffness_label = ttk.Label(root, text="Коэффициент жесткости (Н/м):")
stiffness_label.grid(row=1, column=0, padx=10, pady=5)
stiffness_entry = ttk.Entry(root)
stiffness_entry.grid(row=1, column=1, padx=10, pady=5)

# Поле для ввода коэффициента сопротивления
damping_label = ttk.Label(root, text="Коэффициент сопротивления (кг/с):")
damping_label.grid(row=2, column=0, padx=10, pady=5)
damping_entry = ttk.Entry(root)
damping_entry.grid(row=2, column=1, padx=10, pady=5)

# Поле для ввода начального смещения
displacement_label = ttk.Label(root, text="Начальное смещение (м):")
displacement_label.grid(row=3, column=0, padx=10, pady=5)
displacement_entry = ttk.Entry(root)
displacement_entry.grid(row=3, column=1, padx=10, pady=5)

# Поле для ввода начальной скорости
velocity_label = ttk.Label(root, text="Начальная скорость (м/с):")
velocity_label.grid(row=4, column=0, padx=10, pady=5)
velocity_entry = ttk.Entry(root)
velocity_entry.grid(row=4, column=1, padx=10, pady=5)

# Кнопка для расчета
calculate_button = ttk.Button(root, text="Рассчитать", command=on_calculate)
calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Метка для вывода результата
result_label = ttk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
