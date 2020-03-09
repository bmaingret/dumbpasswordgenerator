""" dumbpasswordgenerator mmodule provides base calss and two different password generator.

This module was done as an exercice for the Machine Learning Nanodegree.

It provides two password generators to be used in code: `GenericPasswordGenerator` and `NumberPasswordGenerator`.

This is purely to showcase some software programming practices:
 * OOP
 * Unit tests
 * Documentation
 * Package and modularity

Example:
    >>> g = passwordgenerator.GenericPasswordGenerator()
    >>> g.new_password(10)
    'ChPlVYBKAo'    

Classes:
    * PasswordGenerator: Base class
    * GenericPasswordGenerator: ascii letter and digit passwords
    * NumberPasswordGenerator: digit passwords
    
"""

import random
import string

class PasswordGenerator(object):
    """ Password generator class for generating random passwords of different types.
    This should not be considered securely random.

    Attributes:
        length (int): default length for password
        
    """
    
    def __init__(self, length=12):
        self.length = length
        self._previous_password = None

    def new_password(self, length=None):
        """Function to generate and return a password.
        
        Args: 
            length (int): length for the password to generate. Length specified when iniating the generator will be 
            used if not provided, or the default length of the constructor if none was specified.
        
        Returns: 
            str:  generated password

        """

        raise NotImplementedError("Please Implement this method")


    def _basic_generate_password(self, length, chars = string.ascii_letters):
        """Private function for basic password generation.

        Args: 
            length (int): length if the password to generate
            chars (str): list of characters to be used in the password to generate
        
        Returns: 
            str: password string of length `length`and composed of char in `chars`

        """
        N = self.length
        if (length is not None):
            N = length
  
        password = ''.join(random.choices(chars, k=N))
        return password
    
    def previous_password(self):
        """Function to return the previously generated password.
        
        Args: 
            None
        
        Returns: 
            str: previously generated password, or None if no password had been generated before.
        """        
        return self._previous_password

class GenericPasswordGenerator(PasswordGenerator, object):
    """Basic implementation of the PasswordGenerator class that generates password composed
    of ascii letters (upper and lower) and digits.
    The characters are taken from the python string package:
    * string.ascii_lowercase
    * string.ascii_uppercase
    * string.digits

    """

    def new_password(self, length=None):
        """Implementation of the new_password method"""
        password = self._basic_generate_password(
            length = length,
            chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        )
        self._previous_password = password
        return password

class NumberPasswordGenerator(PasswordGenerator, object):
    """Basic implementation of the PasswordGenerator class that generates password composed
    of digits.
    The characters are taken from the python string package:
    * string.digits

    """

    def new_password(self, length=None):
        """Implementation of the new_password method"""
        password = self._basic_generate_password(
            length = length,
            chars = string.digits
        )
        self._previous_password = password
        return password
