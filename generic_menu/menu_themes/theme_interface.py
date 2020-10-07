#!/usr/bin/env python3

import abc

import generic_menu

class IMenuTheme(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, '__init__') and
                callable(subclass.__init__) and
                hasattr(subclass, 'display') and
                callable(subclass.display) or
                NotImplemented)

    @abc.abstractmethod
    def __init__(self, generic_menu_instance: generic_menu.generic_menu.GenericMenu):
        ''''''
        raise NotImplementedError

    @abc.abstractmethod
    def display(self):
        '''Display menu according to the theme'''
        raise NotImplementedError

    def get_name(self) -> str:
        '''Return theme name'''
        return self.name

    def __eq__(self, other) -> bool:
        if(type(other) == generic_menu.menu_themes.default_theme.MenuTheme): return (self.get_name() == other.get_name())
        elif(type(other) == str): return (self.get_name() == other)
        else: raise TypeError(f'Unsupported operation between "MenuTheme" and "{type(other)}"')
