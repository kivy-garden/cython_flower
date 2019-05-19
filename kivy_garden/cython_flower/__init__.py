"""
Demo flower using cython
=========================

Defines the Kivy garden :class:`CythonFlowerLabel` class which is
the widget provided by the demo cython flower. 
"""

from kivy.uix.label import Label

__all__ = ('CythonFlowerLabel', )

__version__ = '0.1.0.dev0'


class CythonFlowerLabel(Label):

    def __init__(self, **kwargs):
        # cannot be imported before it's compiled
        from ._compute import compute
        val = compute('Demo flower', 2)
        super(CythonFlowerLabel, self).__init__(**kwargs, text=val)
