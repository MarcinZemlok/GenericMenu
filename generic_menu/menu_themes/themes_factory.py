#!/usr/bin/env python3

import importlib
import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] [%(name)s] %(message)s'
)
LOGGER = logging.getLogger(name=__name__)

class ThemesFactory:
    def __init__(self, generic_menu_instance):
        self.generic_menu_instance = generic_menu_instance
        self.package_location = os.path.dirname(os.path.realpath(__file__))
        self.themes_list = []

    def get_themes(self):
        if(len(self.themes_list) > 0): return self.themes_list

        for _, _, files in os.walk(self.package_location):
            for file in files:
                _file_name = os.path.splitext(os.path.basename(file))[0]
                if(['__init__', 'theme_interface', 'themes_factory'].__contains__(_file_name)): continue
                LOGGER.debug('Importing "%s" module', _file_name)
                _module = importlib.import_module(f'.{_file_name}', 'generic_menu.menu_themes')
                LOGGER.debug('Instanciating MenuTheme class')
                self.themes_list.append(_module.__getattribute__('MenuTheme')(self.generic_menu_instance))
                LOGGER.debug('Instanciated "%s"', self.themes_list[-1].get_name())
            break

        return self.themes_list

if(__name__ == '__main__'):
    LOGGER.debug('Stanalone')
else:
    LOGGER.debug('Imported')
