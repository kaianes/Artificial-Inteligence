
# Deep Neural Network (DNN) for Multiclass Classification – Learning Summary

## 1. Objective of the Exercise

The goal of this lab is to design, train, and understand a **Deep Neural Network (DNN)** for a **multiclass classification problem**, using the Iris dataset as a case study. The exercise focuses on both **practical implementation** and **theoretical understanding** of how DNNs process data.

## 2. Dataset and Problem Setup

The Iris dataset consists of:

* **4 numerical input features**:

  * Sepal length
  * Sepal width
  * Petal length
  * Petal width
* **1 target variable (`target`)** representing flower species:

  * 0 → Setosa
  * 1 → Versicolor
  * 2 → Virginica

This is a **supervised learning** and **multiclass classification** problem.

## 3. Feature and Target Separation

The dataset is split into:

* **Features (`X`)**: numerical input variables used by the model
* **Target (`y`)**: categorical class labels

Although the features are already numerical and require no encoding, the target variable represents categories and must be transformed before training a neural network.

## 4. Label Encoding (One-Hot Encoding)

### Why encoding is required

Class labels such as `0`, `1`, and `2` are categorical identifiers, not numerical values with magnitude or order. Using them directly would introduce a false ordinal relationship.

### One-Hot Encoding

Each class is represented as a binary vector:

* 0 → [1, 0, 0]
* 1 → [0, 1, 0]
* 2 → [0, 0, 1]

This representation:

* Removes any implied order between classes
* Is compatible with softmax activation and categorical cross-entropy loss
* Is required for multiclass neural network outputs

The `OneHotEncoder` from `scikit-learn` is used, with:

* `fit_transform()` applied only to training labels
* `transform()` applied to test labels to avoid data leakage

## 5. Why the Encoder Requires a 2D Input

Scikit-learn encoders operate on **feature matrices**, following the convention:

* Rows represent samples
* Columns represent features

Even when encoding a single categorical variable, the input must be reshaped from:

* `(n_samples,)` → `(n_samples, 1)`

This makes the data structure explicit and allows the encoder to operate correctly.

## 6. Feature Normalization

Before training the DNN, input features are normalized. Normalization ensures that:

* All features are on a similar scale
* Gradient descent converges faster
* No feature dominates learning due to magnitude differences

Normalized data is used for both training and validation.

## 7. Feature Dimension (`feature_dim`)

The feature dimension represents the **number of input features per sample**.

```python
feature_dim = X_train_norm.shape[1]
```

This value defines:

* The size of the input layer
* How many inputs each neuron in the first hidden layer receives

For the Iris dataset:

* `feature_dim = 4`

## 8. DNN Architecture Design

The Deep Neural Network is built using a **Sequential** model with the following layers:

### Input Layer

* Defined implicitly through `input_shape=(feature_dim,)`
* Accepts a vector of normalized features

![DNN Architecture](dnn_architecture.png)

### Hidden Layers

1. **First Hidden Layer**

   * Dense layer with 16 neurons
   * ReLU activation
   * Fully connected to all input features

2. **Dropout Layer**

   * Dropout rate = 0.2
   * Randomly disables 20% of neurons during training
   * Helps prevent overfitting

3. **Second Hidden Layer**

   * Dense layer with 16 neurons
   * ReLU activation

4. **Second Dropout Layer**

   * Dropout rate = 0.2

### Output Layer

* Dense layer with 3 neurons (one per class)
* Softmax activation
* Outputs a probability distribution over classes

## 9. Activation Functions

* **ReLU (Rectified Linear Unit)**
  Introduces non-linearity and enables learning complex patterns.

* **Softmax**
  Converts raw outputs into probabilities that sum to 1, suitable for multiclass classification.

## 10. Model Compilation

The model is compiled with:

* **Optimizer**: Adam (efficient gradient-based optimization)
* **Loss function**: Categorical cross-entropy (appropriate for one-hot encoded multiclass targets)
* **Metric**: Accuracy

## 11. Model Training

The model is trained using:

* **Epochs**: 50
  (Number of complete passes through the training data)
* **Batch size**: 32
  (Number of samples processed before updating weights)
* **Validation split**: 0.3
  (30% of training data used to monitor generalization)

The training process returns a `history` object that stores:

* Training loss and accuracy
* Validation loss and accuracy

## 12. Training Monitoring and Visualization

The training history is used to visualize:

* Accuracy vs. epochs
* Loss vs. epochs

These plots help identify:

* Learning progress
* Convergence behavior
* Overfitting or underfitting

## 13. Key Concepts Learned

* Difference between features and labels
* Importance of label encoding for neural networks
* Role of feature normalization
* Meaning of feature dimension
* Structure and function of DNN layers
* Purpose of dropout regularization
* Relationship between softmax and categorical cross-entropy
* Proper separation of training, validation, and test data

## 14. Conclusion

This lab demonstrates the complete pipeline for building a Deep Neural Network for multiclass classification, combining theoretical understanding with practical implementation. Each preprocessing and architectural choice plays a critical role in ensuring correct learning, numerical stability, and generalization performance.
