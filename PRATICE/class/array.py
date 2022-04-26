"""
@author: Ganesh Jadhawar
@goal: To implement array in which we can replace the elements.
"""


class array:
    def __init__(self, init_size):
        internal_list = []
        for i in range(init_size):
            internal_list.append(0)

