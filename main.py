# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from collision import Collision
import numpy as np
import matplotlib.pyplot as plt


triangle = Collision(np.array([0, 1, 0]), np.array([1, 2, 3]), 0.14)
a, b = triangle.move_tip(np.array([[1, 0], [2.4, -1], [2.5, 0.5]]))

fig = plt.figure()
ax = fig.subplots()
triangle.draw_landscape(ax)
ax.plot(a, b)
plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
