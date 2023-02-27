# Take the input marks and convert it to integer
marks = int(input("Enter the marks: "))


# Condition checking 
if marks < 40:
    print("F")
elif marks < 50:
    print("E")
elif marks < 60:
    print("D")
elif marks < 70:
    print("C")
elif marks < 80:
    print("B")
elif marks < 90:
    print("A")
else:
    print("A+")
    