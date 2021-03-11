import numpy as np
import matplotlib.pyplot as plt

FILENAME = ""
data = np.transpose(np.genfromtxt(FILENAME))

plt.grid()
plt.plot(data[0], data[1], 'bo-')
plt.xlabel('time (s)')
plt.ylabel('position (m)')
plt.show()
