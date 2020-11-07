import random

E_VALUE = 2.71828

class InputNode:
    ''' Creates an object two keys:
        input_value = a float value 
        weights = and an array of floats
    '''
    def __init__ (self, input_value, weights): 
        self.input_value = input_value 
        self.weights = weights 
    
    def __str__(self):
        return "Input Node Value {} \n".format(self.input_value)

    def print_weights(self):
        print("=========================")
        print("Printing weights for InputNode with value {}...\n".format(self.input_value))

        for x in len(self.weights):
            print("Weight at index {} is {}".format(x, self.weights[x]))
            
        print("=========================")


class OutputNode: 
    ''' Creates an object with 5 keys: 
        index = the position of the output node relative to the larger list it originates
        input_list = list of InputNodes 
        weighted_sum = sum of weights in InputNode at the OutputNode's index 
        output = final result after running the activation function on weighted_sum
    '''
    def __init__ (self, index, input_list, expected_output, weighted_sum=0.0, output=0.0):
        self.index = index
        self.input_list = input_list 
        self.weighted_sum = weighted_sum 
        self.output = output 
        self.expected_output = expected_output

    def __str__(self):
        print("=========================")
        print("Printing OutputNode information...\n")
        return "OutputNode # {} \n Weighted Sum {} \n Output {}".format(self.index, self.weighted_sum, self.output)

    def weigh_sums(self):
        # store total of weighted sums 
        temporary_total = 0.0 

        # Multiply the input_value by the weight at the OutputNode's index 
        for x in self.input_list:
            temporary_total += float(x.input_value) * float(x.weights[self.index])

        self.weighted_sum = temporary_total
        return self.weighted_sum

    def activation_function(self):
        global E_VALUE 

        # Activation function 
        self.output = 1 / (1 + (E_VALUE ** -(self.weighted_sum)))
        
        return self.output
    
    def get_error(self):
        #need to access list of actual output[self.index] above is placeholder
        #error = expected output - actual output
        error = self.expected_output - self.output

        return error
       
   
    def backpropogation(self):
        ###### WOOOOOOORWKKKK ON THIS SHIYT  

        sigmoid = 1 / (1 + (E_VALUE ** -(self.weighted_sum)))
        
        #maybe make sigmoid the global var instead of e???
        sigmoid_deriv = sigmoid * (1.0 - sigmoid)

        final_weights = []
        
        for i in range(len(self.input_list)):
    
            new_weight = self.input_list[i].weights[self.index] + (0.1 * self.get_error() * self.input_list[i].input_value * sigmoid_deriv)
            
            # Update weight in InputNode's weight list  
            self.input_list[i].weights[self.index] = new_weight

            

    

# practice 

# Create InputNodes from long list 
# new1 = InputNode(0, [random.uniform(-1,1) for x in range(10)])
# new2 = InputNode(0.1, [random.uniform(-1,1) for x in range(10)])
# new3 = InputNode(0.2, [random.uniform(-1,1) for x in range(10)])
# new4 = InputNode(0.3, [random.uniform(-1,1) for x in range(10)])

# Put all of the InputNodes in a new list 
# input_list = [new1, new2, new3, new4]

# print("========================")
# print("inputs")
# print("========================")
# for x in input_list:
#     print(x)
# print("========================\n")

# Create an output list to store OutputNode objects 
# output_array = []

# for x in range(4): 
    # Create OutputNode object 
    # output_node = OutputNode(x, input_list, 0)

    # Sum up weights for current OutputNode index 
    # output_node.weigh_sums() 

    # Get and store activation function results in OutputNode 
    # output_node.activation_function()

    # Append updated OutputNode to output array 
    # output_array.append(output_node)







