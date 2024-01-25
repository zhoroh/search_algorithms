class Node:
    def __init__(self,value):
        self.value = value
        self.children = {}
        self.f_distance = float('inf')
        self.g_distance = float('inf')


def get_path(predecessor,root,target):
    path = []
    current_node = target
    while current_node != root:
        if current_node not in predecessor:
            break
        else:
            path.insert(0,current_node)
            current_node = predecessor[current_node]
    path.insert(0,root)
    print("path to goal is", path)


def sort_nodes(nodes:list):
    sorted_list = sorted(nodes,key=lambda x: x[0])
    return sorted_list

def a_star_search(root:Node,target):
    root.f_distance = 0
    root.g_distance = 0
    queue = [(root.f_distance,root)]
    predecessor = {}
    min_distances = {root.value:root.f_distance}


    while queue:
        f_distance ,current_node = queue.pop(0)
        print(current_node.value)
        if current_node.value == target:
            print("distances", min_distances)
            print("predeseccor", predecessor)
            get_path(predecessor,root.value,target)
            return 
        for child in current_node.children:
            new_g_distance = current_node.g_distance + current_node.children[child][0]
            if new_g_distance < child.g_distance:
                child.g_distance = new_g_distance
                child.f_distance = new_g_distance + current_node.children[child][1]
                queue.append((child.f_distance,child))
                predecessor[child.value] = current_node.value
                min_distances[child.value] = child.f_distance



def main():
    # root = Node('A')
    # child_1 = Node('B')
    # child_2 = Node('C')
    # root.children[child_1] = [2,2] # where index 0 is the cost from the root node to the child
    # root.children[child_2] = [3,2] # index 1 is the estimated cost from the current node to target node
    # child_3 = Node('D')
    # child_4 = Node("E")
    # child_5 = Node("F")
    # child_1.children[child_3] = [3,5]
    # child_1.children[child_4] = [1,1]
    # child_2.children[child_5] = [2,0]
    # child_4.children[child_5] = [1,0]

    root = Node('S')
    child_1= Node('A')
    child_2 = Node('B')
    child_3 = Node('C')
    child_4 = Node('D')
    child_5 = Node('F')
    child_6 = Node('E')
    goal_1 = Node('G1')
    goal_2 = Node('G2')
    goal_3 = Node('G3')
    root.children[child_1] = [5,7]
    root.children[child_2] = [9,3]
    root.children[child_4] = [6,6]
    child_1.children[child_2] = [3,3]
    child_1.children[goal_1] = [9,0]
    child_2.children[child_1] = [2,7]
    child_2.children[child_3] = [1,4]
    child_3.children[root] = [6,4]
    child_3.children[goal_2] = [5,0]
    child_3.children[child_5] = [7,6]
    child_4.children[root] = [1,5]
    child_4.children[child_3] = [2,4]
    child_4.children[child_6] = [2,5]
    child_6.children[goal_3] = [7,0]
    child_5.children[goal_3] = [8,0]

    a_star_search(root,"G3")

    # print(root.f_distance)
    # print(child_1.f_distance)
    # print(child_2.f_distance)
    # print(child_3.f_distance)
    # print(child_4.f_distance)
    # print(child_5.f_distance)
    # print(child_6.f_distance)

    # print(goal_1.f_distance)
    # print(goal_2.f_distance)
    # print(goal_3.f_distance)

    





main()

#A* is very very similar to dijiskira search