# Perceptron2020
CS 2400 Assignment 3 Neural Networks Fall 2020
Kayla Stuhlmann and Ya'kuana Davis


Results (100 epochs, 0.1 learning rate):

	90% train, 10% test
	Average Euclidean Distance = 0.2073667928112389

	80% train, 20% test
	Average Euclidean Distance = 0.21538961025746017

	70% train, 30% test
	Average Euclidean Distance = 0.19466408139287775

	60% train, 40% test
	Averade Euclidean Distance = 0.22378973796148766

	50% train, 50% test
	Average Euclidean Distance = 0.2515065923707962

	40% train, 60% test
	Average Euclidean Distance = 0.2146976100799424

	30% train, 70% test
	Average Euclidean Distance = 0.273591721727439

	20% train, 80% test
	Average Euclidean Distance = 0.2994175258448269

	10% train, 90% test
	Average Euclidean Distance = 0.3698008810065077

How to Run:
	To determine what percentage of examples will be in the training set or the test set,
	set the value of "train_split" in line 7 of Main.py to an int between 1-9. For example, if you want to train 70% and test
	30% of the examples, set "train_split" equal to 7. If you want to train 60% and test 40%, set "train_split"
	equal to 6. And so on. Then, run main() and wait for the Euclidean distance to print out.

Description of code:

