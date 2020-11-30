import readline
from termcolor import colored
from colorama import init
from colorama import Fore, Back, Style
from core.command_parser import CParser
import core.session_manager as sm
import config
import platform
import os

class Clx:
    '''A class to manage command line.'''
    def __init__(self):
        pass

    @staticmethod
    def start():
        #TODO: setup listener for commands
        _session = sm.Session()
        #TODO : Remove below line from prod code.
        _parser = CParser()
        Clx.clear_screen()
        Clx.print_banner()
        while True:
            #command = input(colored('m#$h>', 'green', attrs=['bold']))
            command = input(
                Fore.MAGENTA + 
                'eks' + 
                Fore.BLUE + 
                'm#$h> ' + 
                Fore.WHITE
            )
            if command == 'q':
                print(Fore.YELLOW + 'Bye')
                Clx.reset_style()
                break
            _parse_command = _parser.parse_command(_session, command)
            Clx.do_parse_result(_parse_command)
                

    @staticmethod
    def print_banner():
        init()
        self.print_banner()
        Clx.reset_style()

    @staticmethod
    def print_banner():
        print(Fore.MAGENTA)
        print(Fore.MAGENTA + '        _                     ' + Fore.BLUE + '__  _      _    _')
        print(Fore.MAGENTA + '       | |                  ' + Fore.BLUE + '_|  || |_  _| |_ | |')
        print(Fore.MAGENTA + '  ____ | |  _   ___  ' + Fore.BLUE + '____  (_   __  _)|  ___)| | _')
        print(Fore.MAGENTA + ' / _  )| | / ) /___)' + Fore.BLUE + '|    \  _| |__| | |___  || || \\')
        print(Fore.MAGENTA + '( (/ / | |< ( |___ |' + Fore.BLUE + '| | | |(_       _)(_   _|| | | |')
        print(Fore.MAGENTA + ' \____)|_| \_)(___/ ' + Fore.BLUE + '|_|_|_|  |__||_|    |_|  |_| |_|')
        print(Fore.WHITE)
        print('Use verbs to initiate action.')
        print('Make sure parameters are clearly defined like below.')
        print(Fore.GREEN + 'set project --name=<project name>')
        print(Fore.GREEN + 'test iotclient --app=<app name> --provider=<cloud provider>')
        print(Fore.GREEN + 'init fastapi')
        print(Fore.GREEN + 'init faust')
        print(Fore.GREEN + 'test faust')
        print(Fore.CYAN + 'For help: type do help or get help')


    @staticmethod
    def reset_style():
        print(Style.RESET_ALL)

    @staticmethod
    def clear_screen():
        if(platform.system()=='Windows'):
            os.system('cls')
        else:
            os.system('clear')


    @staticmethod
    def do_parse_result(result):
        if result['status'] == 1:
            Clx.reset_style()
        else:
            print(Fore.RED + Style.BRIGHT + result['message'])
            Clx.reset_style()


    
    

    