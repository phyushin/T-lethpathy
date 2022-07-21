class StoreItem():
    def __init__(self, offset, qty):
         self.offset = offset
         self.set_item_qty(qty)

    def set_item_qty(self, qty):
        _max_qty = 30000
        if qty > _max_qty:
            self.qty = _max_qty
        else:
            self.qty = qty

    def get_location(self):
        return self.offset

    def get_qty(self):
        return self.qty.to_bytes(2, 'little')

## Sub Weps
class Ajax_Launcher(StoreItem):
    def __init__(self, qty):
        self.offset = 0x10
        self.set_item_qty(qty)

class DUP_Launcher(StoreItem):
    def __init__(self, qty):
        self.offset = 0x12
        self.set_item_qty(qty)

class Craft_Gas_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x14
        self.set_item_qty(qty)

class PWT_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x16
        self.set_item_qty(qty)

class Gauss_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x18
        self.set_item_qty(qty)

class Sonic_Oscillator(StoreItem):
    def __init__(self, qty):
        self.offset = 0x1a
        self.set_item_qty(qty)

## Ammo for Sub Weps

class Ajax_Torpedo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x1c
        self.set_item_qty(qty)

class DUP_Torpedo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x1e
        self.set_item_qty(qty)

class Craft_Gas_Cannon_Rounds(StoreItem):
    def __init__(self, qty):
        self.offset = 0x20
        self.set_item_qty(qty)

class PWT(StoreItem):
    def __init__(self, qty):
        self.offset = 0x22
        self.set_item_qty(qty)

## HWPs

class Coelacanth_G_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x24
        self.set_item_qty(qty)

class Coelacanth_Aqua_Jet(StoreItem):
    def __init__(self, qty):
        self.offset = 0x26
        self.set_item_qty(qty)

class Coelacanth_Gauss(StoreItem):
    def __init__(self, qty):
        self.offset = 0x28
        self.set_item_qty(qty)

class Displacer_Sonic(StoreItem):
    def __init__(self, qty):
        self.offset = 0x2a
        self.set_item_qty(qty)

class Displacer_PWT(StoreItem):
    def __init__(self, qty):
        self.offset = 0x2c
        self.set_item_qty(qty)

## Guns/Amm

class Dart_Gun(StoreItem):
    def __init__(self, qty):
        self.offset = 0x2e
        self.set_item_qty(qty)

class Dart_Glip(StoreItem):
    def __init__(self, qty):
        self.offset = 0x30
        self.set_item_qty(qty)

class Jet_Harpoon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x32
        self.set_item_qty(qty)

class Harpoon_Clip(StoreItem):
    def __init__(self, qty):
        self.offset = 0x34
        self.set_item_qty(qty)

class Gas_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x36
        self.set_item_qty(qty)

class GC_AP(StoreItem):
    def __init__(self, qty):
        self.offset = 0x38
        self.set_item_qty(qty)

class GC_HE(StoreItem):
    def __init__(self, qty):
        self.offset = 0x3a
        self.set_item_qty(qty)

class GC_Phosph(StoreItem):
    def __init__(self, qty):
        self.offset = 0x3c
        self.set_item_qty(qty)

class Hydro_Jet_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x3e
        self.set_item_qty(qty)

class HJ_AP(StoreItem):
    def __init__(self, qty):
        self.offset = 0x40
        self.set_item_qty(qty)

class HJ_HE(StoreItem):
    def __init__(self, qty):
        self.offset = 0x42
        self.set_item_qty(qty)

class HJ_Phosph(StoreItem):
    def __init__(self, qty):
        self.offset = 0x44
        self.set_item_qty(qty)

class Torpedo_Launcher(StoreItem):
    def __init__(self, qty):
        self.offset = 0x46
        self.set_item_qty(qty)

class Small_Torpedo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x48
        self.set_item_qty(qty)

class Large_Torpedo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x4a
        self.set_item_qty(qty)

class Phosph_Torpedo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x4c
        self.set_item_qty(qty)

class Gauss_Pistol(StoreItem):
    def __init__(self, qty):
        self.offset = 0x4e
        self.set_item_qty(qty)

class Gauss_Rifle(StoreItem):
    def __init__(self, qty):
        self.offset = 0x50
        self.set_item_qty(qty)

class Heavy_Gauss(StoreItem):
    def __init__(self, qty):
        self.offset = 0x52
        self.set_item_qty(qty)

class Magna_Blast_Grenade(StoreItem):
    def __init__(self, qty):
        self.offset = 0x54
        self.set_item_qty(qty)

class Dye_Grenade(StoreItem):
    def __init__(self, qty):
        self.offset = 0x56
        self.set_item_qty(qty)

class Partice_Dist_Grenade(StoreItem):
    def __init__(self, qty):
        self.offset = 0x58
        self.set_item_qty(qty)

class Magna_Pack_Explosive(StoreItem):
    def __init__(self, qty):
        self.offset = 0x5a
        self.set_item_qty(qty)

class Particle_Dist_Sensor(StoreItem):
    def __init__(self, qty):
        self.offset = 0x5c
        self.set_item_qty(qty)

class Medikit(StoreItem):
    def __init__(self, qty):
        self.offset = 0x5e
        self.set_item_qty(qty)

class MC_Disruptor(StoreItem):
    def __init__(self, qty):
        self.offset = 0x60
        self.set_item_qty(qty)

class Thermal_Tazer(StoreItem):
    def __init__(self, qty):
        self.offset = 0x62
        self.set_item_qty(qty)

class Chemical_Flare(StoreItem):
    def __init__(self, qty):
        self.offset =0x64
        self.set_item_qty(qty)

