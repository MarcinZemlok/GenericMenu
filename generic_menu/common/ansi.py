#!/usr/bin/env python3

class ANSI:
    def __new__(cls):
        return None

    @staticmethod
    def ansi_clear_display():
        print('\x1b[2J')