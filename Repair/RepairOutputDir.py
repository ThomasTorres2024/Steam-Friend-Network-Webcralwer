"""
@brief Basic repair for saved data and rendered images. I decided to make this because
I messed around with the structure a bit and the program didn't work. 
This structure should work. 

@author Thomas Torres
@date 12/30/25 
"""

import os #check if corresponding folders exist 

def repair_file_directory() -> None: 

    #for scraping 
    
    EXPECTED_ROOT_SAVE_DIRECTORY = "SavedData"
    EXPECTED_STEAM_ROOT_DIRECTORY = EXPECTED_ROOT_SAVE_DIRECTORY+"/Steam"

    #repair file directory for scraping 

    #check if corresponding directories exist 
    if not os.path.isdir(EXPECTED_ROOT_SAVE_DIRECTORY):
        os.mkdir(EXPECTED_ROOT_SAVE_DIRECTORY) 
            
    #check if the specific steam saver is there or not 
    if not os.path.isdir(EXPECTED_STEAM_ROOT_DIRECTORY):
        os.mkdir(EXPECTED_STEAM_ROOT_DIRECTORY)
                
    #check if user directory is there too 
    if not os.path.isdir(EXPECTED_STEAM_ROOT_DIRECTORY+"/Users/"):
        os.mkdir(EXPECTED_STEAM_ROOT_DIRECTORY+"/Users/")
    
    ###############################
    #for repairing render directory 
    ###############################
    
    RENDER_ROOT : str = "Renders"
    
    #add for render folder 
    
    if(not os.path.isdir(RENDER_ROOT)):
        os.mkdir(RENDER_ROOT)
     
    if(not os.path.isdir(RENDER_ROOT+"/Users")):
        os.mkdir(RENDER_ROOT+"/Users")
        
    if(not os.path.isdir(RENDER_ROOT+"/Users/Steam")):
        os.mkdir(RENDER_ROOT+"/Users/Steam")
    
            
