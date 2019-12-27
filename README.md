# AndI


Each neuron takes in an input, multiplies by a weight, a proportional constant, and outputs the result. It can have multiple weights. The number of weights equals the number of neurons in the upcoming layer. Each weight is associated with a neuron of the upcoming layer. So if a neuron connects to 3 neurons, a, b and c, in the upcoming layer, it will multiply its input with a specific weight for a and output the result to a, a specific weight for b and output the result to b and a specific weight for c and output the result to c.

Remember though, when there are many incoming neurons, the sum of the weight * the input just becomes a hodge podge of massive numbers. We need to know how high these numbers are relative to the range of possible values. This is why we use the Sigmoid normalization function.

Sigmoid normalization function takes any number and tells you how positive it is on a scale from 0 to 1. Anything less than 0.5 is negative and anything
above is positive. By having the sums represented on a scale from 0 to 1, it allows us to see the "strength" of the output. So once a neuron carries out its function on its input, it also executes the Sigmoid normalization function and outputs this result to the upcoming neuron.

When there's many neurons and layers, the programming behind the multiplications can get tricky. This can be simply done with matrix multiplication. You don't have to but it makes everything much easier.

Let A = a matrix of m x n where m = the number of neurons in the upcoming layer and n = the number of neurons in the incoming layer. Each row holds the specific weights at every neuron of the incoming layer meant for a specific neuron. So a row can hold all n weights (for each incoming neuron) for upcoming neuron a, another row holds the weights for upcoming neuron b and another row holds the weights for upcoming neuron c.

Let x = a matrix of n x 1 which holds each input of neurons 1 to n of the incoming layer.

Ax = y = a matrix of m x 1 which holds the outputs to each neuron in the upcoming layer.

You can then run the Sigmoid normalization function on every output in y. We can simplify this process further though. Running the normalization function on every element in y is equal to running the function on the whole matrix, y. Therefore we can just input Ax into the normalization function to get y as already normalized.

There is one more thing you can do to increase accuracy, biases. You can add a constant to the sum of the weights * inputs of incoming neurons, this constant is the bias. This essentially provides a hurdle to how positive the output to a layer is. We use it when we only care if the output of a layer reaches a certain threshold value, the bias. To implement it, just add a matrix, b, of n x 1 which holds the bias for each incoming neuron to Ax before you do the normalization. 



  A          X    =    y

Inputs       X       Outputs
0 0 1        x1         0
1 1 1        x2         1
1 0 1        x3         1
0 1 1        x4         0


Training process:
1. Assign random weights to neurons.
2. Take random inputs through the network to get actual output.
2. Calculate error, error = training output - actual output
3. Depending on size of error, adjust weights. We use the following function
      AdjustBy = error * derivative of sigmoidNormalization(actual outputs)
4. Repeat as much as possible (This does 30,000 times)
