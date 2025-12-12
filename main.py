from DataScraper.DataScrape import ScrapeData 
from Calculation.MathAndVisualizer  import MathRendering

"""True main"""
def main():
    mode_str : str = input("Mode: ")
    mode_str=mode_str.strip().lower()
    HELP_STRING : str  ="1. Scrape Data\n2. Math/Rendering\n3. Help\n4. Stop\n"
    print(HELP_STRING)
    while mode_str != "stop" or mode_str != "0":
        if(mode_str=="help"):
            print(HELP_STRING)
        elif(mode_str=="scrape"):
            scraper : ScrapeData =ScrapeData() 
            scraper.loop_over_decision_menu()
        elif(mode_str=="rendering" or mode_str == "math"):
            math_and_vis : MathRendering = MathRendering()
            math_and_vis.loop_over_decision_menu()
        else:
            print(f"ERROR. Invalid command. To see valid commands type help.")
        #get input again
        mode_str : str = input("Mode: ")
        mode_str=mode_str.strip().lower()

"""Check if the name is main"""
if __name__ == "__main__":
    main()