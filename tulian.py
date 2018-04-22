#!/usr/bin/python3
""" Provides insights and filtered data from method parameter. """

from json import dumps

from modules.mutable import Mutable
from modules.immutable import Immutable

__author__ = "@ivanleoncz"


class Tulian(Mutable, Immutable):


    def summary(self, data):
        """
        Summary of all information contained on data.

        Parameters
        ----------
        data : tuple or list
            Composed of multiple data types.

        Returns
        -------
        d : dictionary
            Presents a summary of all information contained in data.
        """
        d = {}
        d["int"]         = len(self.ints(data))
        d["bytes"]       = len(self.bytes(data))
        d["bytearrays"]  = len(self.bytearray(data))
        d["complex"]     = len(self.complex(data))
        d["float"]       = len(self.ints(data))
        d["str"]         = len(self.strs(data))
        d["dict"]        = len(self.dicts(data))
        d["tuples"]      = len(self.tuples(data))
        d["lists"]       = len(self.lists(data))
        d["sets"]        = len(self.sets(data))
        d["frozensets"]  = len(self.frozen(data))
        d["booleans"]    = len(self.booleans(data))
        new_d = { k:v for (k,v) in d.items() if d[k] != 0}
        return dumps(new_d, indent=4)
