"""To use, first create the function and initialize any relevant variables. Next, call the decision loop."""
from DecisionLoopConsole import ConsoleDecisionLoop
from User import UserData
from DataScraper.SteamFriendsWebCrawler import  SteamFriendsCrawler
from DataScraper.SteamFriendFileWriter import SteamFriendsFileWriter 
import time 
from DataScraper.LinkQueue import QueueLink

"""A decision menu driven by user commands in console. Unifies different functions related to scraping data
from steam profiles. 
Dec 20th 2024"""
class ScrapeData(ConsoleDecisionLoop):

    user_list : list[UserData]

    #where all files are saved to
    ROOT_OUT_DIR : str 

    """Create object initialize vals"""
    def __init__(self):
        super().__init__()
        self.user_list=[]
        self.ROOT_OUT_DIR = "SavedData/Steam/"

    #######################################
    #Getters and Setters
    #######################################
    
    """Gets current user list"""
    def get_user_list(self):
        return self.user_list
    
    """Sets new user list"""
    def set_user_list(self,new_list : list[str]):
        self.user_list=new_list

    #######################################
    #Menu functions etc
    #######################################

    """Fill menu with choice options"""
    def create_menu(self):
        super().create_menu()
        self.menu = {"0":self.help_command,
                     "1":self.steam_scrape,
                    #  "2":self.steam_free_roam}
                    #here the roam function is so we can feed in other params for CLi 
                    "2":self.intermediary_roam_function,
                    }

    """Override help command filll with commands for this particular class"""
    def help_command(self):
        super().help_command()
        print(f"0. Help\n1. Steam Scraper For Individual Profiles.\n-1. Stop\n2. Free Roam Scraper With No Endpoint\n3. Youtube Account Scraper\n 4. Youtube Video Scraper\n 5. Youtube Video Roamer")
        print("*"*40)

    """Common to all scrapers"""
    def console_get_link_one_by_one(self) -> list[str]:
        link : str = input("Provide the link to scrape, -1 to stop:")
        list_links : list[str] = []
        while(link != "-1"):
            list_links.append(link)
            link : str = input("Provide the link to scrape, -1 to stop:") 
        print("*"*40)
        print("Complete, list of links entered: ")
        print(list_links)     
        print("*"*40)
        return list_links

    ###############################################################
    #Data Manipulation Functions for Steam 
    ###############################################################

    """Takes link from user, feed list of links into steam scraper """
    def steam_scrape(self):
        list_links  : list[str] = self.console_get_link_one_by_one()
        for link in list_links:
            try: 
                steam_friends_crawler = SteamFriendsCrawler([link])
                user_list : list[UserData] = steam_friends_crawler.get_user_data_list()
                for user in list_links:
                    self.save_file(user,user_list)
            except  Exception as e:
                print(f"ERROR. Unexpected error ocurred: {e}")
    
    """Generates name for a file and saves userdata object to the file's generated name location"""
    def save_file(self, uid : str,users : list[UserData]):
        file_name : str = self.generate_save_file_name(uid)
        steam_friend_file_writer : SteamFriendsFileWriter = SteamFriendsFileWriter(file_name,users)
        steam_friend_file_writer.save_file()
        print(f"File saved to: {file_name}")

    
    """"This is an intermediary function to make this compatible with the menu and its implementation calling
    one of the options with no arguments, it calls this instead. """
    def intermediary_roam_function(self):
        
        depth_entry_incorrect : bool = True 
        depth : int = 0 
        while(depth_entry_incorrect):
            print("*"*80)
            temp : str = input("\nDepth for Roam (for no depth -1): ")
            
            try:
                depth = int(temp)    
                depth_entry_incorrect=False 
            except TypeError:
                print("ERROR. Depth value must be numeric.\n")
             
        #at last execute the roam function with appropriate depth 
        self.steam_free_roam(depth)
    
    """Takes root link and continually iterates over friends
    TODO Multithread this function, this should not be singled threaded. 
    Add an optional depth parameter, otherwise the traversal might blowup.
    """
    def steam_free_roam(self, depth : int):
        
        #get links that user provided 
        list_links  : list[str] = self.console_get_link_one_by_one()
        queue : QueueLink = QueueLink(list_links)
        queue_head  = queue.get_head()

        #keeps track of all of the different links that have been encountered 
        processed : set = set()
        
        #only consider depth when value is positive 
        consider_depth : bool = False 
        if(depth > 0):
            consider_depth=True 
        
        loop_start = time.time()
        
        #iterate over the entire queue, and find the assosciated friends of an individual 
        while queue_head:
            
            
            if(consider_depth and (depth <= 0)):
                break  
            
            link : str = queue_head.get_val()
            if link not in processed:
                
                start=time.time()  
                
                processed.add(link)
                
                # print(f"User: link")
                steam_friends_crawler = SteamFriendsCrawler([link])
                user_list : list[UserData] = steam_friends_crawler.get_user_data_list()
                self.save_file(link,user_list)
                
                #this was useful for debugging, but it's really cluttered here otherwise. 
                
                # for user in user_list:
                #     print(user.get_uid())
                #     queue.add_links([user.get_uid()])

                end = time.time()
            
                print(f"Completed: {link} in {start-end} seconds")
            
            #stop searching  if queue is over 
            if queue_head.get_next():
                queue_head=queue_head.get_next()
            else:
                queue_head=None 
            
            #each iteration for a member of the set results in the total depth
            #going down 
            if(consider_depth):
                depth-=1
                
        loop_end=time.time()
        print(f"Completed iterating over the entire friend network in: {loop_start-loop_end}")
        
    """@brief Fundamentally the same function as the steam free roam function, 
    the only difference here is that this is not intended to use any I/O from the users 
    
    Takes root link and continually iterates over friends
    TODO Multithread this function, this should not be singled threaded. 
    Add an optional depth parameter, otherwise the traversal might blowup.
    """
    def steam_free_roam_test(self, depth : int, list_links : list[str]):
        
        #get links that user provided 
        # list_links  : list[str] = self.console_get_link_one_by_one()
        queue : QueueLink = QueueLink(list_links)
        queue_head  = queue.get_head()

        #keeps track of all of the different links that have been encountered 
        processed : set = set()
        
        #only consider depth when value is positive 
        consider_depth : bool = False 
        if(depth > 0):
            consider_depth=True 
        
        loop_start = time.time()
        
        #iterate over the entire queue, and find the assosciated friends of an individual 
        while queue_head:
            
            
            if(consider_depth and (depth <= 0)):
                break  
            
            link : str = queue_head.get_val()
            if link not in processed:
                
                start=time.time()  
                
                processed.add(link)
                
                # print(f"User: link")
                steam_friends_crawler = SteamFriendsCrawler([link])
                user_list : list[UserData] = steam_friends_crawler.get_user_data_list()
                self.save_file(link,user_list)
                
                #this was useful for debugging, but it's really cluttered here otherwise. 
                
                # for user in user_list:
                #     print(user.get_uid())
                #     queue.add_links([user.get_uid()])

                end = time.time()
            
                print(f"Completed: {link} in {start-end} seconds")
            
            #stop searching  if queue is over 
            if queue_head.get_next():
                queue_head=queue_head.get_next()
            else:
                queue_head=None 
            
            #each iteration for a member of the set results in the total depth
            #going down 
            if(consider_depth):
                depth-=1
                
        loop_end=time.time()
        print(f"Completed iterating over the entire friend network in: {loop_start-loop_end}")
        
        
    """Takes in a stem URL which either ends in /id/example_id or profiles/123456.. example  number, 
    so we have to split this and get the current time and root and add this together to make the out file directory"""
    def generate_save_file_name(self, user_url : str) ->str:
        split_url :str= user_url.split("/")
        uid_str : str = split_url[3]+"-"+split_url[4]+"-"
        current_time = time.strftime("%Y-%m-%d %H-%M-%S")
        return self.ROOT_OUT_DIR+"Users/"+uid_str+current_time+".csv"

    ######################################################
    #YOUTUBE SCRAPER FUNCTIONS
    ######################################################

    def scrape_user(self):  
        pass 