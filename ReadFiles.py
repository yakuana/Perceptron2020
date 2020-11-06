def read_file(file_name):
    node_pairs = []

    with open(file_name) as nodes:
        count = 0 
       
        while count < 6: 
            input_nodes = nodes.readline().split(" ")
        
            input_nodes.remove('(')
            input_nodes.remove(')\n')

            for i in range(len(input_nodes)):
                input_nodes[i] = float(input_nodes[i])
                
            goal_nodes = nodes.readline().split(" ")
            goal_nodes.remove('(')
            goal_nodes.remove(')\n')

            for i in range(len(goal_nodes)):
                goal_nodes[i] = float(goal_nodes[i])

            node_pairs.append([input_nodes, goal_nodes])

            count += 1

            if not goal_nodes:
                break 
    return node_pairs

