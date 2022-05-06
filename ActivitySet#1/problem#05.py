#Functions

def computepay(hrs, rate_per_hour):
    if hrs > 40:
        return ((40 * rate_per_hour) + ((hrs - 40) * (rate_per_hour * 1.5)))
    else:
        return hrs * rate_per_hour
    

hrs = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
print("Pay", computepay(hrs, rate_per_hour))