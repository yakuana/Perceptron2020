def read_file(file_name):
    node_pairs = []

    with open(file_name) as nodes:
       
        while True: 
            input_nodes = nodes.readline().split(" ")
            input_nodes = input_nodes[1:-1]

            for i in range(len(input_nodes)):
                input_nodes[i] = float(input_nodes[i])
                
            goal_nodes = nodes.readline().split(" ")
            goal_nodes = goal_nodes[1:-1]

            for i in range(len(goal_nodes)):
                goal_nodes[i] = float(goal_nodes[i])

            node_pairs.append([input_nodes, goal_nodes])

            if not goal_nodes:
                break 
    return node_pairs

