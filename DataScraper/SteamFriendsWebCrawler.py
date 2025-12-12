from DataScraper.SocialMediaConnectionWebCrawler import SocialMediaConnectionFinder
class SteamFriendsCrawler(SocialMediaConnectionFinder):

    """Constructor for a steamfriends webcrawler"""
    def __init__(self, root_links : list[str]):
        #abstract constructor 
        super().__init__(root_links)

    """Overrides processing and specifies it for Steam Friends Specifically using the fact we
    can get other steam friends from: https://steamcommunity.com/id/example_id/friends"""
    def process_site_uniquely(self, souped_request_info, found_links):
        #call parent class vers  
        super().process_site_uniquely(souped_request_info, found_links)

        #get every link within the page 
        friend_sections = souped_request_info.find_all("a",{"class":"selectable_overlay"})
        for friend in friend_sections:
            found_links.append(friend.get("href"))
    
    """Takes the site link and modifies it so that we are accessing steam friends each time"""
    def modify_link(self,site_link :str) -> str:
        #obligatory super call
        super().modify_link(site_link)

        return f"{site_link}/friends"