#!/usr/bin/python3

"""MyInt inherits from int"""
class MyInt(int):
    """inherits from in built class int"""

    def __eq__(self, value):
        """flipping equal to function"""
        return (self.real != value)

    def __ne__(self, value):
        """flipping not equal to function"""
        return (self.real == value)
