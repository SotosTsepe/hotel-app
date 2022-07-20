"""Database models.

The package dynamically imports every submodule class to itself
so that every database model can be imported directly.

Example:
    from app.models import <model_name>

NOTE: The naming for the database columns follows the snakecase rule.
Use full names for the variables instead of abbreviations. This will
ensure that the column names will be meaningful when rendered in the
frontend pages. The technique used is capitalization of every letter
after each underscore and then substitution of each underscore with a
space.
"""

import os

from importlib import import_module
from inspect import isclass
from pkgutil import iter_modules


package_dir = os.path.dirname(__file__)
for i, module_name, _ in iter_modules([package_dir]):
    # import the module and iterate through its attributes
    module = import_module(f"{__name__}.{module_name}")

    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)

        if isclass(attribute):
            # Add to package's variables
            globals()[attribute_name] = attribute
