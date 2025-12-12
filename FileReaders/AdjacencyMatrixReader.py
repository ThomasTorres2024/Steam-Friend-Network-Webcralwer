from AbstractDataFileReader import AbstractFileReader
from User import UserData
"""Reads in Adjacency Matrices"""

import numpy as np 

class AdjacencyMatrixFileReader(AbstractFileReader):

    adjacency_matrix : list[list[int]]

    def __init__(self,file_name:str):
        super().__init__(file_name)
        self.adjacency_matrix=[]
        self.read_in_file_data()

    def generate_adjacency_matrix(self,length:int):
        self.adjacency_matrix=[]
        for i in range(length):
            sub_list : list[int] = []
            for j in range(length):
                sub_list.append(0)
            self.adjacency_matrix.append(sub_list)
        print(self.adjacency_matrix)
    
    def get_adjacency_matrix(self):
        return self.adjacency_matrix
    
    def set_adjacency_matrix(self,new_matr):
        self.adjacency_matrix=new_matr

    """Processes the header, then gets connections for each row"""
    def read_in_file_data(self):
        with open(self.file_name,'r') as file:
            
            count : int = -1
            for line in file:
                #process header and create adjacency matrix 
                if count == -1:
                    header = line.split(",")[1:]
                    header[-1]=header[-1][0:-1]
                    subcount : int= 0
                    for name in header:
                        #fill both dicts 
                        self.username_to_num_hash[name]=subcount
                        self.num_to_username_hash[subcount]=name
                        subcount+=1
                    #create adjcency matrix now that we know the count size 
                    self.generate_adjacency_matrix(subcount)
                    print(self.username_to_num_hash)
                    print(self.num_to_username_hash)
                #if not header process normally
                else:
                    split_line = line.split(",")
                    uid:str=split_line[0] 
                    connections : list[str] = []
                    i : int= self.username_to_num_hash[uid]

                    #go through  0,s and  1s, if 1 there is a connection
                    #graph is synmmetric so makes it ezer to do 
                    for j in range(1,len(split_line)):
                        if(int(split_line[j])==1):
                            self.adjacency_matrix[i][j]=1
                            self.adjacency_matrix[j][i]=1
                            connections.append(self.num_to_username_hash[j])

                count+=1 

            file.close()