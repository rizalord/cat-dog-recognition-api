from PIL import Image
import io
import tensorflow as tf
import numpy as np

class PredictService:
    def predict(self, file: bytes):
        # Process the image
        img_height = 180
        img_width = 180
        target_size = (img_height, img_width)

        img = Image.open(io.BytesIO(file))
        img = img.convert('RGB')
        img = img.resize(target_size, Image.NEAREST)
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        # Import model
        model = tf.keras.models.load_model('app/models/model.h5')

        # Predict
        class_names = ["Cats", "Dogs", "Others"]
        predictions = model.predict(img_array)
        score = tf.nn.softmax(predictions[0])

        animalName = class_names[np.argmax(score)].replace("s", "")
        percentage = (np.max(score) * 100).astype(int)
        message = "Percentage of " + animalName + " Image"

        return animalName, percentage, message
