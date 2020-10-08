#!/usr/bin/env python3

import abc

import generic_menu

class IMenuTheme(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, '__init__') and
                callable(subclass.__init__) and
                hasattr(subclass, 'get_name') and
                callable(subclass.get_name) and
                hasattr(subclass, 'get_prompt') and
                callable(subclass.get_prompt) and
                hasattr(subclass, 'get_termination') and
                callable(subclass.get_termination) and
                hasattr(subclass, 'display_top') and
                callable(subclass.display_top) and
                hasattr(subclass, 'display_bottom') and
                callable(subclass.display_bottom) or
                NotImplemented)

    @abc.abstractmethod
    def __init__(self, generic_menu_instance: generic_menu.generic_menu.GenericMenu):
        ''''''
        raise NotImplementedError

    @abc.abstractmethod
    def display_top(self):
        '''Display menu according to the theme'''
        raise NotImplementedError

    @abc.abstractmethod
    def display_bottom(self):
        '''Display menu according to the theme'''
        raise NotImplementedError

    @abc.abstractmethod
    def get_name(self) -> str:
        '''Return theme name'''
        raise NotImplementedError

    @abc.abstractmethod
    def get_prompt(self) -> str:
        '''Return theme prompt'''
        raise NotImplementedError

    @abc.abstractmethod
    def get_termination(self) -> str:
        '''Return theme termination'''
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        if(type(other) == generic_menu.menu_themes.default_theme.MenuTheme): return (self.get_name() == other.get_name())
        elif(type(other) == str): return (self.get_name() == other)
        else: raise TypeError(f'Unsupported operation between "MenuTheme" and "{type(other)}"')
