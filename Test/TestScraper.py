"""
@author Thomas Torres
@date 12-29-25
@brief Test function for the scraper library 
"""

from DataScraper.DataScrape import ScrapeData 
from Calculation.MathAndVisualizer  import MathRendering

"""Used for testing the steam scraper on some 
user functions, there's one for users """
def test_steam_scraper():
    scraper : ScrapeData =ScrapeData() 
    
    #using free roam for users 
    scraper.steam_free_roam(-1)

def main():
    
    test_steam_scraper() 

if __name__=="__main__":
    main()