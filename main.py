# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from collision import Collision
import numpy as np

Collision(np.array([0,1,0]), np.array([1,2,3]), 0.5)
a = Collision.move_tip(np.array([[1,0], [2,-1], [2.5, 0.5]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
