#!/usr/bin/env python3
import argparse
from lib.base_save_game_dat_file import BaseDatFile as Base
from lib.save_game_dat_file import SaveGameDatFile as DatFile
version = 0.2
parser = argparse.ArgumentParser(
	prog='XCOM Save Game Editor',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description='''\
   _  ___________  __  ___  ____                ____   ___ __          
  | |/_/ ___/ __ \/  |/  / / __/__ __  _____   / __/__/ (_) /____  ____
 _>  </ /__/ /_/ / /|_/ / _\ \/ _ `/ |/ / -_) / _// _  / / __/ _ \/ __/
/_/|_|\___/\____/_/  /_/ /___/\_,_/|___/\__/ /___/\_,_/_/\__/\___/_/   
                                                                      
                                                    v{0} - @Phyushin'''.format(version),
    epilog='XCOM Save Game Editor')
group = parser.add_mutually_exclusive_group()

group.add_argument("-v","--verbose", help="Run editor in verbose mode", action="store_true")
group.add_argument("-q","--quiet", help="Run editor in quiet mode (default)",default=True, action="store_true")
parser.add_argument("-p","--path", help="Path to XCOM folder", required=True)
parser.add_argument("-g","--game", type=int, choices=[1,2,3,4,5,6,7,8,9,10], help="Save game to edit", required=True)
parser.add_argument("--cash", help = "Path the game to give you $800M", action="store_true")
args = parser.parse_args()

if args.cash:
	gameData = DatFile(args.path, args.game, args.verbose)
	gameData.add_cash()
baseData = Base(args.path, args.game, args.verbose)
