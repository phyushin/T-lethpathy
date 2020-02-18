#

#Todo:
## file ops
## editing soldiers details - this will be tricky xD
##
from base import XcomBase as XcomBase
from stores import Zrbite

base_file_stream = ""
base_size = 0x128
base_count = 7

def load_basefile(path):
    base = ""
    with open(path + "\\BASE.DAT", 'rb') as base_file:
        base =  base_file.read()
    base_file.close()
    print ("Base file loaded")
    return base

def main():
    print("X-Com Save Game Editor - Name Subject to Change xD")
    test_save_path = "E:\\Blog\\XCOM SaveGameEditor\\Games\\X-COM Terror from the Deep\\TFD\\GAME_1"
    base_file = load_basefile(test_save_path)
    Xc = [XcomBase(i) for i in range(base_count+1)]
    

    for base in Xc:
        base.load_base(base_file[base.start_offset:base.end_offset])
       # base.print_base_name()
       # base.print_base_scientist_count()
       # base.print_base_technician_count()
        
    store = Xc[0].load_store()
    store.print_stores()
    store.set_item_qty(Zrbite(0xff))
       
    store.print_stores()

    


       
       
    
if __name__ == "__main__":
    main()