class Vibro_Blade(StoreItem):
    def __init__(self, qty):
        self.offset = 0x66
        self.set_item_qty(qty)

class Thermic_Lance(StoreItem):
    def __init__(self, qty):
        self.offset = 0x68
        self.set_item_qty(qty)

class Heavy_Thermic_Lance(StoreItem):
    def __init__(self, qty):
        self.offset = 0x6a
        self.set_item_qty(qty)

### Sonic weapons (gotta go fast!!)

class Sonic_Cannon(StoreItem):
    def __init__(self, qty):
        self.offset = 0x72
        self.set_item_qty(qty)

class Sonic_Cannon_Clip(StoreItem):
    def __init__(self, qty):
        self.offset = 0x74
        self.set_item_qty(qty)


class Sonic_Blasta(StoreItem):
    def __init__(self, qty):
        self.offset = 0x76
        self.set_item_qty(qty)

class Sonic_Blasta_Clip(StoreItem):
    def __init__(self, qty):
        self.offset = 0x78
        self.set_item_qty(qty)

class Sonic_Pistol(StoreItem):
    def __init__(self, qty):
        self.offset = 0x7a
        self.set_item_qty(qty)

class Sonic_Pistol_Clip(StoreItem):
    def __init__(self, qty):
        self.offset = 0x7c
        self.set_item_qty(qty)

class Distuptor_Pulse_Launcher(StoreItem):
    def __init__(self, qty):
        self.offset = 0x7e
        self.set_item_qty(qty)

class Distuptor_Ammo(StoreItem):
    def __init__(self, qty):
        self.offset = 0x80
        self.set_item_qty(qty)

class Thermal_Shok_Launcher(StoreItem):
    def __init__(self, qty):
        self.offset = 0x82
        self.set_item_qty(qty)

class Thermal_Shok_Bomb(StoreItem):
    def __init__(self, qty):
        self.offset = 0x84
        self.set_item_qty(qty)

class Sonic_Pulser(StoreItem):
    def __init__(self, qty):
        self.offset = 0x86
        self.set_item_qty(qty)

class Zrbite(StoreItem):
    def __init__(self, qty):
        self.offset = 0x88
        self.set_item_qty(qty)

class MC_Reader(StoreItem):
    def __init__(self, qty):
        self.offset = 0x8a
        self.set_item_qty(qty)

### Dead Aliens
class Aqautoid(StoreItem):
    def __init__(self, qty):
        self.offset = 0x92
        self.set_item_qty(qty)

class Gill_Man(StoreItem):
    def __init__(self, qty):
        self.offset = 0x94
        self.set_item_qty(qty)

class Lobster_Man(StoreItem):
    def __init__(self, qty):
        self.offset = 0x96
        self.set_item_qty(qty)

class Tasoth(StoreItem):
    def __init__(self, qty):
        self.offset = 0x98
        self.set_item_qty(qty)

class Calcinite(StoreItem):
    def __init__(self, qty):
        self.offset = 0x9a
        self.set_item_qty(qty)

class Deep_One(StoreItem):
    def __init__(self, qty):
        self.offset = 0x9c
        self.set_item_qty(qty)

class Bio_Drone(StoreItem):
    def __init__(self, qty):
        self.offset = 0x9e
        self.set_item_qty(qty)

class Tentaculat(StoreItem):
    def __init__(self, qty):
        self.offset = 0xa0
        self.set_item_qty(qty)

class Triscene(StoreItem):
    def __init__(self, qty):
        self.offset = 0xa2
        self.set_item_qty(qty)

class Hallucinoid(StoreItem):
    def __init__(self, qty):
        self.offset = 0xa4
        self.set_item_qty(qty)

class Xarquid(StoreItem):
    def __init__(self, qty):
        self.offset = 0xa6
        self.set_item_qty(qty)

### Submarine Parts

class Ion_Beam_Acc(StoreItem):
    def __init__(self, qty):
        self.offset = 0xb0
        self.set_item_qty(qty)

class Magnetic_Navigation(StoreItem):
    def __init__(self, qty):
        self.offset = 0xb2
        self.set_item_qty(qty)

class Alien_Sub_Construction(StoreItem):
    def __init__(self, qty):
        self.offset = 0xb4
        self.set_item_qty(qty)

class Alien_Cryogenics(StoreItem):
    def __init__(self, qty):
        self.offset = 0xb6
        self.set_item_qty(qty)

class Alien_Cloning(StoreItem):
    def __init__(self, qty):
        self.offset = 0xb8
        self.set_item_qty(qty)

class Alien_Learning_Arrays(StoreItem):
    def __init__(self, qty):
        self.offset = 0xba
        self.set_item_qty(qty)

class Alien_Implanter(StoreItem):
    def __init__(self, qty):
        self.offset = 0xbc
        self.set_item_qty(qty)

class Examination_Room(StoreItem):
    def __init__(self, qty):
        self.offset = 0xbe
        self.set_item_qty(qty)

class Aqua_Plastics(StoreItem):
    def __init__(self, qty):
        self.offset = 0xc0
        self.set_item_qty(qty)

class Alien_ReAnimation_Zone(StoreItem):
    def __init__(self, qty):
        self.offset = 0xc2
        self.set_item_qty(qty)

class Plastic_Aqua_Armour(StoreItem):
    def __init__(self, qty):
        self.offset = 0xc4
        self.set_item_qty(qty)

class Ion_Armour(StoreItem):
    def __init__(self, qty):
        self.offset = 0xc6
        self.set_item_qty(qty)

class Magnetic_Ion_Armour(StoreItem):
    def __init__(self, qty):
        self.offset = 0xc6
        self.set_item_qty(qty)
