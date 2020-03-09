# Demo package - Dumb Password Generator

This package was done as an exercice for the Machine Learning Nanodegree.

It provides two password generators to be used in code: `GenericPasswordGenerator` and `NumberPasswordGenerator`.

This is purely to showcase some software programming practices:
 * OOP
 * Unit tests
 * Documentation
 * Package and modularity

## Installation
```
    pip install -i https://test.pypi.org/simple/ dumbpasswordgenerator
```

## Usage

``` python
    generator = GenericPasswordGenerator(length=10)
    new_password = generator.new_password()
    new_password_2 = generator.new_password(length=5) # It is possible to override the default length
    forgotten_password = generator.previous_password() # Get the previously generated password
```
