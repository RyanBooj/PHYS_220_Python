import numpy as np
import matplotlib.pyplot as plt

# testArray = np.array([[5, 3, 8, 1, 4], [3, 2, 8, 13, 4]])
# print(testArray)
#
# testArrayZero = np.zeros((4, 3))
# print(testArrayZero)
#
# # Write to a file
# arrayRandom = np.random.random((3, 2))
# np.savetxt('aTest.txt', arrayRandom, fmt='%.4f')
#
# arrayRead = np.loadtxt('aTest.txt')
# print(arrayRead)

x = np.linspace(0.01,np.pi*2, 10)
print(x)
y1 = np.sin(x)
y2 = np.cos(x)
yerror = 0.3*y1

#Plot without error bars
plt.figure()
plt.plot(x, y1, color='r', lineStyle='none', marker = 'o', markerSize = 12)

plt.plot(x, y2, linewidth=4)
plt.title("Sine and Cosine Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()