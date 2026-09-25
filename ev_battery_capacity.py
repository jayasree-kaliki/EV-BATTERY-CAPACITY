# EV Battery Capacity Calculator
# Calculates the required battery capacity for an Electric Vehicle

print("====================================")
print("     EV BATTERY CAPACITY CALCULATOR")
print("====================================")

# User inputs
energy_consumption = float(input("Enter energy consumption (Wh/km): "))
range_km = float(input("Enter desired driving range (km): "))
battery_efficiency = float(input("Enter battery efficiency (%): "))
depth_of_discharge = float(input("Enter allowable depth of discharge (%): "))

# Convert percentages to decimal
efficiency = battery_efficiency / 100
dod = depth_of_discharge / 100

# Calculate energy required by vehicle
energy_required = energy_consumption * range_km

# Calculate battery capacity
battery_capacity_wh = energy_required / (efficiency * dod)

# Convert Wh to kWh
battery_capacity_kwh = battery_capacity_wh / 1000

# Display results
print("\n----------- RESULTS -----------")
print(f"Energy required by vehicle : {energy_required:.2f} Wh")
print(f"Required battery capacity  : {battery_capacity_kwh:.2f} kWh")
print("--------------------------------")
