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

from lib.Research import Research

from os import path
from pathlib import Path as plib

__author__ = "Paul W"
__version__ = 0.8

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

def add_sonic_weps(base):
    weps = []
    weps.append(Sonic_Cannon(1))
    weps.append(Sonic_Cannon_Clip(1))
    weps.append(Sonic_Blasta(1))
    weps.append(Sonic_Blasta_Clip(1))
    weps.append(Sonic_Pistol(1))
    weps.append(Sonic_Pistol_Clip(1))
    weps.append(Sonic_Pulser(1))
    weps.append(Sonic_Oscillator(8))
    base.set_stores(weps)

def main():
    title = f"T\'leth-pathy, The X-Com savegame editor v{__version__}\n\n"
    parser = argparse.ArgumentParser(title)
    parser.add_argument("-f", dest="file_path", help="Path where the 'GAME_N' folders are", required=True)
    parser.add_argument("-gn", dest="game_no", help="the save game slot (1-10)", required=True)

    args=parser.parse_args()

    save_path = path.abspath(
            path.join(f"{args.file_path}",f"GAME_{args.game_no}")
    )
    research = Research(save_path)
    research.load_file()
    research.print_info()


    xcombase = XcomBase(save_path)
    bases = xcombase.get_bases()

    # first let's max out our money
    max_out_money(save_path)

    # next let's rename out base!
    bases[0].set_name('Hi,STEELCON!')

    # then max out scientists
    bases[0].set_scientist_count(250)
    bases[0].set_technician_count(50)
    # lets mess with base number 1

    # set in progress build to finished


    bases[0].load_layout()
    _layout = bases[0].get_layout() # get current layout
    _construction_times = bases[0].get_construction_time_layout() #get build times

    ## Add alien containment to store our aliens (otherwise they will die)
    _rank = Rank()

    print("building alien containment")
    bases[0].build_facility(1,4, Alien_Contain()) # Add alien containment else our alien chaps won't survive!

    print("building transmission resolver")
    bases[0].build_facility(2,4, Transmission_Resolver()) # lets replace that poor sonar with the transmission resolver

   #we now need a few extra labs for all our scientists)

    print("building 4 more labs for all the extra scientists")
    bases[0].build_facility(3,5,Lab())
    bases[0].build_facility(3,6,Lab())
    bases[0].build_facility(4,5,Lab())
    bases[0].build_facility(4,6,Lab())

    # add stuff to stores

    submarine_construction = []
    submarine_construction.append(Alien_Sub_Construction(1))
    submarine_construction.append(Ion_Beam_Acc(20))
    submarine_construction.append(Magnetic_Navigation(20))
    bases[0].set_stores(submarine_construction)

    _zrbite = Zrbite(100000)
    _ap = Aqua_Plastics(100000)
    _deep_one_corpse = Deep_One(1)

    add_sonic_weps(bases[0])

    shopping_list = []

    shopping_list.append(Magnetic_Ion_Armour(200))
    shopping_list.append(Sonic_Oscillator(8))
    bases[0].set_stores(shopping_list)

    bases[0].set_stores([_zrbite])
    bases[0].set_stores([_ap])
    bases[0].set_stores([_deep_one_corpse])

    bases[1].load_layout()
    bases[1].build_facilities()

    xcombase.update_base(bases[1])

    xcombase.update_base(bases[0]) # update the base we've been tinkering with
    xcombase.save_bases() # write all base data back to base.dat

    ### Alien Containment Stuff
    containment = AlienContainment(save_path)
    """
    aq = Aquatoid()
    aqn = Aquatoid()
    lobsterman = Lobster_man()
    lobsterman.set_rank(_rank.commander())
    aqn.set_rank(_rank.navigator())
    live_deep_one = DeepOne()

    # Lets capture some aliens

    containment.capture_alien(1, aq, bases[0].get_base_no())
    containment.capture_alien(2, live_deep_one, bases[0].get_base_no())
    containment.capture_alien(3, aqn, bases[0].get_base_no())
    containment.capture_alien(4, lobsterman, bases[0].get_base_no())
    containment.capture_alien(5, lobsterman, bases[0].get_base_no())
    lobsterman.set_rank(_rank.navigator())

    containment.capture_alien(6, lobsterman, bases[0].get_base_no())
    """
    aliens = []
    aliens.append(Aquatoid(_rank.navigator()))
    aliens.append(DeepOne())
    aliens.append(Calcinite())
    aliens.append(Lobster_man(_rank.medic()))

    containment.capture_aliens(aliens, bases[0])

if __name__ == "__main__":
    main()
