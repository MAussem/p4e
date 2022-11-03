hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h > 40:
    regpay = h * r
    adjrate = (h - 40.0) * (r * 0.5)
    expay = regpay + adjrate
else:
    expay = h * r
print(expay)
