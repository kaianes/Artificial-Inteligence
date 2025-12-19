# Convolutional Autoencoders for Image Reconstruction and Denoising

## 1. Aim of the Exercises

The aim of these exercises is to introduce and apply **autoencoders** and **convolutional autoencoders (CAE)** for image reconstruction and image denoising tasks using the **MNIST dataset**.
Through a sequence of progressively more complex models, the exercises demonstrate how neural networks can learn **compact latent representations** of images and use them to generate meaningful outputs.

The work focuses on:

* Understanding the structure and purpose of **autoencoders**
* Implementing **dense** and **convolutional** autoencoders
* Applying autoencoders as **generative models**
* Using convolutional autoencoders to **remove noise from images**


## 2. Subject Content Overview

The exercises cover the following core topics in Artificial Intelligence and Deep Learning:

* Artificial Neural Networks
* Autoencoders
* Convolutional Neural Networks (CNNs)
* Latent representations
* Generative models
* Image reconstruction
* Image denoising
* Training neural networks using backpropagation


## 3. Autoencoders: Conceptual Background

![Autoencoder Architecture](autoencoder.png)

An **autoencoder** is a type of neural network trained to reproduce its input at the output.
It is composed of two main parts:

* **Encoder**: compresses the input into a lower-dimensional representation (latent space)
* **Decoder**: reconstructs the original input from this latent representation

The model is trained by minimizing the difference between the input and the reconstructed output.


## 4. Generative Models and Autoencoders

Autoencoders are considered **generative models** because they learn the underlying structure of the data distribution.
After training, they can:

* Generate reconstructed versions of input data
* Produce meaningful outputs from compressed representations
* Learn features without supervision

In the convolutional case, the model learns **spatial features** such as edges and shapes, making it well-suited for image-related tasks.


## 5. Workflow of the Exercises

The exercises follow a structured workflow:

1. Data preparation
2. Model definition (encoder and decoder)
3. Model compilation
4. Model training
5. Evaluation and visualization

Each step builds upon the previous one to reinforce understanding.


## 6. Exercise 1: Fully Connected Autoencoder

### Objective

To introduce the basic concept of autoencoders using fully connected (Dense) layers.

The MNIST images are first flattened from a two-dimensional structure (28 × 28 pixels) into a one-dimensional vector of 784 values.

Because of this flattening:

- The spatial relationship between pixels is lost
- The model treats all pixels as independent values
- The network learns global numerical patterns, not spatial features

### Steps

1. Flatten MNIST images into vectors of size 784
2. Build an encoder using Dense layers
3. Build a decoder using Dense layers
4. Combine encoder and decoder into a full autoencoder
5. Train the model to reconstruct the original images
6. Visualize original and reconstructed images

### Outcome

The model learns a compressed representation of the images and reconstructs them with reasonable accuracy.


## 7. Exercise 2: Convolutional Autoencoder (CAE)

### Objective

To improve reconstruction performance by preserving spatial information using convolutional layers.

By using convolutional layers and pooling operations:

- The spatial structure of the image is preserved
The network learns local features such as edges, shapes, and textures
The latent representation becomes spatially meaningful

The decoder then uses upsampling and convolution to reconstruct the image while maintaining spatial coherence.

### Steps

1. Use MNIST images in their 2D form (28 × 28 × 1)
2. Build a convolutional encoder using Conv2D and MaxPooling2D layers
3. Build a convolutional decoder using Conv2D and UpSampling2D layers
4. Combine encoder and decoder into a convolutional autoencoder
5. Train the model on clean images
6. Visualize encoded representations and reconstructed images

### Outcome

The CAE produces sharper reconstructions by learning spatial features such as edges and shapes.


## 8. Exercise 3: Image Denoising Using CAE

### Objective

To demonstrate how a convolutional autoencoder can be used to remove noise from images.

### Steps

1. Add Gaussian noise to MNIST images using a random normal distribution
2. Scale the noise using a noise factor
3. Clip noisy images to keep values in the valid range [0, 1]
4. Train the CAE using noisy images as input and clean images as output
5. Apply the trained model to noisy test images
6. Visualize noisy images and their denoised reconstructions

### Outcome

The model learns to filter out noise and reconstruct clean digit images, demonstrating a practical application of generative models.


## 9. Training Process

For all exercises, the training process follows the same principles:

* **Optimizer**: Adam
* **Loss function**: Binary Crossentropy
* **Input-output relationship**:

  * Reconstruction: input = output
  * Denoising: noisy input → clean output
* **Validation** is performed using the test set


## 10. Key Learning Outcomes

After completing these exercises, the following concepts are understood:

* How autoencoders compress and reconstruct data
* The importance of convolutional layers for image tasks
* How latent representations capture essential features
* How generative models learn data distributions
* How convolutional autoencoders can be applied to real-world problems such as image denoising


## 11. Conclusion

These exercises provide a complete introduction to autoencoders and convolutional autoencoders, moving from basic reconstruction to practical generative applications.
By progressively increasing complexity, the work demonstrates how deep learning models can learn meaningful representations and generate high-quality outputs from noisy or compressed inputs.
