from AdjacencyMatrixReader import AdjacencyMatrixFileReader
file_name : str = "saved_adjacency_matrices/50AmewahFriends.csv"
read_file  = AdjacencyMatrixFileReader(file_name)
adjacency_matrix = read_file.get_adjacency_matrix()
print(adjacency_matrix)