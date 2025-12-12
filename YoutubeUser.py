from User import UserData

"""Represents a youtuber user, looks through their account to find:
-their number of subs 
-the people they are subbed to 
-link to their acc"""
class YoutubeUser(UserData): 
    
    def __init__(self, uid : str, sub_list : list[str] ):
        super.__init__(uid,sub_list)