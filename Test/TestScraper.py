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
    
    #using free roam for users, test method specifically for this, just missing the UI part 
    scraper.steam_free_roam_test(-1,['https://steamcommunity.com/id/St4ck'])

def main():
    
    test_steam_scraper() 

if __name__=="__main__":
    main()