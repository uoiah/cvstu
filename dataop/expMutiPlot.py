import matplotlib
# matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt
import pandas

fig = plt.figure(figsize=(8, 6))

ax1 = plt.subplot(3,1,1)
ax1.set_title('sin')
x = np.linspace(-1,2,50)
y = np.sin(x)
plt.plot(x, y, label='sin')

ax2 = plt.subplot(334)
ax2.set_title("ax2 title")
 
ax3 = plt.subplot(335)
ax4 = plt.subplot(336)
ax5 = plt.subplot(325)
ax6 = plt.subplot(326)

# fig.savefig("multi_curve_tmp.png")
plt.show()
