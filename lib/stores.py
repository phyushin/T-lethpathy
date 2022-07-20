class Base_Stores():
    #by passsing olnlt the offsets needed for the stores bit we shouldn't need to care about the adjustment for each base as we'll just stack them all
    #back up again at the end
    def __init__(self, base_store_stream):
        self.base_store_stream = bytearray(base_store_stream)

    def set_item_qty(self, store_item):
        self.base_store_stream[store_item.offset] = store_item.qty #probably shouldn't do it like this but what ever xD

    def get_stores_data(self):
        return self.base_store_stream

class StoreItem():
    def __init__(self, offset, qty):
         self.offset = offset
         self.qty = qty

    def set_item_qty(self, qty):
        self.qty = qty

    def get_item_qty(self):
        return self.qty

## Sub Weps
class Ajax_Launcher(StoreItem):
    def __init__(self, qty):
        self.offset = 0x10
        self.qty = qty

class DUP_Launcher(StoreItem):
    def __init__(self, qty):
        self.offset = 0x12
        self.qty = qty

class Craft_Gas_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x14
        self.qty = qty

class PWT_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x16
        self.qty = qty

class Gauss_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x18
        self.qty = qty

class Sonic_Oscillator(StoreItem):
    def __init__(self, qty):
        self.offset = 0x1a
        self.qty = qty

## Ammo for Sub Weps

class Ajax_Torpedo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x1c
        self.qty = qty

class DUP_Torpedo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x1e
        self.qty = qty

class Craft_Gas_Cannon_Rounds(StoreItem):
    def __init__(self, qty):
        self.offset = 0x20
        self.qty = qty

class PWT(StoreItem):
    def __init__(self, qty):
        self.offset = 0x22
        self.qty = qty

## HWPs

class Coelacanth_G_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x24
        self.qty = qty

class Coelacanth_Aqua_Jet(StoreItem):
    def __init__(self, qty):
        self.offset = 0x26
        self.qty = qty

class Coelacanth_Gauss(StoreItem):
    def __init__(self, qty):
        self.offset = 0x28
        self.qty = qty

class Displacer_Sonic(StoreItem):
    def __init__(self, qty):
        self.offset = 0x2a
        self.qty = qty

class Displacer_PWT(StoreItem):
    def __init__(self, qty):
        self.offset = 0x2c
        self.qty = qty

## Guns/Amm

class Dart_Gun(StoreItem):
    def __init__(self, qty):
        self.offset = 0x2e
        self.qty = qty

class Dart_Glip(StoreItem):
    def __init__(self, qty):
        self.offset = 0x30
        self.qty = qty

class Jet_Harpoon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x32
        self.qty = qty

class Harpoon_Clip(StoreItem):
    def __init__(self, qty):
        self.offset = 0x34
        self.qty = qty

class Gas_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x36
        self.qty = qty

class GC_AP(StoreItem):
    def __init__(self, qty):
        self.offset = 0x38
        self.qty = qty

class GC_HE(StoreItem):
    def __init__(self, qty):
        self.offset = 0x3a
        self.qty = qty

class GC_Phosph(StoreItem):
    def __init__(self, qty):
        self.offset = 0x3c
        self.qty = qty

class Hydro_Jet_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x3e
        self.qty = qty

class HJ_AP(StoreItem):
    def __init__(self, qty):
        self.offset = 0x40
        self.qty = qty

class HJ_HE(StoreItem):
    def __init__(self, qty):
        self.offset = 0x42
        self.qty = qty

class HJ_Phosph(StoreItem):
    def __init__(self, qty):
        self.offset = 0x44
        self.qty = qty

class Torpedo_Launcher(StoreItem):
    def __init__(self, qty):
        self.offset = 0x46
        self.qty = qty

class Small_Torpedo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x48
        self.qty = qty

class Large_Torpedo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x4a
        self.qty = qty

class Phosph_Torpedo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x4c
        self.qty = qty

class Gauss_Pistol(StoreItem):
    def __init__(self, qty):
        self.offset = 0x4e
        self.qty = qty

class Gauss_Rifle(StoreItem):
    def __init__(self, qty):
        self.offset = 0x50
        self.qty = qty

class Heavy_Gauss(StoreItem):
    def __init__(self, qty):
        self.offset = 0x52
        self.qty = qty

class Magna_Blast_Grenade(StoreItem):
    def __init__(self, qty):
        self.offset = 0x54
        self.qty = qty

class Dye_Grenade(StoreItem):
    def __init__(self, qty):
        self.offset = 0x56
        self.qty = qty

class Partice_Dist_Grenade(StoreItem):
    def __init__(self, qty):
        self.offset = 0x58
        self.qty = qty

class Magna_Pack_Explosive(StoreItem):
    def __init__(self, qty):
        self.offset = 0x5a
        self.qty = qty

class Particle_Dist_Sensor(StoreItem):
    def __init__(self, qty):
        self.offset = 0x5c
        self.qty = qty

class Medikit(StoreItem):
    def __init__(self, qty):
        self.offset = 0x5e
        self.qty = qty

class MC_Disruptor(StoreItem):
    def __init__(self, qty):
        self.offset = 0x60
        self.qty = qty

