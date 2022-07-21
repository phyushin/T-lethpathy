#!/usr/bin/python
# Todo:
## file ops
## editing soldiers details - this will be tricky xD
##

import argparse
from lib.base import BaseGameFile as XcomBase
from lib.liglob import LiGlob
from lib.stores import *
from lib.AlienContainment import *
from lib.BaseFacility import *
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

def max_out_money(save_path):
    li_glob = LiGlob(save_path)
    li_glob.load_file()
    li_glob.set_max_money()
    li_glob.save_file()

def main():
    title = f"T\'leth-pathy, The X-Com savegame editor v{__version__}\n\n"
    parser = argparse.ArgumentParser(title)
    parser.add_argument("-f", dest="file_path", help="Path where the 'GAME_N' folders are", required=True)
    parser.add_argument("-gn", dest="game_no", help="the save game slot (1-10)", required=True)

    args=parser.parse_args()

    save_path = path.abspath(
            path.join(f"{args.file_path}",f"GAME_{args.game_no}")
    )

    xcombase = XcomBase(save_path)
    bases = xcombase.get_bases()

    # first let's max out our money
    max_out_money(save_path)

    # next let's rename out base!
    bases[0].set_name('Hi,STEELCON!')

    # then max out scientists
    bases[0].set_scientist_count(250)
    # lets mess with base number 1

    # set in progress build to finished

    bases[0].load_layout()
    _layout = bases[0].get_layout() # get current layout
    _construction_times = bases[0].get_construction_time_layout() #get build times

    ## Add alien containment to store our aliens (otherwise they will die)
    ac = Alien_Contain()
    tr = Transmission_Resolver()
    lab = Lab()

    _rank = Rank()
    bases[0].build_facility(1,4,ac) # Add alien containment else our alien chaps won't survive!
    bases[0].build_facility(2,4,tr) # lets replace that poor sonar with the transmission resolver

   #we now need a few extra labs for all our scientists)
    """
    bases[0].build_facility(3,5,lab)
    bases[0].build_facility(3,6,lab)
    bases[0].build_facility(4,5,lab)
    bases[0].build_facility(4,6,lab)
    """
    # add stuff to stores

    xcombase.update_base(bases[0]) # update the base we've been tinkering with
    xcombase.save_bases() # write all base data back to base.dat

    containment = AlienContainment(save_path)
    aq = Aquatoid()
    aqn = Aquatoid()
    aqn.set_rank(_rank.navigator())
    deep_one = DeepOne()

    containment.capture_alien(1, aq, bases[0].get_base_no())
    containment.capture_alien(2, deep_one, bases[0].get_base_no())
    containment.capture_alien(3, aqn, bases[0].get_base_no())

if __name__ == "__main__":
    main()
