#!/usr/bin/env python3

import importlib
import logging
import os
import sys

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] [%(name)s] %(message)s'
)
LOGGER = logging.getLogger(name=__name__)

class OptionsFactory:
    def __init__(self, generic_menu_instance, options_packages_directory: str = ''):
        self.generic_menu_instance = generic_menu_instance
        self.options_packages_directory = options_packages_directory
        self.options_dict = {}

        if(self.options_packages_directory == ''): LOGGER.warning('Options factory instanciated with no options package directory')

    def get_options(self):
        if(self.options_packages_directory == '' or len(self.options_dict) > 0): return self.options_dict

        if(not self.options_packages_directory in sys.path):
            sys.path.append(self.options_packages_directory)

        _i = 0
        for _, directories, _ in os.walk(self.options_packages_directory):
            for directory in directories:
                if(['__pycache__'].__contains__(directory)): continue
                LOGGER.debug('Importing "%s" module', directory)
                _module = importlib.import_module('.gm_option', directory)
                LOGGER.debug('Instanciating MenuOption class')
                self.options_dict[str(_i)] = _module.__getattribute__('MenuOption')(self.generic_menu_instance)
                LOGGER.debug('Instanciated "%s"', self.options_dict[str(_i)].get_name())
                _i += 1
            break

        return self.options_dict

if(__name__ == '__main__'):
    LOGGER.debug('Stanalone')
else:
    LOGGER.debug('Imported')
