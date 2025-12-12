from User import UserData

"""Saves scraped data in files. To use, create an object using the fields appropriately, and then use the save file
command. Dec 20 2024"""
class SteamFriendsFileWriter:

    """Initialized fields and create object"""
    def __init__(self,directory : str, data : list[UserData]):
        self.HEADER = "uid,connections"
        self.data = data 
        self.directory = directory 

    """Refines a list of strings into a single string for being saved.
    Called by the program when saving the array """
    def refine_list_for_saving(self, list_names : list[str]) -> str:
        out_str:str = ""
        for name in list_names:
            split_name : list[str] = name.split("/")
            actual_name = split_name[3]+"/"+split_name[4]
            out_str+=f"{actual_name},"
        return out_str

    """Puts file into coherent format and then saves it. ATM only does this for UIDs and connections with other UIDs"""
    def save_file(self):
        #begin with the header 
        out_str : str = "UID,Connections\n"

        #go through every use in the data and then add them to the file string 
        for user in self.data:
            print(user)
            uid : str = user.get_uid()

            #get the list of strings, format them so that they can be saved in a file 
            connections_str : str = self.refine_list_for_saving(user.get_connections())   
            out_str+=f"{uid},{connections_str}\n"
            print(out_str)
        
        #save file where directory specifies 
        with open(self.directory,'w') as file:
            file.write(out_str)
            file.close() 