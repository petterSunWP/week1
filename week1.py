import numpy as np
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

average_temp = temperatures.mean()
print(f"Average temperature: {average_temp:.2f}°C")

highest = temperatures.max()
lowest = temperatures.min()
print(f"Highest temperature: {highest}°C")
print(f"Lowest temperature: {lowest}°C")

fahrenheit = temperatures * 9/5 + 32
print("Temperatures in Fahrenheit:", fahrenheit)

hot_days = np.where(temperatures > 20)[0]
print("Days with temperature > 20°C (indices):", hot_days)