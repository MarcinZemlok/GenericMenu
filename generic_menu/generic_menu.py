#!/usr/bin/env python3

import importlib
import logging
import os
import sys

from colorama import init
init()

from .menu_options.options_factory import OptionsFactory
from .menu_themes.themes_factory import ThemesFactory

logging.basicConfig(
    level=logging.WARNING,
    format='[%(levelname)s] [%(name)s] %(message)s'
)
LOGGER = logging.getLogger(name=__name__)

class GenericMenu:
    def __init__(self, options_packages_directory: str = '', option_objects_list: list = [], theme_name: str = 'Default Theme', header='GenericMenu'):
        ''''''

        self.__header = header
        self.__package_location = os.path.dirname(os.path.realpath(__file__))
        self.__option = None

        # Load menu themes
        self.__themes_factory = ThemesFactory(self)
        self.__themes_list = self.__themes_factory.get_themes()

        # Setting active theme
        self.__active_theme = None
        for _theme in self.__themes_list:
            self.__active_theme = _theme if(self.__active_theme is None and _theme == theme_name) else _theme
        LOGGER.debug('Active theme name: %s', self.__active_theme.get_name())

        # Load menu options
        self.__options_factory = OptionsFactory(self, options_packages_directory)
        self.__options_dict = self.__options_factory.get_options()

    def display_top(self):
        self.__active_theme.display_top()

    def display_bottom(self):
        self.__active_theme.display_bottom()

    def request_option(self):
        self.__option = input(self.__active_theme.get_prompt())

    def execute_option(self):
        try:
            self.__options_dict[self.__option].run()
        except KeyError as err:
            if(self.__option != self.__active_theme.get_termination()):
                LOGGER.error("Wrong option specified: %s", e)

    def loop(self):
        while(True):
            self.display_top()
            self.request_option()
            if(self.__option == self.__active_theme.get_termination()): break
            self.execute_option()
            self.display_bottom()

    def get_option(self):
        return self.__option

    def get_header(self):
        return self.__header

    def get_package_location(self):
        return self.__package_location

    def get_themes_factory(self):
        return self.__themes_factory

    def get_themes_list(self):
        return self.__themes_list

    def get_active_theme(self):
        return self.__active_theme

    def get_options_factory(self):
        return self.__options_factory

    def get_options_dict(self):
        return self.__options_dict

    def __str__(self):
        _ret = f'''class: GenericMenu
\tAvailable themes:
'''
        for _theme in self.__themes_list:
            _selected = '* ' if(_theme == self.__active_theme) else '  '
            _ret += (f'\t\t{_selected}{_theme.get_name()}\n')

        _ret += '''\tAvailable options:
'''
        for _index, _option in self.__options_dict.items():
            _ret += (f'\t\t  [{_index}] {_option.get_name()}\n')

        return _ret

if(__name__ == '__main__'):
    LOGGER.debug('Stanalone')
else:
    LOGGER.debug('Imported')
