from projet import * 
# exemple de l'énoncé :
test = np.array([[0, 0, 0, 0, 3, 0, 0, 0],
                [0, -1, 2, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]])


# test = np.array([[0, 0, 0, 0, 3, 0, 0, 0],
#                 [0, -1, 2, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 1],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0]])

# test = np.array([[0, 0, 0, 0, 3, 0, 0, 0],
#                 [0, -1, 2, 0, 0, 0, 0, 0],
#                 [1, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 1],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0]])


# test = np.array([[1, 0, 0, 0, 3, 0, 0, 0],
#                 [0, -1, 2, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 1],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0]])


verticaux = np.array([[0, 1, 0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 0, 0]])

horizontaux = np.array([[0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0]])
# cellules, verticaux, horizontaux = generateRandomInstances(8, 3)
distance, m = bfs_robot_bleu(test, verticaux, horizontaux)
print(
    f"Borne supérieure de l'évaluation de la solution optimale : {distance}\n nombre d'itérations : {m}")
distanceprime, mprime = bfs_tous_robots(test, verticaux, horizontaux, 3)
print(
    f"Borne supérieure de l'évaluation de la solution optimale : {distanceprime}\n nombre d'itérations : {mprime}")
print("astar ", astar(test, verticaux, horizontaux))
