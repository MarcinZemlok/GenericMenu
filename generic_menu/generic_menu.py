#!/usr/bin/env python3

import importlib
import logging
import os
import sys

from .menu_options.options_factory import OptionsFactory
from .menu_themes.themes_factory import ThemesFactory

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] [%(name)s] %(message)s'
)
LOGGER = logging.getLogger(name=__name__)

class GenericMenu:
    def __init__(self, options_packages_directory: str = '', option_objects_list: list = [], theme_name: str = 'Default Theme', header='GenericMenu'):
        ''''''

        self.header = header
        self.package_location = os.path.dirname(os.path.realpath(__file__))

        # Load menu themes
        self.themes_factory = ThemesFactory(self)
        self.themes_list = self.themes_factory.get_themes()

        # Setting active theme
        self.active_theme = None
        for _theme in self.themes_list:
            self.active_theme = _theme if(self.active_theme is None and _theme == theme_name) else _theme
        LOGGER.debug('Active theme name: %s', self.active_theme.get_name())

        # Load menu options
        self.options_factory = OptionsFactory(self, options_packages_directory)
        self.options_dict = self.options_factory.get_options()

    def display(self):
        self.active_theme.display()

    def loop(self):
        _option = ''

        while(_option != self.active_theme.termination):
            self.display()
            _option = input(self.active_theme.prompt)

            try:
                self.options_dict[_option].run()
            except KeyError as err:
                if(_option != self.active_theme.termination):
                    LOGGER.error("Wrong option specified: %s", e)

    def __str__(self):
        _ret = f'''class: GenericMenu
\tAvailable themes:
'''
        for _theme in self.themes_list:
            _selected = '* ' if(_theme == self.active_theme) else '  '
            _ret += (f'\t\t{_selected}{_theme.get_name()}\n')

        _ret += '''\tAvailable options:
'''
        for _index, _option in self.options_dict.items():
            _ret += (f'\t\t  [{_index}] {_option.get_name()}\n')

        return _ret

if(__name__ == '__main__'):
    LOGGER.debug('Stanalone')
else:
    LOGGER.debug('Imported')
