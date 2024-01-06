"""
__init__.py: Entry point for the Nekrosis library.

Library usage:
    >>> from nekrosis import Nekrosis
    >>> nekrosis = Nekrosis(payload="/path/to/payload")

    >>> nekrosis.supported_persistence_methods()
    >>> nekrosis.recommended_persistence_method()
    >>> nekrosis.install()
"""

__version__:  str = "0.0.1"
__license__:  str = "3-clause BSD License"
__author__:   str = "Ezra Fast, Mitchell Nicholson, Mykola Grymalyuk, Scott Banister and Ulysses Hill"
__all__:     list = ["Nekrosis"]

from .core import Nekrosis, main