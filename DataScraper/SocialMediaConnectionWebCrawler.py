from User import UserData
from bs4 import BeautifulSoup
import requests
from DataScraper.LinkQueue import Node , QueueLink


"""This class will be overriden by child classes. This represents the general behaviors of a social media scraper.
Dec 20th 2024
"""
class SocialMediaConnectionFinder:

    #The links that the program will begin to traverse through in order to find other connections
    root_links : list[str]

    #The list of functions of users
    user_data_list : UserData 

    #queue of links for the site 
    site_queue : QueueLink

    #equal to the number of people we  want to iterate over
    iterations_per_root_link : int 

    #head of the queue 
    queue_head : Node 

    """Sets root links, sets iterations per root link"""
    def __init__(self, root_links : list[str]):

        #set vals 
        self.root_links = root_links

        self.iterations_per_root_link = len(root_links)

        #convert list of links to root 
        self.site_queue = QueueLink(root_links)
        self.queue_head = self.site_queue.get_head()

        #the list of user data 
        self.user_data_list : UserData = []
            
        #processes the links 
        self.process_links()

    """Returns the list of user data list"""
    def get_user_data_list(self) -> list[UserData]:
        return self.user_data_list

    """Abstract function which is overriden by a child class which processes """
    def process_site_uniquely(self, souped_request_info : BeautifulSoup, found_links : list[str]) -> list[str]:
        pass 
    
    """Abstract function which modifies a link. Any time a link is processed, it goes through here."""
    def modify_link(self,link : str) -> str:
        pass 
    
    """Version for processing one person"""
    def process_links_old(self) -> None:
        total : set[str] = set()
        found_links : list[str]= []

        #we want to iterate through a user's friends, and then the friends's of the user's friends, and then save them
        

        #
        while self.queue_head and self.iterations_per_root_link > i:
            #find all the a tags on the steam site 
            link = self.modify_link(self.queue_head.get_val())
            html_request_info = requests.get(link)
            souped_request_info : BeautifulSoup = BeautifulSoup(html_request_info.text)

            #processes site links 
            self.process_site_uniquely(souped_request_info,found_links)
            
            #add to list of users
            self.user_data_list.append(UserData(link,found_links))

            #update the header and iterator 
            self.queue_head = self.queue_head.get_next()
            i+=1

            #add new links to queue,  reset found links
            self.site_queue.add_links(found_links)
            total =  total.union(set(found_links))
            found_links = []

            if self.queue_head:
                print(f"{self.queue_head.get_val()},{i+1}")
            else:
                print("end")

        print(f"Number of friends: len(total)")
        return found_links

    """Abstract function which processes links"""
    def process_links(self) -> None:
        total : set[str] = set()
        found_links : list[str]= []

        #find all the a tags on the steam site 
        link = self.modify_link(self.queue_head.get_val())
        html_request_info = requests.get(link)
        souped_request_info : BeautifulSoup = BeautifulSoup(html_request_info.text)
        #processes site links 
        self.process_site_uniquely(souped_request_info,found_links)
        new_queue: QueueLink = QueueLink(found_links)  
        new_queue_head = new_queue.get_head() 
           
        i :int  = 1
        #we want to iterate through a user's friends, and then the friends's of the user's friends, and then save them
        while new_queue_head:
            #find all the a tags on the steam site 
            link = self.modify_link(new_queue_head.get_val())
            html_request_info = requests.get(link)
            souped_request_info : BeautifulSoup = BeautifulSoup(html_request_info.text)

            #processes site links 
            self.process_site_uniquely(souped_request_info,found_links)
            
            #add to list of users
            self.user_data_list.append(UserData(link,found_links))

            #update the header and iterator 
            new_queue_head = new_queue_head.get_next()
            i+=1

            #add new links to queue,  reset found links
            self.site_queue.add_links(found_links)
            total =  total.union(set(found_links))
            found_links = []

            if new_queue_head:
                print(f"{new_queue_head.get_val()},{i+1}")
            else:
                print("end")

        print(f"Number of friends: len(total)")

