#!/usr/bin/env python3

import abc

class IOption(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_name') and
                callable(subclass.get_name) and
                hasattr(subclass, 'run') and
                callable(subclass.run) or
                NotImplemented)

    @abc.abstractmethod
    def get_name(self):
        """Return option name"""
        raise NotImplementedError

    @abc.abstractmethod
    def run(self):
        """Run code defined by option"""
        raise NotImplementedError
