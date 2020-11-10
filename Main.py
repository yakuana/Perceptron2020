from NeuralNet import NeuralNetwork
from ReadFiles import read_file
import random

def main(): 
    node_pairs_list = read_file("digit-examples-all.txt")
    train_split = 1
    
    print("Split: {0}0% train, {1}0% test".format(str(train_split), str(10 - train_split)))
    train_set_size = (5620 // 10) * train_split

    training_set = node_pairs_list[0 : train_set_size + 1]
    test_set = node_pairs_list[train_set_size + 1 :]
    
    #training_set = node_pairs_list[0 : 50]
    #test_set = node_pairs_list[50 : 100]
    
    weights = [] 

    for i in range(64):
        weights.append([random.uniform(-1,1) for x in range(10)])

    for pair in training_set:
        neural_net = NeuralNetwork(pair[0], pair[1], weights)
        neural_net.train_NN()
        weights = neural_net.weights_list
    
    euclidean_distance = 0 

    for pair in test_set:
        neural_net = NeuralNetwork(pair[0], pair[1], weights)
        euclidean_distance += neural_net.test_NN()
        weights = neural_net.weights_list

    if (euclidean_distance == 0):
        avg_euclidean_distance = 0
    else: 
        avg_euclidean_distance = euclidean_distance / len(test_set) 

    print("Average Euclidean Distance: {}".format(avg_euclidean_distance))

main()