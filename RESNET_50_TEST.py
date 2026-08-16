import os
import numpy as np
from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing import image

# Load the trained model
model = load_model('ResNet50_model.h5')

# Load class names from the pickle file
with open('class_names.pkl', 'rb') as f:
    class_names = pickle.load(f)

def predict_image(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_names[predicted_class_index]
    
    print("Predicted class:", predicted_class)
    if predicted_class =="NCCL":
        str_label="NCCl"
        


    elif predicted_class =="Normal":
        str_label="Normal"

    print(f"RESULT IS {str_label}")

# Test with a sample image
image_path = "test/d (1).png"  # Change this to your image path
predict_image(image_path)

# Test with another sample image
image_path = "test/n (2).png"  # Change this to your image path
predict_image(image_path)
