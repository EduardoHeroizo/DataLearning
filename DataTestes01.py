import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2)

ax[0].plot([1, 2, 3])
ax[1].plot([3, 2, 1])

plt.show()