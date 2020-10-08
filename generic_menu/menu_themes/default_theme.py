#!/usr/bin/env python3

from generic_menu.generic_menu import GenericMenu
from .theme_interface import IMenuTheme
from ..common.prompts import Prompt
from ..common.ansi import ANSI

class MenuTheme(IMenuTheme):
    def __init__(self, generic_menu_instance: GenericMenu):
        ''''''
        self.__name = 'Default Theme'
        self.__prompt = 'Select option >> '
        self.__termination = 'q'
        self.__generic_menu_instance = generic_menu_instance

    def display_top(self):
        '''Display menu according to the theme'''
        _buff = f'''{"="*80}
{" "*int(40-len(self.__generic_menu_instance.get_header())/2)}{self.__generic_menu_instance.get_header()}
{"="*80}
Options:
'''
        for i, o in self.__generic_menu_instance.get_options_dict().items():
            _buff += f'[{i}] {o.get_name()}\n'

        _buff += '[q] Quit\n'
        _buff += '='*80

        ANSI.ansi_clear_display()
        print(_buff)

    def display_bottom(self):
        print('-'*40)
        Prompt.press_enter()

    def get_name(self) -> str:
        '''Return theme name'''
        return self.__name

    def get_prompt(self) -> str:
        '''Return theme prompt'''
        return self.__prompt

    def get_termination(self) -> str:
        '''Return theme termination'''
        return self.__termination
