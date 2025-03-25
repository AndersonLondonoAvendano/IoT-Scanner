import os
from termcolor import colored, cprint

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner(text, color):
    cprint(text, color)

def print_message(text, color, attrs=None):
    cprint(text, color, attrs=attrs)