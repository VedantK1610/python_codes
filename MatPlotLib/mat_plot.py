import matplotlib.pyplot as plt

x=[20,21,22,23]
y=[15000,20000,22000,27000]
z=[10000,21000,15000,25500]

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Avg Salary Graph")

plt.plot(x,y,'g',label='salary')
plt.plot(x,z,'b',label='bonus')
plt.legend()
plt.show()

