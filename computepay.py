def computepay(h,r):
    if h <= 40:
        return (r * h)
    elif h > 40:
    	return ((r * 40)+((h-40)*(r*1.5)))
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h,r)
print("Pay:",p)
