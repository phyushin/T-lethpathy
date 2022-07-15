## todo : change offsets to hex and all related maths
import array as arr
import base_facility as base
from stores import *
class XcomBase():
    
    
    def __init__(self,base_number):
        self.filename = "BASE.DAT" #File name
        self.file_stream = ""
        self.base_number = base_number 
        self.base_size = 0x128 # base size is 296 bytes 
                               # after the name section there is the stores section then the layout and build time for facilities
        ### General Stores 'region'
        self.base_stores_start_offset = 0x10 #Ajax launcher
        self.base_stores_end_offset = 0xc8 # Magnetic ion armour
        
        self.base_layout_offset_start = 0xda
        self.base_layout_build_timer_start_offset = self.base_layout_offset_start + 36
        self.start_offset = self.base_number * self.base_size
        self.end_offset = self.start_offset + self.base_size
        self.layout = self.init_array(6,6,"\xff")
        self.buildtime = self.init_array(6,6,"\xff")
        self.scientists = 0
        self.technicians = 0

    
    def load_base(self, file_stream):
        self.file_stream = file_stream
        self.scientists = self.file_stream[0x123:0x124]
        self.technicians = self.file_stream[0x122:0x123]
        self.store = self.load_store()

    def load_store(self):
        stores = Base_Stores(self.file_stream[self.base_stores_start_offset:self.base_stores_end_offset])
        return stores
    
    def print_base_info(self):
        print("***********************")
        print("Base Info")
        print("***********************")
        self.print_base_name()
        self.print_base_scientist_count()
        self.print_base_technician_count()

    def print_base_name(self):
        #print("offsets\nstart:{}\nend:{}".format(self.start_offset, self.end_offset))
        print("\t\nName:{}".format(self.file_stream[:0xc]))

    def print_base_scientist_count(self):
        print("\tScientists:{}".format(self.scientists )) 

    def print_base_technician_count(self):
        print("\tTechnicians:{}".format(self.technicians)) 

    def init_array(self, x, y, val):
        array = [[val for i in range(x)] for j in range(y)]
        return array
        
    def build_facility(self, x, y, facility, force = False):
        facility.build(self.layout, self.buildtime, x, y, force)
        
    def change_build(self, x, y, val,):
        self.layout[x-1][y-1] = val

    def print_layout(self):
        print("base layout base{0}\noffset:{1}".format(self.base_number,self.start_offset))
        for i in range(6) :
            print (self.layout[i])

    def print_time(self):
        print("build time")
        for i in range(6):
            print(self.buildtime[i])
        
        