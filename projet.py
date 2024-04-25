from collections import deque
import numpy as np
import time
import matplotlib.pyplot as plt
from main import generateRandomInstances

# QUESTION 4 ---------------------------------------------------------------
def bfs_robot_bleu(cellules, verticaux, horizontaux): 
    cible = np.where(cellules == -1)
    cible = (cible[0][0], cible[1][0])
    n = len(cellules)  # dimension de grille

    # on récupère la position du robot bleu
    pos = np.where(cellules == 1)
    pos = (pos[0][0], pos[1][0])

    queue = deque([(pos, 0)])
    m = 0
    while queue and m<100000: 
        (x, y), distance = queue.popleft()
        for (dx, dy) in [(0, 1), (0, -1), (-1, 0), (1, 0)]:  # droite, gauche, haut, bas
            tx, ty = x, y
            nx, ny = tx + dx, ty + dy
            if not(0 <= nx < n and 0 <= ny < n):
                continue
            while no_obstacle(tx, ty, dx, dy, cellules, horizontaux, verticaux, n):
                if (nx, ny) == cible:
                    return distance+1, m

                tx, ty = nx, ny
                nx, ny = tx + dx, ty + dy
            else:  # avance jusqu'à la rencontre d'un obstacle
                queue.append(((tx, ty), distance+1))
        m += 1
    return -1, m


def no_obstacle(tx, ty, dx, dy, cellules, horizontaux, verticaux, n): 
    nx, ny = tx + dx, ty + dy
    if not(0 <= nx < n and 0 <= ny < n): return False
    cond_horiz = True if nx == n-1 else nx < n - \
        1 and not ((dx == 1 and horizontaux[tx, ty]) or (
            dx == -1 and horizontaux[tx+dx, ty]))
    cond_verti = True if ny == n-1 else ny < n - \
        1 and not ((dy == 1 and verticaux[tx, ty]) or (
            dy == -1 and verticaux[tx, ty+dy]))
    # soit on a atteint le but soit il n'y a aucun robot sur cette cellule
    no_robot = cellules[nx, ny] in [0, -1]
    no_obstacle = no_robot and cond_horiz and cond_verti
    return no_obstacle

# QUESTION 5 ---------------------------------------------------------------
def bfs_tous_robots(cellules, verticaux, horizontaux, k): 
    cible = np.where(cellules == -1)
    cible = (cible[0][0], cible[1][0])
    n = len(cellules)  # dimension de grille

    # on récupère la position du robot bleu
    queue = deque([])
    config = []
    for robot in range(1, k+1):
        pos = np.where(cellules == robot)
        pos = (pos[0][0], pos[1][0])
        config.append((pos, 0))
    queue.append(config)

    _, m = bfs_robot_bleu(cellules, verticaux, horizontaux)
    mprime = 0
    while queue and mprime < m:  
        robots = queue.popleft()
        for ind in range(k):
            (x, y), distance = robots[ind]
            for (dx, dy) in [(0, 1), (0, -1), (-1, 0), (1, 0)]:  # droite, gauche, haut, bas
                tx, ty = x, y
                nx, ny = tx + dx, ty + dy
                if not(0 <= nx < n and 0 <= ny < n):
                    continue
                while no_obstacle(tx, ty, dx, dy, cellules, horizontaux, verticaux, n):
                    if ind == 0 and (nx, ny) == cible:
                        return distance+1, mprime
                    tx, ty = nx, ny
                    nx, ny = tx + dx, ty + dy
                else:  # avance jusqu'à la rencontre d'un obstacle
                    config = []
                    for i in range(k):
                        if i == ind:
                            config.append(((tx, ty), distance+1))
                        else: 
                            config.append(robots[i])
                    queue.append(config)
        mprime += 1
    return -1, mprime

