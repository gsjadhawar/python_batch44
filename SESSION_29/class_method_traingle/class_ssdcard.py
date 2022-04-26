"""
@author: Ganesh Jadhawar
@goals: to pratice writing class constructor
"""
import sys


class dimensions():
    def __init__(self, length: int, width: int, height: int):
        """
        :param length: length of product
        :param width: width of product
        :param height: height of product
        """
        if type(length) != int and type(length) != float:
            print("actual parameter passed are of invalid data type")
            sys.exit(-1)
        if type(width) != int and type(width) != float:
            print("actual parameter passed are of invalid data type")
            sys.exit(-1)
        if type(height) != int and type(height) != float:
            print("actual parameter passed are of invalid data type")
            sys.exit(-1)

        self.length = length
        self.width = width
        self.height = height


class ssd_card():
    def __init__(self, brand: str, manufacturer: str, model: str, model_name: str, model_year: int, product_dimensions: dimensions, ram_size: int, storage: int, weight: float):
        """
        :param brand: brand of ssd card
        :param manufacturer: manufacturer name of ssd card
        :param model: model of ssd card
        :param model_name: model name of ssd card
        :param model_year: model year of ssd card
        :param product_dimensions: size of ssd card in terms of l, W, H
        :param ram_size: ram size of ssd card
        :param storage: total storage size of ssd card
        :param weight: weight of ssd card in float
        """
        if type(brand) != str or type(manufacturer) != str or type(model) != str or type(model_name) != str or type(model_year) != int or type(product_dimensions) != dimensions or type(ram_size) != int or type(storage) != int or type(weight) != float:
            print("actual parameters passed are not of valid data type")
            sys.exit(-1)

        self.brand = brand
        self.manufacturer = manufacturer
        self.model = model
        self.model_name = model_name
        self.model_year = model_year
        self.product_dimensions = product_dimensions
        self.ram_size = ram_size
        self.storage = storage
        self.weight = weight


ssd_card1 = ssd_card('sandisk', 'HP', 'x124w', 'xori', 2021, dimensions(2, 5, 6), 40, 40, 10.5)

print("printing details of ssd_card1:", ssd_card1.__dict__)