class Thermal_Tazer(StoreItem):
    def __init__(self, qty):
        self.offset = 0x62
        self.qty = qty

class Chemical_Flare(StoreItem):
    def __init__(self, qty):
        self.offset =0x64
        self.qty = qty

class Vibro_Blade(StoreItem):
    def __init__(self, qty):
        self.offset = 0x66
        self.qty = qty

class Thermic_Lance(StoreItem):
    def __init__(self, qty):
        self.offset = 0x68
        self.qty = qty

class Heavy_Thermic_Lance(StoreItem):
    def __init__(self, qty):
        self.offset = 0x6a
        self.qty = qty

### Sonic weapons (gotta go fast!!)

class Sonic_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x72
        self.qty = qty

class Sonic_Cannon_Clip(StoreItem):
    def __init__(self, qty):
        self.offset = 0x74
        self.qty = qty


class Sonic_Blasta(StoreItem):
    def __init__(self, qty):
        self.offset = 0x76
        self.qty = qty

class Sonic_Blasta_Clip(StoreItem):
    def __init__(self, qty):
        self.offset = 0x78
        self.qty = qty

class Sonic_Pistol(StoreItem):
    def __init__(self, qty):
        self.offset = 0x7a
        self.qty = qty

class Sonic_Pistol_Clip(StoreItem):
    def __init__(self, qty):
        self.offset = 0x7c
        self.qty = qty

class Distuptor_Pulse_Launcher(StoreItem):
    def __init__(self, qty):
        self.offset = 0x7e
        self.qty = qty

class Distuptor_Ammo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x80
        self.qty = qty

class Thermal_Shok_Launcher(StoreItem):
    def __init__(self, qty):
        self.offset = 0x82
        self.qty = qty

class Thermal_Shok_Bomb(StoreItem):
    def __init__(self, qty):
        self.offset = 0x84
        self.qty = qty

class Sonic_Pulser(StoreItem):
    def __init__(self, qty):
        self.offset = 0x86
        self.qty = qty

class Zrbite(StoreItem):
    def __init__(self, qty):
        self.offset = 0x88
        self.qty = qty

class MC_Reader(StoreItem):
    def __init__(self, qty):
        self.offset = 0x8a
        self.qty = qty

### Dead Aliens
class Aqautoid(StoreItem):
    def __init__(self, qty):
        self.offset = 0x92
        self.qty = qty

class Gill_Man(StoreItem):
    def __init__(self, qty):
        self.offset = 0x94
        self.qty = qty

class Lobster_Man(StoreItem):
    def __init__(self, qty):
        self.offset = 0x96
        self.qty = qty

class Tasoth(StoreItem):
    def __init__(self, qty):
        self.offset = 0x98
        self.qty = qty

class Calcinite(StoreItem):
    def __init__(self, qty):
        self.offset = 0x9a
        self.qty = qty

class Deep_One(StoreItem):
    def __init__(self, qty):
        self.offset = 0x9c
        self.qty = qty

class Bio_Drone(StoreItem):
    def __init__(self, qty):
        self.offset = 0x9e
        self.qty = qty

class Tentaculat(StoreItem):
    def __init__(self, qty):
        self.offset = 0xa0
        self.qty = qty

class Triscene(StoreItem):
    def __init__(self, qty):
        self.offset = 0xa2
        self.qty = qty

class Hallucinoid(StoreItem):
    def __init__(self, qty):
        self.offset = 0xa4
        self.qty = qty

class Xarquid(StoreItem):
    def __init__(self, qty):
        self.offset = 0xa6
        self.qty = qty

### Submarine Parts

class Ion_Beam_Acc(StoreItem):
    def __init__(self, qty):
        self.offset = 0xb0
        self.qty = qty

class Magnetic_Navigation(StoreItem):
    def __init__(self, qty):
        self.offset = 0xb2
        self.qty = qty

class Alien_Sub_Construction(StoreItem):
    def __init__(self, qty):
        self.offset = 0xb4
        self.qty = qty

class Alien_Cryogenics(StoreItem):
    def __init__(self, qty):
        self.offset = 0xb6
        self.qty = qty

class Alien_Cloning(StoreItem):
    def __init__(self, qty):
        self.offset = 0xb8
        self.qty = qty

class Alien_Learning_Arrays(StoreItem):
    def __init__(self, qty):
        self.offset = 0xba
        self.qty = qty

class Alien_Implanter(StoreItem):
    def __init__(self, qty):
        self.offset = 0xbc
        self.qty = qty

class Examination_Room(StoreItem):
    def __init__(self, qty):
        self.offset = 0xbe
        self.qty = qty

class Aqua_Plastics(StoreItem):
    def __init__(self, qty):
        self.offset = 0xc0
        self.qty = qty

class Alien_ReAnimation_Zone(StoreItem):
    def __init__(self, qty):
        self.offset = 0xc2
        self.qty = qty

class Plastic_Aqua_Armour(StoreItem):
    def __init__(self, qty):
        self.offset = 0xc4
        self.qty = qty

class Ion_Armour(StoreItem):
    def __init__(self, qty):
        self.offset = 0xc6
        self.qty = qty

class Magnetic_Ion_Armour(StoreItem):
    def __init__(self, qty):
        self.offset = 0xc6
        self.qty = qty
