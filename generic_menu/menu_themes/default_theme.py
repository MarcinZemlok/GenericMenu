#!/usr/bin/env python3

from generic_menu.generic_menu import GenericMenu
from .theme_interface import IMenuTheme

class MenuTheme(IMenuTheme):
    def __init__(self, generic_menu_instance: GenericMenu):
        ''''''
        self.name = 'Default Theme'
        self.prompt = 'Select option >> '
        self.termination = 'q'
        self.generic_menu_instance = generic_menu_instance

    def display(self):
        '''Display menu according to the theme'''
        _buff = f'''{"="*80}
{" "*int(40-len(self.generic_menu_instance.header)/2)}{self.generic_menu_instance.header}
{"="*80}
Options:
'''
        for i, o in self.generic_menu_instance.options_dict.items():
            _buff += f'[{i}] {o.get_name()}\n'

        _buff += '[q] Quit\n'
        _buff += '='*80

        print(_buff)
