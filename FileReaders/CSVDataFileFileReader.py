from User import UserData 
from FileReaders.AbstractDataFileReader import AbstractFileReader
class DataFileReader(AbstractFileReader):

    def __init__(self,file_name:str):
        super().__init__(file_name)
        self.read_in_file_data()

    """Read in file data to user list, user to num haash, num to user hash,
    username to user object hash"""
    def read_in_file_data(self):
        with open(self.file_name, 'r') as file:
            count : int = -1 
            #go through file and create user for each row 
            for line in file: 
                if count != -1:
                    line_split_str : list[str] = line.split(",")
                    id_split : list[str] = line_split_str[0].split("/")
                    user_uid : str = id_split[3]+"/"+id_split[4]
                    all_friends : list[str] = line_split_str[1:-1]
                    if(len(all_friends)!=0):
                        new_user : UserData = UserData(user_uid,all_friends)
                    
                    print(f"New user created at: {count}, UID: {user_uid}")
                    self.username_to_num_hash[user_uid]=count
                    self.username_to_user_object_hash[user_uid]=new_user
                    self.num_to_username_hash[count]=user_uid
                    self.users_list.append(new_user)
                count+=1
            file.close()