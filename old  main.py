from SteamFriendsWebCrawler import SteamFriendsCrawler
from User import UserData
import networkx
import matplotlib.pyplot as plt
from SteamFriendFileWriter import SteamFriendsFileWriter
from SteamFriendsFileReader import SteamFriendFileReader

def scraper_sample():
    #gets the friends of one person
    ID : str = "coldpaw"
    root_links : list[str] = ["https://steamcommunity.com/id/coldpaw"]
    iterations_per_root_link : int = 1 
    steam_friends_crawler = SteamFriendsCrawler(root_links,iterations_per_root_link)
    users : list[UserData] = steam_friends_crawler.get_user_data_list()


    #get friends of subsequent friends 

    second_root = users[0].get_connections()
    #secondary_friend_crawler = SteamFriendsCrawler(second_root,4)
    secondary_friend_crawler = SteamFriendsCrawler(second_root,len(second_root))
    second_users : list[UserData] = secondary_friend_crawler.get_user_data_list()
    file_writer : SteamFriendsFileWriter = SteamFriendsFileWriter(ID,second_users)
    file_writer.save_file()

def main():
    ROOT : str ="saved_data/amewah.txt"
    reader = SteamFriendFileReader(ROOT)
    print(reader.get_user_data_list())


    # converted : dict[str,str] = {}

    # graph = networkx.Graph()

    # i : int = 0

    # for i in range(len(users)):
    #     user_1 = users[i]

    #     for j in range(i+1,len(users)):
    #         user_2 = users[j]
    #         connections  = determine_intersection(user_1,user_2,converted)
    #         for connection in connections:
    #             graph.add_edge(connection[0],connection[1])

    # i+=1

    # # for user in users:

    # #     user_name : str = user.get_uid()
    # #     connections : list[str] = user.get_connections()

    # #     for connection in connections:
    # #         graph.add_edge(user_name,connection)


    # pos = networkx.spring_layout(graph, k=1.2)
    # networkx.draw(graph, pos, with_labels=True,font_size = 15)
    # plt.show()

def modify_str(url :str) -> str:
    return url.split("/")[4] 

def determine_intersection_three_users(user1 : UserData, user2 : UserData, user3 : UserData):
    pass

def determine_intersection(user1 : UserData,user2 : UserData,converted_vals) -> list[tuple[str,str]]:

    list_1 = user1.get_connections()
    user1_name  : str = user1.get_uid()
    list_2 = user2.get_connections()
    user2_name : str = user2.get_uid()

    if user1_name in converted_vals:
        user1_name  : str = converted_vals[user1_name]
    else:
        modified = modify_str(user1_name)
        converted_vals[user1_name]=modified
        user1_name=modified
    
    if user2_name in converted_vals:
        user2_name  : str = converted_vals[user2_name]
    else:
        modified = modify_str(user2_name)
        converted_vals[user2_name]=modified
        user2_name=modified

    pairs: list[tuple[str,str]] = []
    set_1 = set(list_1)
    set_2 = set(list_2)

    set_intersection = set_1.intersection(set_2)

    for item in set_intersection:

        if item in converted_vals:
            item  : str = converted_vals[item]
        else:
            modified = modify_str(item)
            converted_vals[item]=modified
            item=modified

        pairs.append((user1_name,item))
        pairs.append((user2_name,item))
    
    return pairs
main()
#if __name__ == "__main__":
#    main()
