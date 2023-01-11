# CNN-for-Image-Classification-
I'm using AlexNet Network for image classification 
The architecture consists of eight layers: five convolutional layers and three fully-connected layers.

AlexNet is an incredibly powerful model capable of achieving high accuracies on very challenging datasets. However, removing any of the convolutional layers will drastically degrade AlexNet’s performance. AlexNet is a leading architecture for any object-detection task and may have huge applications in the computer vision sector of artificial intelligence problems. In the future, AlexNet may be adopted more than CNNs for image tasks.


As a milestone in making deep learning more widely-applicable, AlexNet can also be credited with bringing deep learning to adjacent fields such as natural language processing and medical image analysis.


This script creates an AlexNet model, which is a deep convolutional neural network architecture that was introduced in 2012. The architecture consists of several layers of convolutional, max pooling, and fully connected layers. The model is then trained on an image dataset using the Adam optimizer, with categorical cross-entropy as the loss function and accuracy as the evaluation metric. The script is preprocessing the image data before training, by loading the images, resizing them to a fixed size, shuffling them, and then splitting them into training and validation sets. The script is also one-hot encoding the labels before training the model on them. After training the model, the script will evaluate the model on the validation data
