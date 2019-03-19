from enum import Enum
from binascii import hexlify,unhexlify

#Base
class SaveGameConstants(Enum):
	Base_Length = 124
	Engineer_Count_Loc  = '5E'
	Scientist_Count_Loc = '5F'
	Max_Cash = 'FFFFFF32'

class Facilities(Enum):
	Access_Lift = unhexlify('00')
	Living_Qtrs = unhexlify('01')
	Lab = unhexlify('02')
	Workshop = unhexlify('03')
	Radar_SR = unhexlify('04')
	Radar_LR = unhexlify('05')
	Missle_Def = unhexlify('06')
	General_Stores = unhexlify('07')
	Alien_Containment = unhexlify('08')
	Laser_Def = unhexlify('09')
	Plasma_Def = unhexlify('0A')
	Fusion_Def = unhexlify('0B')
	Grav_Shield = unhexlify('0C')
	Mind_Shield = unhexlify('0D')
	Psi_Lab = unhexlify('0E')
	Hyperwave_Decoder = unhexlify('0F')
	Hangar_Top_Left = unhexlify('10')
	Hangar_Top_Right = unhexlify('11')
	Hangar_Bottom_Left = unhexlify('12')
	Hangar_Bottom_Right = unhexlify('13')

#Items - Note these are 2 byte ints
class Items(Enum):
	#Ship Weapons
	Stingray_Launcher = unhexlify('60')
	Avalance_Launcher = unhexlify('62')
	Cannon = unhexlify('64')
	Fusion_Ball_Launcher = unhexlify('66')
	Laser_Cannon = unhexlify('68')
	Plasma_Beam = unhexlify('6A')
	#Ammo for Ship's Weapons
	Stingray_Missile = unhexlify('6C')
	Avalanche_Missile = unhexlify('6E')
	Cannon_Rounds = unhexlify('70') #x50
	Fusion_Ball = unhexlify('72')
	#Heavy Weapons Platforms
	Tank_Cannon = unhexlify('74')
	Tank_Cannon_Ammo = unhexlify('011A')
	Tank_Rocket = unhexlify('76')
	Tank_Rocket_Ammo = unhexlify('011C')
	Tank_Laser = unhexlify('78')
	HoverTank_Plasma = unhexlify('7A')
	HoverTank_Launcher = unhexlify('7C')
	HoverTank_Launcher_Ammo = unhexlify('011E')
	#Inventory
	Pistol = unhexlify('7E')
	Pistol_Clip = unhexlify('80')
	Rifle = unhexlify('82')
	Rifle_Clip = unhexlify('84')
	Heavy_Cannon= unhexlify('86')
	HC_AP_Ammo = unhexlify('88')
	HC_HE_Ammo = unhexlify('8A')
	HC_I_Ammo = unhexlify('8C')
	Auto_Cannon =  unhexlify('8E')
	AC_AP_Ammo = unhexlify('90')
	AC_HE_Ammo = unhexlify('92')
	AC_I_Ammo = unhexlify('94')
	Rocket_Launcher = unhexlify('96')
	Rocket_Small = unhexlify('98')
	Rocket_Large = unhexlify('9A')
	Rocket_Incendiary = unhexlify('9C')
	Laser_Pistol = unhexlify('9E')
	Laser_Rifle = unhexlify('A0')
	Heavy_Laser = unhexlify('A2')
	Grenade = unhexlify('A4')
	Smoke_Grenade = unhexlify('A6')
	Proximity_Grenade = unhexlify('A8')
	Hi_Explosive = unhexlify('AA')
	Motion_Scanner = unhexlify('AC')
	Medikit = unhexlify('AE')
	Psi_Amp = unhexlify('B0')
	Stun_Rod = unhexlify('B2')
	Electro_Flare = unhexlify('B4')
	Heavy_Plasma = unhexlify('C2')
	HP_Clip = unhexlify('C4')
	Plasma_Rifle = unhexlify('C6')
	Plasma_Rifle_Clip = unhexlify('C8')
	Plasma_Pistol = unhexlify('CA')
	Plasma_Pistol_Clip = unhexlify('CC')
	Blaster_Launcher = unhexlify('CE')
	Blaster_Bomb = unhexlify('D0')
	Small_Launcher = unhexlify('D2')
	Stun_Bomb = unhexlify('D4')
	Alien_Grenade = unhexlify('D6')
	Elerium = unhexlify('D8')
	Mind_Probe = unhexlify('DA')
	#Alien Corpses
	Sectiod = unhexlify('E2')
	Snakeman = unhexlify('E4')
	Etherial = unhexlify('E6')
	Muton = unhexlify('E8')
	Floater = unhexlify('EA')
	Celatid = unhexlify('EC')
	Silacoid = unhexlify('EE')
	Crysalid = unhexlify('F0')
	Reaper = unhexlify('F2')
	Sectopod = unhexlify('F4')
	Cyberdisc = unhexlify('F6')
	#UFO Components
	Power_Source = unhexlify('0100')
	Navigation = unhexlify('0102')
	Alien_Alloys = unhexlify('0110')
	#Alien Base
	Alien_Food = unhexlify('0106')
	Alien_Reproduction = unhexlify('0108')
	Alien_Entertainment = unhexlify('010A')
	Alien_Surgery = unhexlify('010C')
	Examination_Room = unhexlify('010E')
	#Armour
	Personal_Armour = unhexlify('0114')
	Power_Suit = unhexlify('0116')
	Flying_Suit = unhexlify('0118')

