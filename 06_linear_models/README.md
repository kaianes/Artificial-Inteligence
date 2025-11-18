# Lab 6: Linear Models for Regression and Classification

This lab explores the foundational concepts and practical implementation of **Linear Models** in Machine Learning, covering both **Regression** and **Classification**.

##  Setup & Prerequisites

| Requirement | Files Needed | Tools Used |
| :--- | :--- | :--- |
| **Environment** | `Salary_data.csv`, `play_tennis.csv` | Google Colab or Jupyter Notebook |
| **Libraries** | N/A | `numpy`, `pandas`, `matplotlib.pyplot`, `sklearn` |


## Part I: Linear Regression

Linear regression is a fundamental statistical and machine learning technique used to model the relationship between a scalar dependent variable (what you want to predict) and one or more explanatory variables (the features you use for prediction).

Goal: To predict a continuous numerical value.

Find a line/hyperplane that minimizes the error between the line and the actual data points.

Finding the line $y = w \mathbf{x} + b$ that best fits the Salary data.

**Objective:** Understand how to find a best-fit line by minimizing error and apply this using Python libraries.

### 1. Tutorial: Manual Gradient Descent Implementation

This section focuses on the **theoretical underpinnings** of linear regression by manually implementing the training process.

| Concept | Key Takeaway |
| :--- | :--- |
| **Feature Extractor ($\phi(x)$)** | Understands how the **bias (intercept)** term is incorporated into the feature vector (e.g., transforming $x$ to $[1, x]$). |
| **Loss Function (MSE)** | Learns how the **Mean Squared Error** quantifies the distance between the prediction and the actual value. |
| **Gradient Descent** | Implements the core iterative process of adjusting the **weights ($w$)** based on the gradient of the loss function, using a **learning rate ($\eta$)** to reach the minimum error. |

### 2. Exercise I: Univariate Linear Model (`sklearn`)

This section transitions to the practical, optimized use of models.

* **Model:** Use `sklearn.linear_model.LinearRegression`.
* **Data Split:** Learn to partition the dataset into **training** and **test** sets (e.g., 1/3 split) to evaluate generalization performance.
* **Evaluation Metrics:** Calculate and interpret the **Root Mean Square Error (RMSE)** and **Relative RMSE (RRMSE)** to assess the prediction accuracy.

***

## Part II: Linear Classification

Linear classification is a method used to separate data points into different classes using a linear decision boundary. It is widely used in various applications, including spam detection, image recognition, and medical diagnosis.

Goal: To predict a discrete category or class label.

Find an optimal decision boundary (a line or hyperplane) that separates the data points belonging to different classes.

Finding the line $w \cdot \mathbf{x} + b = 0$ that separates the 'Yes' and 'No' data points.

**Objective:** Understand the transition from error minimization (regression) to boundary definition (classification), using specialized loss functions.

### 1. Tutorial: Manual Hinge Loss Implementation

This section introduces a core concept used by Support Vector Machines (SVMs).

| Concept | Key Takeaway |
| :--- | :--- |
| **Binary Mapping** | Understands that the target variable $y$ must be mapped to $\{-1, +1\}$ for linear classification. |
| **Hinge Loss ($\max(0, 1 - y \cdot \mathbf{w} \cdot \phi(x))$)** | Learns that Hinge Loss not only penalizes incorrect predictions but also penalizes correct predictions that are too close to the decision boundary (i.e., low *margin*). |
| **Classification Gradient** | Implements the specific gradient calculation for Hinge Loss, which is zero when the prediction is confident and correct. |

### 2. Exercise II: Multi-Class Classification (`LinearSVC`)

This section applies the classification concepts to a multi-class problem (Iris dataset) using a standard `sklearn` model.

* **Model:** Use `sklearn.svm.LinearSVC` (Linear Support Vector Classifier).
* **Decision Function:** Crucially, learn to use `linearClassifierName.decision_function()` to retrieve the **raw score** (margin) for each class before the final label is predicted. This explains how multi-class classification is handled internally.
* **Hinge Loss on Test Set:** Calculate the mean Hinge Loss using the raw decision values to evaluate the model's confidence and margin on unseen data.
* **Final Evaluation:** Use the **Confusion Matrix** and **Classification Report** (Precision, Recall, F1-score) to fully quantify the model's performance for each class.