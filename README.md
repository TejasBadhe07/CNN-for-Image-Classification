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


This script in Prediction loads a trained model, which is named 'model_name' using tf.keras.models.load_model('model_name') and uses it to make predictions on a single image. The image path is passed to the script as the variable 'Image_path'.

The preprocess_image function is used to read the image from the specified image path, resize it to the same fixed size (227x227), and convert it to a numpy array that can be used as input to the model. The function takes the image_path as the input and returns the preprocessed image.

After preprocessing the image, it is passed through the model.predict function, which produces an array of predicted class probabilities for the image. The np.argmax function is used to find the index of the highest probability, which corresponds to the most likely predicted class. The index is then used to look up the corresponding class label from the CATEGORIES list.

The Prediction script will print the predictions (class probabilities) and the predicted category of the image. 
