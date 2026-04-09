
# -------------------------------------------------------------
# 3. Deep Learning Basics
# -------------------------------------------------------------





# -------------------------------------------------------------
# 🔹 1. Neural Networks Fundamentals
# -------------------------------------------------------------

## /FIRST PRINCIPLES

* A neural network is inspired by the human brain.
* Basic unit = **neuron** → takes inputs, applies weights, adds bias, produces output.
* Many neurons form layers → Input → Hidden → Output.

## /HIGHLIGHTS

* Learns patterns from data automatically.
* Uses weights & biases to adjust learning.
* More layers = more complex learning (Deep Learning).

## /5WHYS

1. Why neural networks? → To learn complex patterns.
2. Why complex patterns? → Data is not linear/simple.
3. Why not traditional methods? → They fail for high-dimensional data.
4. Why high-dimensional data? → Real-world data (images, text) is complex.
5. Why mimic brain? → Brain is best example of learning system.

“Mimic brain” na, brain epdi learn pannudho adha mathiri machine learn panna try pannradhu.

## /BRIEFLY
Neural networks are layered systems that learn patterns using weighted inputs and outputs.



# -------------------------------------------------------------
# 🔹 2. Activation Functions
# -------------------------------------------------------------

## /FIRST PRINCIPLES

* After neuron calculation → we apply a function.
* This function decides **whether neuron should activate or not**.
* Adds **non-linearity** to model.

## /HIGHLIGHTS

* Common: ReLU, Sigmoid, Tanh.
* Without activation → model becomes linear.
* ReLU is most widely used.

## /5WHYS

1. Why activation? → To decide output.
2. Why decision needed? → Raw output not meaningful.
3. Why non-linearity? → Real-world problems are non-linear.
4. Why not linear only? → Cannot solve complex problems.
5. Why ReLU popular? → Simple and efficient.

## /BRIEFLY
Activation functions add non-linearity and decide neuron output.

---

# 🔹 3. Loss Functions

## /FIRST PRINCIPLES

* Measures **error** between predicted and actual output.
* Guides the model on how wrong it is.

## /HIGHLIGHTS

* Regression → MSE (Mean Squared Error)
* Classification → Cross-Entropy
* Lower loss = better model

## /5WHYS

1. Why loss? → To measure error.
2. Why measure error? → To improve model.
3. Why improve? → Predictions must be accurate.
4. Why accuracy important? → Real-world decisions depend on it.
5. Why continuous improvement? → Model learns iteratively.

## /BRIEFLY

Loss function tells how wrong the model prediction is.


# -------------------------------------------------------------
# 🔹 4. Backpropagation
# -------------------------------------------------------------

## /FIRST PRINCIPLES

* Method to **update weights** using error.
* Error flows backward from output to input layers.

## /HIGHLIGHTS

* Uses chain rule (calculus).
* Adjusts weights to reduce loss.
* Core of training neural networks.

## /5WHYS

1. Why backpropagation? → To update weights.
2. Why update weights? → To reduce error.
3. Why reduce error? → To improve prediction.
4. Why backward? → Error starts at output.
5. Why efficient? → Uses gradients smartly.

## /BRIEFLY

Backpropagation updates weights by sending error backward.


# -------------------------------------------------------------
# 🔹 5. Gradient Descent Optimization
# -------------------------------------------------------------

## /FIRST PRINCIPLES

* Algorithm to **minimize loss**.
* Moves weights in direction of **lowest error**.

## /HIGHLIGHTS

* Learning rate controls speed.
* Types: Batch, Stochastic, Mini-batch.
* Too high LR = unstable, too low = slow.

## /5WHYS

1. Why gradient descent? → To minimize loss.
2. Why minimize loss? → Better predictions.
3. Why use gradients? → Shows direction of change.
4. Why step-by-step? → Avoid overshooting.
5. Why optimization needed? → Efficient training.

## /BRIEFLY

Gradient descent updates weights to reduce loss step by step.


# -------------------------------------------------------------

https://chatgpt.com/share/69c6d42e-06f4-8321-8085-93e18e53f39c











