class Node:
    def __init__(self,key):
        self.key = key
        self.children = {}
        self.distance = float('infinity')


def sort_nodes(nodes:list):
    sorted_list = sorted(nodes,key=lambda x: x[0])
    return sorted_list

def dijiskira(root:Node):
    root.distance = 0
    queue = [(root.distance,root)]
    predecessor = {}
    min_distances = {root.key:root.distance}
    while queue:
        distance ,current_node = queue.pop(0)
        for child in current_node.children:
            new_distance = current_node.distance + current_node.children[child]
            if new_distance < child.distance:
                child.distance = new_distance
                min_distances[child.key] = child.distance
                queue.append((child.distance,child))
                predecessor[child.key] = current_node.key
        queue = sort_nodes(queue)

    return min_distances,predecessor

def ucs(root,target):
    min_distances, predecessor = dijiskira(root)
    print(min_distances)
    path = []
    print(predecessor)
    current_node = target
    while current_node != root.key:
        if current_node not in predecessor:
            break
        else:
            path.insert(0,current_node)
            current_node = predecessor[current_node]
    path.insert(0,root.key)

    print(path)


    
            




def main():
    root = Node('a')
    child_1 = Node('b')
    child_2 = Node('c')
    root.children[child_1] = 6
    root.children[child_2] = 3
    child_4 = Node('d')
    child_5 = Node('e')
    child_1.children[child_2] = 1
    child_1.children[child_4] = 2
    child_2.children[child_1] = 4
    child_2.children[child_4] = 8
    child_2.children[child_5] = 2
    child_4.children[child_5] = 9
    child_5.children[child_4] = 7
    ucs(root,'e')




main()