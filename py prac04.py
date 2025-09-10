temp=int(input("Enter temperature in celsius:"))
if temp<=0:
    print("Freezing")
elif temp>0 and temp<=15:
    print("Cold")
elif temp>15 and temp<=30:
    print("Warm")
elif temp>30:
    print("Hot")
else:
    print("No Message")
