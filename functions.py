def computepay(h, r):
    if h > 40:
        regpay = h * r
        adjrate = (h - 40.0) * (r * 0.5)
        expay = regpay + adjrate
        return expay
    else:
        expay = h * r
        return expay


hrs = input("Enter Hours:")
fh = float(hrs)
rate = input("Enter Rate:")
fr = float(rate)
x = computepay(fh, fr)
print("Pay", x)
