# -*- coding: utf-8 -*-

"""
Pythonic class collection that helps you structure external data from LHC / HEP experiments.
"""


__author__     = "Marcel Rieger"
__email__      = "python-order@googlegroups.com"
__copyright__  = "Copyright 2017, Marcel Rieger"
__credits__    = ["Marcel Rieger"]
__contact__    = "https://github.com/riga/order"
__license__    = "MIT"
__status__     = "Development"
__version__    = "0.0.1"
__all__        = ["UniqueObject", "UniqueObjectIndex", "AuxDataContainer", "TagContainer",
                  "DataSourceContainer", "SelectionContainer", "Channel", "Category", "Variable"]


# provisioning imports
from .unique import UniqueObject, UniqueObjectIndex
from .mixins import AuxDataContainer, TagContainer, DataSourceContainer, SelectionContainer
from .categorize import Channel, Category
from .variable import Variable

