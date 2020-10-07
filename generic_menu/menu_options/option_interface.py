#!/usr/bin/env python3

import abc

import generic_menu

class IMenuOption(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, '__init__') and
                callable(subclass.__init__) and
                hasattr(subclass, 'run') and
                callable(subclass.run) or
                NotImplemented)

    @abc.abstractmethod
    def __init__(self, generic_menu_instance: generic_menu.generic_menu.GenericMenu):
        ''''''
        raise NotImplementedError

    @abc.abstractmethod
    def run(self):
        '''Run code defined by option'''
        raise NotImplementedError

    def get_name(self) -> str:
        '''Return option name'''
        return self.name

    def __eq__(self, other) -> bool:
        if(type(other) == generic_menu.menu_options.default_option.MenuOption): return (self.get_name() == other.get_name())
        elif(type(other) == str): return (self.get_name() == other)
        else: raise TypeError(f'Unsupported operation between "MenuOption" and "{type(other)}"')
