"""
@author: Ganesh Jadhawar
@goal: to implement class in python
"""

import sys


class Book:
    def __init__(self, book_object_dict):
        list_of_attr = ['bk_title', 'bk_authors', 'bk_publisher',
                        'bk_genre', 'bk_nr_pages']
        for attr_name in list_of_attr:
            if attr_name in list(book_object_dict.keys()):
                pass
            else:
                print("wrong dict key")
                sys.exit(-1)
        self.__dict__ = book_object_dict


B = Book({'bk_title' : 'Introduction to Algorithms', 'bk_authors' : 'Cormen', 'bk_publisher': 'MIT Press', 'bk_genre': 'Algorithms', 'bk_nr_pages' : 1292})

print(B.__dict__)