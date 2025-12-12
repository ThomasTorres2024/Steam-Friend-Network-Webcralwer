from User import UserData 
import numpy as np 
class AbstractFileReader:

    user_list : list[UserData]
    username_to_num_hash : dict [str,int]
    num_to_username_hash  : dict[int,str]
    username_to_user_object_hash : dict[str,UserData]

    """Reads in file data into user list user to num hash user to object variables"""
    def __init__(self, file_name : str):
        self.users_list = []
        self.username_to_num_hash = {}
        self.num_to_username_hash = {}
        self.username_to_user_object_hash = {}
        self.file_name = file_name


    """Returns hash of str to userdata"""
    def get_username_to_object_hash(self)->dict[str,UserData]:
        return self.username_to_user_object_hash

    """Returns dict of count to user hash"""
    def get_num_to_user_hash(self)->dict[int,str]:
        return self.num_to_username_hash

    """Returns the user to num hash"""
    def get_user_to_num_hash(self)->dict[str,int]:
        return self.username_to_num_hash

    """Sets the list of users"""
    def set_user_list(self,new_user_list : list[UserData]) -> None:
        if(isinstance(new_user_list),list):
            self.user_list=new_user_list
        else:
            raise ValueError("ERROR. Object is not a list")
    
    """Returns the list of users"""
    def get_user_list(self) -> list[UserData]:
        return self.users_list

    """This method is to be overided in child classes. Read in file data to user list, user to num haash, num to user hash,
    username to user object hash."""
    def read_in_file_data(self):
        pass 