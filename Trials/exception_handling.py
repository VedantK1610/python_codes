x=int(input("num1"))
y=int(input("num2"))

try:
    z=x/y
except Exception as e:
    print("Error:",e)
    z=None
print(z)
