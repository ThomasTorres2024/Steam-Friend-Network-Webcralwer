from User import UserData

"""Tries to open and read a file. Files are formatted like:
UID,connections
https://steamcommunity.com/id/ImOceano,friend1 link friend2 link friend 3 link etc     
"""
class SteamFriendFileReader:

    #the file name 
    file_name : str     

    """Creates object and then tries to read in file"""
    def __init__(self, file_name : str):
        self.user_data = []
        self.file_name = file_name 

        #try to open file 
        try:

            #go through each line of the file and create a new user object,  add it to the user data list  
            with open(file_name) as file:
                for line in file:
                    split_line : list[str] = line.split(",")
                    root_uid : str = split_line[0]
                    friends : list[str] = split_line[1:-1]

                    self.user_data.append(UserData(root_uid,friends))
                file.close()

        except FileExistsError:
            print(f"ERROR. File at {file_name} does not exist.")

    def get_user_data_list(self)->list[UserData]:
        return self.user_data
    