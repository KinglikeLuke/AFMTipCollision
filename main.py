# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from collision import Collision
import numpy as np
import matplotlib.pyplot as plt

random_surface = Collision(np.random.normal(1, 5, 100), np.logspace(0.1, 1, 100), 0.01)
x_movement, y_movement, animation, ax = random_surface.move_tip(np.array([[1, 0], [1.1, -1], [1.2, -1], [1.4, 0]]),
                                                                do_animation=True)
plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
