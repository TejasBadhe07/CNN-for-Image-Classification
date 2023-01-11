import tensorflow as tf
import numpy as np
import cv2

im_size = 227
CATEGORIES = ['category1', 'category2', 'category3']

model = tf.keras.models.load_model('model_name')

Image_path = 'custom image path'


def preprocess_image(image_path):
    # Read in the image
    image = cv2.imread(image_path)

    # Resize the image
    image = cv2.resize(image, (im_size, im_size))

    # Convert the image to a numpy array
    image = np.array(image).reshape(-1, im_size, im_size, 3)

    return image

X = preprocess_image(Image_path)

# Make predictions on the data
predictions = model.predict(X)

# Get the index of the highest prediction value
prediction_index = np.argmax(predictions)

# Get the corresponding category
category = CATEGORIES[prediction_index]

# Print the predictions
print(predictions)
# Print the category
print(category)

