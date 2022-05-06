# Conditional Execution

hrs = float(input("Enter Hours:"))
rate_per_hour = float(input("Enter rate per hour: "))

if hrs > 40:
    gross_pay = ((40 * rate_per_hour) + ((hrs - 40) * (rate_per_hour * 1.5)))
    print(gross_pay)
else:
    gross_pay = hrs * rate_per_hour
    print(gross_pay)