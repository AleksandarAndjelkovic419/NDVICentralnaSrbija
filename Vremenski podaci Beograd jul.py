import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import csv


# Ubacivanje vremenskih podataka iz CSV fajla
csv_file = "./Belgrade Serbia 2021-07-01 to 2021-07-31.csv"

# Initialize an empty list to hold the data
data_list = []

# Open and read the CSV file
with open(csv_file, "r") as file:
    reader = csv.reader(file)

    # Read the header (first row)
    header = next(reader)

    # Read the remaining rows and store them as a list
    for row in reader:
        # Convert each row to a list of floats (or you can adjust as needed)
        data_list.append(row)

# Convert the list to a NumPy array
data = np.array(data_list)


def to_float_array(data: np.array):
    return [float(d) for d in data]


# Vadjenje datuma, temperature, vlaznosti i padavina iz fajla
datetime_str = data[:, 1]  #                   "datetime"
temperature = to_float_array(data[:, 3])  #    "temperature"
humidity = to_float_array(data[:, 9])  #       "humidity"
precipitation = to_float_array(data[:, 10])  # "precipitation"

# Pretvaranje datuma u stringove
datetime_obj = [datetime.strptime(date, "%Y-%m-%d") for date in datetime_str]

# Prikazivanje temperature tokom vremena
plt.figure(figsize=(10, 5))
plt.plot(
    datetime_obj,
    temperature,
    marker="o",
    linestyle="-",
    label="Temperature (in Celsius)",
)
plt.title("Temperature over time")
plt.xlabel("Datetime")
plt.ylabel("Temperature (in Celsius)")
plt.grid(True)
plt.legend()
plt.show()

# Prikazivanje vlaznosti tokom vremena
plt.figure(figsize=(10, 5))
plt.plot(
    datetime_obj, humidity, marker="o", linestyle="-", color="b", label="Humidity (%)"
)
plt.title("Humidity over time")
plt.xlabel("Datetime")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.legend()
plt.show()

# Prikazivanje padavina tokom vremena
plt.figure(figsize=(10, 5))
plt.plot(
    datetime_obj,
    precipitation,
    marker="o",
    linestyle="-",
    color="g",
    label="Precipitation (mm)",
)
plt.title("Precipitation over time")
plt.xlabel("Datetime")
plt.ylabel("Precipitation (mm)")
plt.grid(True)
plt.legend()
plt.show()

# Sumiranje statistike
print("Summary statistics:")
print(
    f"Temperature: Mean={np.mean(temperature):.2f} in Celsius, Std={np.std(temperature):.2f} in Celsius"
)
print(f"Humidity: Mean={np.mean(humidity):.2f}%, Std={np.std(humidity):.2f}%")
print(f"Precipitation: Total={np.sum(precipitation):.2f} mm")
