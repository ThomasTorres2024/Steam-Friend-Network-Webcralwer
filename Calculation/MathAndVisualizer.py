"""To use, first create the function and initialize any relevant variables. Next, call the decision loop."""
from DecisionLoopConsole import ConsoleDecisionLoop
from User import UserData
from DataScraper.SteamFriendsWebCrawler import  SteamFriendsCrawler
from DataScraper.SteamFriendFileWriter import SteamFriendsFileWriter 
from FileReaders.CSVDataFileFileReader import DataFileReader
import time 
import os 
import networkx
import matplotlib.pyplot as plt

"""A decision menu driven by user commands in console. Unifies different functions related to scraping data
from steam profiles. 
Dec 20th 2024"""
class MathRendering(ConsoleDecisionLoop):

    user_list : list[UserData]

    #where all files are saved to
    ROOT_OUT_DIR : str 

    """Create object initialize vals"""
    def __init__(self):
        super().__init__()
        self.user_list=[]
        self.ROOT_FILE_DIR = "SavedData/Steam/"

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
                     "1":self.list_steam_files,
                     "2":self.visualize_persons_own_friendgroup}

    def get_uids(self)->list[list[UserData]]:
        input_str = ""
        people :list[str] =[]
        while input_str != "-1":
            input_str= input("Enter file name: ")
            if input_str!= "-1":
                people.append(input_str)

        #people : list[str] =  ["id-ijustshovedanukeupmypussy-2024-12-24 07-35-47.csv"]
        ROOT_INSTANCE : str = self.ROOT_FILE_DIR+"Users/"
        all_users  : list[list[UserData]] = []

        #read in file list and append
        for person in people:
            file_name : str = ROOT_INSTANCE+person
            file_reader_instance : DataFileReader = DataFileReader(file_name)
            all_users.append(file_reader_instance.get_user_list())
        
        return all_users

    def visualize_persons_own_friendgroup(self):
        users : list[list[UserData]] = self.get_uids()[0]
        friends : set = set()
        graph = networkx.Graph()
        for user in users:
            friends.add(user.get_uid())
        
        for i in range(len(users)):
            user : UserData  = users[i]
            connections : list[str] = user.get_connections()
            for connection in connections:
                if connection in friends:
                    graph.add_edge(connection,user.get_uid())
        # Create a color map
        cmap = plt.cm.get_cmap('viridis')
        degrees = dict(graph.degree())

        print(degrees)

        # Assign colors to nodes based on degree
        node_colors = [cmap(degrees[node] / max(degrees.values())) for node in graph.nodes()]
        pos = networkx.spring_layout(graph, k=1.2)
        networkx.draw(graph, pos, with_labels=True,font_size = 10,node_color=node_colors)
        plt.show() 


    def visualize_union_friends(self):
        pass 

    """Override help command filll with commands for this particular class"""
    def help_command(self):
        super().help_command()
        print(f"0. Help\n1. List Steam Files.\n2. Render Existing Adjacency Matrices\n-1. Stop\n2. Visualize Own Friendslists")
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
    #Data Manipulation Functions
    ###############################################################

    """Goes through the files at a specified directory and lists them user selects which 
    files they want to go through"""
    def list_steam_files(self):

        user_input : str = input("1. Adjacency Matrices.\n2. User Data\n-1. Quit\n: ")

        while(user_input!="-1"):

            if(user_input == "1" or user_input =="2"):
                root_particular : str = self.ROOT_FILE_DIR
                if(user_input=="1"):
                    root_particular+="AdjacencyMatrices"
                else:
                    root_particular+="Users"

                print(root_particular)
                list_dir : list[str] = os.listdir(root_particular)

                print("*"*40)
                for i in range(len(list_dir)):
                    print(f"{i+1}.{list_dir[i]}")
                print("*"*40)
            
            #if quit
            elif user_input !="-1":
                print("ERROR. Must enter an expected number.")
            user_input : str = input("1. Adjacency Matrices.\n2. User Data\n-1. Quit\n: ")

    """Takes link from user, feed list of links into steam scraper """
    def steam_scrape(self):
        list_links  : list[str] = self.console_get_link_one_by_one()
        for link in list_links:
            try: 
                steam_friends_crawler = SteamFriendsCrawler([link])
                self.user_list : list[UserData] = steam_friends_crawler.get_user_data_list()
                for user in list_links:
                    self.save_file(user)
            except  Exception as e:
                print(f"ERROR. Unexpected error ocurred: {e}")


    
    """Generates name for a file and saves userdata object to the file's generated name location"""
    def save_file(self,uid : str):
        print("Trying to save file:")
        for user in self.user_list:
           file_name : str = self.generate_save_file_name(uid)
           steam_friend_file_writer : SteamFriendsFileWriter = SteamFriendsFileWriter(file_name,[user])
           steam_friend_file_writer.save_file()
           print(f"File saved to: {file_name}")
         

    """Takes in a stem URL which either ends in /id/example_id or profiles/123456.. example  number, 
    so we have to split this and get the current time and root and add this together to make the out file directory"""
    def generate_save_file_name(self, user_url : str) ->str:
        split_url :str= user_url.split("/")
        uid_str : str = split_url[3]+"-"+split_url[4]+"-"
        current_time = time.strftime("%Y-%m-%d %H-%M-%S")
        return self.ROOT_OUT_DIR+uid_str+current_time+".csv"
