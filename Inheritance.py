# define a bunch of attributes and functions and things inside of a class
# then we can create another class and we can inherit all of those attributes
# we have one class that has all the functionality of another class w/o having to rewrite any of the same methods or attributes

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()