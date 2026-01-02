"""
@author Thomas Torres
@date 12-30-25

@brief Entry point for steam webscraping and 
"""

from DataScraper.DataScrape import ScrapeData 
from Calculation.MathAndVisualizer  import MathRendering
from Repair import RepairOutputDir

"""True main"""
def main():
    
    #before any execution ensure that file system for saving is intact
    #i made some changes to the program so I made a method to handle this
    RepairOutputDir.repair_file_directory()
    
    HELP_STRING : str  ="1. Scrape Data\n2. Math/Rendering\n3. Help\n4. Stop\n"
    print(HELP_STRING)
    
    mode_str : str = input("Mode: ")
    mode_str=mode_str.strip().lower()
    
    #option menu 
    while mode_str != "stop" or mode_str != "0" or mode_str !="4" or mode_str !="4." :
        
        #help methods entry point
        if(mode_str=="help" or mode_str == "3" or mode_str=="3."):
            print(HELP_STRING)
        
        #scrape methods entry point
        elif(mode_str=="scrape" or mode_str == "1" or mode_str=="1."):
            scraper : ScrapeData =ScrapeData() 
            scraper.loop_over_decision_menu()
        
        #render/math methods entry point 
        elif(mode_str=="rendering" or mode_str == "math" or mode_str == "2" or mode_str=="2."):
            math_and_vis : MathRendering = MathRendering()
            math_and_vis.loop_over_decision_menu()
        elif(mode_str=="quit" or mode_str=="4"):
            break 
        else:
            print(f"ERROR. Invalid command. To see valid commands type help.")
            
        #get input again
        mode_str : str = input("Mode: ")
        mode_str=mode_str.strip().lower()

if __name__ == "__main__":
    main()