"""Represents a user"""
class UserData:

    #unique user id 
    uid  : str 

    #connections meaning their friends, followers, etc, corresponds to a list of other User Objects
    connections : list

    """Create a user object"""
    def __init__(self, uid : str,connection_list):
        #Set UID and Link
        self.uid = uid 

        #set connections to be brackets 
        self.set_connections(connection_list)
    
    #Setters

    """Change the list of connections with a new list of uids"""
    def set_connections(self, new_connections : list[str]) -> None: 
        self.connections=new_connections
    
    #Other Mutators 

    """Adds new link to the list of links """
    def add_connection(self,new_link : str) -> None:
        self.connections.append(new_link)

    #Getters

    """Returns the list of connections"""
    def get_connections(self) -> list[str]:
        return self.connections
    
    """Returns user ID"""
    def get_uid(self) -> str:
        return self.uid

    def __str__(self)->str:
        return f"UID:f{self.uid}\n"