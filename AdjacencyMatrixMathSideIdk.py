from CSVDataFileFileReader import DataFileReader
from User import UserData
import pprint
import networkx
import matplotlib.pyplot as plt
import numpy as np 
def main():
    FILE_NAME_PART : str = "amewah"
    DATA_FILE_NAME : str = f"saved_data/{FILE_NAME_PART}.txt" 
    social_media_datafile  : DataFileReader =  DataFileReader(DATA_FILE_NAME)
    user_name_to_user_object : dict[str,UserData] = social_media_datafile.get_username_to_object_hash()
    user_name_to_count  : dict[str,int] = social_media_datafile.get_user_to_num_hash()
    num_to_user : dict[int,str] = social_media_datafile.get_num_to_user_hash()
    user_list : list[UserData] = social_media_datafile.get_user_list()
    out : list[list[int]] =  create_n_n_null_matrix(len(user_list))

    graph = networkx.Graph()
    plot_adjacency_of_all_friends_except_main_friend(user_list,user_name_to_user_object, graph,user_name_to_count,out)
    pos = networkx.spring_layout(graph, k=1.2)
    networkx.draw(graph, pos, with_labels=True,font_size = 15)
    plt.show()
    np.savetxt('data.csv', out, delimiter=',') 
    #pprint.pprint(out)
    render_name : str = "50AmewahFriends"
    FILE_SAVE_DIR : str = f"saved_adjacency_matrices/{FILE_NAME_PART}AdjacencyMatrix.csv"
    save_data(out,user_list,FILE_SAVE_DIR)

def save_data(out, users : list[UserData] ,file_name : str):
    with open(file_name,'w') as file:
        header : list[str] = []
        header_str : str = ","
        for i in range(len(users)):
            user : UserData = users[i]
            uid : str  =  user.get_uid()
            header.append(user.get_uid())

            #last case scenario 
            if i+1 == len(users):
                header_str+=uid
            else:
                header_str+=f"{uid},"
        file.write(header_str+"\n")
        print(header_str)
        print(len(out))
        print(len(header_str))
        for i in range(len(out)):
            new_row : str = header[i]+","
            for j in range(len(out[i])):
                to_str_vers : str = str(out[i][j])
                if j+1 != len(out[i]):
                    new_row+=f"{to_str_vers},"
                else:
                    new_row+=to_str_vers
            file.write(new_row+"\n")
        
        file.close()
        

        

def create_n_n_null_matrix(n : int) -> list[list[int]]:
    out : list[list[int]] = []

    for i in range(n):
        sub_arr : list[int] = []
        for j in range(n):
            sub_arr.append(0)
        out.append(sub_arr)

    return out
    

"""Hard to name this one. We consider the friends of 1 user called X. We will not
consider X. All of the users of X's friends are in Y. Consider for all k in Y, 
the friendlist of k is G, we are graphing the intersection of G and Y."""
def plot_adjacency_of_all_friends_except_main_friend(user_list : list[UserData],user_name_to_user_object : dict[str,UserData],graph,user_name_to_count:dict[str,int],out:list[list[int]]):
    for i in range(len(user_list)):
    #for user in user_list:
        user = user_list[i]
        user_connections : list[str] = user.get_connections()
        user_name : str = user.get_uid()
        user_position : int = user_name_to_count[user_name]
        print(f"{i+1}. Processing: {user_name}")
        for friend in user_connections:
            if friend in user_name_to_user_object:
                friend_pos : int = user_name_to_count[friend]
                out[user_position][friend_pos] = 1 
                out[friend_pos][user_position] = 1 
                graph.add_edge(friend,user_name)


if __name__ == "__main__":
    main()