#!/usr/bin/python
# Todo:
## file ops
## editing soldiers details - this will be tricky xD
##

import argparse
from lib.base import BaseGameFile as XcomBase
from lib.stores import Zrbite
from os import path
from pathlib import Path as plib

__author__ = "Paul W"
__version__ = 0.2

def load_base_file(file_path):
    base = ""
    print ("Base file loaded")
    return bases

def load_save_game_file(file_path):
    p = plib(file_path)

    if not p.is_dir():
        print (f"Failed to load file at {file_path}")
        save_game_file = {}
    else:
        save_game_file = load_base_file(file_path)

    return save_game_file

def main():
    title = f"T\'leth-pathy, The X-Com savegame editor v{__version__}\n\n"

    parser = argparse.ArgumentParser(title)
    parser.add_argument("-f", dest="file_path", help="Path where the 'GAME_N' folders are", required=True)
    parser.add_argument("-gn", dest="game_no", help="the save game slot (1-10)", required=True)

    args=parser.parse_args()

    save_path = path.abspath(
            path.join(f"{args.file_path}",f"GAME_{args.game_no}")
    )

    xcombases = XcomBase(save_path)
    bases = xcombases.get_bases()

    print(bases[0].get_info())
    bases[0].set_scientist_count(500)
    print(bases[0].get_info())

if __name__ == "__main__":
    main()