# QUESTION 7 ---------------------------------------------------------------
def question7():
    n, k = 8, 3
    times_bleu = []
    times_tous = []
    for _ in range(20):
        instance = generateRandomInstances(n, k)
        start = time.time()
        bfs_robot_bleu(*instance)
        end = time.time()
        exec_time = end - start
        times_bleu.append(exec_time)

        start = time.time()
        bfs_tous_robots(*instance, k)
        end = time.time()
        exec_time = end - start
        times_tous.append(exec_time)

    moyenne_bleu = np.mean(times_bleu)
    plt.plot(range(20), times_bleu, marker='o')
    plt.plot(range(20), [moyenne_bleu]*20, label=f"Moyenne {moyenne_bleu}")
    plt.xticks(range(20), range(1, 21))
    plt.title(f"Temps d'exécution sur 20 instances avec n={n} et k={k}, robot bleu")
    plt.ylabel("Temps (en secondes)")
    plt.legend()
    plt.show()

    moyenne_tous = np.mean(times_tous)
    plt.plot(range(20), times_tous, marker='o')
    plt.plot(range(20), [moyenne_tous]*20, label=f"Moyenne {moyenne_tous}")
    plt.xticks(range(20), range(1, 21))
    plt.title(f"Temps d'exécution sur 20 instances avec n={n} et k={k}, tous robots")
    plt.ylabel("Temps (en secondes)")
    plt.legend()
    plt.show()

    # variations de nombre de robots
    times_bleu = []
    times_tous = []
    for i in range(1, 6):
        instance = generateRandomInstances(n, i)
        start = time.time()
        bfs_robot_bleu(*instance)
        end = time.time()
        exec_time = end - start
        times_bleu.append(exec_time)

        start = time.time()
        bfs_tous_robots(*instance, i)
        end = time.time()
        exec_time = end - start
        times_tous.append(exec_time)

    moyenne_bleu = np.mean(times_bleu)
    plt.plot(range(5), times_bleu, marker='o')
    plt.plot(range(5), [moyenne_bleu]*5, label=f"Moyenne {moyenne_bleu}")
    plt.xticks(range(5), range(1, 6))
    plt.title(f"Temps d'exécution sur 5 instances avec n={n} (k varie), robot bleu")
    plt.xlabel("k")
    plt.ylabel("Temps (en secondes)")
    plt.legend()
    plt.show()

    moyenne_tous = np.mean(times_tous)
    plt.plot(range(5), times_tous, marker='o')
    plt.plot(range(5), [moyenne_tous]*5, label=f"Moyenne {moyenne_tous}")
    plt.xticks(range(5), range(1, 6))
    plt.title(f"Temps d'exécution sur 5 instances avec n={n} (k varie), tous robots")
    plt.xlabel("k")
    plt.ylabel("Temps (en secondes)")
    plt.legend()
    plt.show()

# QUESTION 9 ---------------------------------------------------------------
class Node(): 
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.pos = pos
        self.g = self.h = self.f = 0

    def __eq__(self, other):
        return self.pos == other.pos
    
    def __repr__(self):
        return f"[Node, parent={self.parent.pos if self.parent else self.parent}, pos={self.pos}, f={self.f}, g={self.g}, h={self.h}]"

def astar(cellules, verticaux, horizontaux): 
    dim = len(cellules)
    n0_pos = np.where(cellules == 1)
    n0_pos = (n0_pos[0][0], n0_pos[1][0])

    cible_pos = np.where(cellules == -1)
    cible_pos = (cible_pos[0][0], cible_pos[1][0])

    n0 = Node(None, n0_pos)
    end_node = Node(None, cible_pos)

    ouvert = []
    ferme = []
    ouvert.append(n0)
    cmp = 0

    while ouvert:
        current_node = None
        current_node_f = None
        current_node_g = None

        current_index = None
        current_index_f = None
        current_index_g = None

        for ind in range(1, len(ouvert)+1):
            if ind == len(ouvert):
                prec = ouvert[-1]
                courant = ouvert[0]
            else:
                prec = ouvert[ind-1]
                courant = ouvert[ind]

            if prec.f < courant.f:
                current_node_f = prec
                current_index_f = ind-1
            elif prec.g > courant.g:
                current_node_g = prec
                current_index_g = ind-1

        if current_node_f: 
            current_node = current_node_f
            current_index = current_index_f
        elif current_node_g: 
            current_node = current_node_g
            current_index = current_index_g
        else: 
            current_node = ouvert[0]
            current_index = 0

        if current_node == end_node:
            path = []
            current = current_node
            while current:
                path.append(current.pos)
                current = current.parent
            return path[::-1] 

        ouvert.pop(current_index)
        ferme.append(current_node)

        (x, y) = current_node.pos
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tx, ty = x, y 
            nx, ny = tx + dx, ty + dy 
            cout = 0

            while no_obstacle(tx, ty, dx, dy, cellules, horizontaux, verticaux, dim): 
                if (nx, ny) == end_node.pos:
                    tmp = Node(current_node, (nx, ny))
                    path = []
                    current = tmp
                    while current:
                        path.append(current.pos)
                        current = current.parent
                    return path[::-1] 
                
                tx, ty = nx, ny 
                nx, ny = tx + dx, ty + dy 
                cout += 1 

            else:
                if not(0 <= tx < dim and 0 <= ty < dim) or cout == 0: continue 

                m = Node(current_node, (tx, ty))
                m.g = current_node.g + cout # cout = |x-nx| + |y-ny|
                if m == end_node: m.h = 0
                elif m.pos[0] == end_node.pos[0]: m.h = 1
                elif m.pos[1] == end_node.pos[1]: m.h = 1
                else : m.h = 2
                m.f = m.g + m.h

                for ferme_child in ferme:
                    if m == ferme_child: continue

                for noeud in ouvert:
                    if m == noeud and m.g > noeud.g: continue

                ouvert.append(m)
        cmp += 1
    return None