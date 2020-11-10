from Node import InputNode, OutputNode
import math

class NeuralNetwork:
    '''
    '''
    def __init__(self, input_list, output_list_expected, weights_list):
        self.input_list = input_list
        self.output_list_expected = output_list_expected
        self.weights_list = weights_list 
       
    
    def train_NN(self):
        input_nodes_list = [] 

        # List of 10 lists - One for each possible OutputNode 
        final_weights = [] 

        # Loop through input list
        for i in range(len(self.input_list)): 
            input_node = InputNode(self.input_list[i], self.weights_list[i])

            input_nodes_list.append(input_node)

        # Create output nodes 
        for i in range(len(self.output_list_expected)):
            output_node = OutputNode(i, input_nodes_list, self.output_list_expected[i])

            # Count the number of epochs 
            count = 0 

            # Do 100 epochs of back propogation 
            while count < 10: 
                # Sum up weights for current OutputNode index 
                output_node.weigh_sums() 

                # Get and store activation function results in OutputNode 
                output_node.activation_function()

                # Get the error
                error = output_node.get_error() 

                output_node.backpropogation()
                
                count += 1
            
            # List of weights for this one OutputNode  
            final = [] 

            # Get evey InputNode's new weights 
            for node in output_node.input_list:
                final.append(node.weights[output_node.index])
            
            # Append the updated weight list for the current OutputNode
            final_weights.append(final)
            
        return final_weights

               
    def test_NN(self): 
        input_nodes_list = [] 

        # Stores the error for each output 
        final_error = 0.0 

         # Loop through input list
        for i in range(len(self.input_list)): 
            input_node = InputNode(self.input_list[i], self.weights_list[i])

            input_nodes_list.append(input_node)

        # Create output nodes 
        for i in range(len(self.output_list_expected)):
            output_node = OutputNode(i, input_nodes_list, self.output_list_expected[i])

            # Sum up weights for current OutputNode index 
            output_node.weigh_sums() 

            # Get and store activation function results in OutputNode 
            output_node.activation_function()

            # Get the error
            error = output_node.get_error() ** 2

            # square error 
            final_error += error 
        
        return math.sqrt(final_error)




               
               
                   
    #def main()
   
    #data_list = [ [input, output] ] # list of every input, output pair in data (each example)
    #number of pairs = 5620
   
    #FOR 10/90 SPLIT
   
    #training_set = data_list[0 : 561]
    #test_set = data_list[561 :]
   
   
   

    #for each [input, output] pair, make nueral_network(inputs list, expected outputs list)
        #weight