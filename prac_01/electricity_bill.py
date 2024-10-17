"""
Electricity bill estimator
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_choice = int(input("Which tariff? 11 or 31: "))
if tariff_choice == 11:
    cents_per_kwh = TARIFF_11
else:
    cents_per_kwh = TARIFF_31
daily_use_kwh = float(input("Enter daily use kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
estimated_bill = cents_per_kwh * daily_use_kwh * number_of_billing_days
print(f"Estimated bill: ${estimated_bill:.2f}")
