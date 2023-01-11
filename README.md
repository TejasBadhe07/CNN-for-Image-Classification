# CNN-for-Image-Classification-
I'm using AlexNet Network for image classification 
The architecture consists of eight layers: five convolutional layers and three fully-connected layers.

AlexNet is an incredibly powerful model capable of achieving high accuracies on very challenging datasets. However, removing any of the convolutional layers will drastically degrade AlexNet’s performance. AlexNet is a leading architecture for any object-detection task and may have huge applications in the computer vision sector of artificial intelligence problems. In the future, AlexNet may be adopted more than CNNs for image tasks.


As a milestone in making deep learning more widely-applicable, AlexNet can also be credited with bringing deep learning to adjacent fields such as natural language processing and medical image analysis.


The function create_alexnet is used to create an AlexNet model using the TensorFlow Keras library. The function defines the architecture of the model by adding several layers of convolutional, max pooling, and fully connected layers to the model in a sequential manner. The function also sets some hyperparameters for these layers such as the number of filters, kernel size, stride, padding, activation function, and kernel initialization method.

The preprocess_data function is used to load the images from the dataset, resize them, and then divide them into training and validation sets.
The code reads all the images from the given DATADIR path, divide the images into 3 classes i.e. 'category1', 'category2', 'category3'
It will then resize the images and make a list of tuples where first element of tuple is the resized image and the second element of tuple is the label (number associated with the class of image)

After creating the model and preprocessing the data, the script trains the model using the model.fit method, providing the training data and the validation data as input, along with the number of training epochs. Finally, the script evaluates the model on the validation data using the model.evaluate method and prints the loss and accuracy scores.
