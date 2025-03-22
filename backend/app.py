from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
import io

app = Flask(__name__)
CORS(app)

def decode_image(img_base64):
    img_data = base64.b64decode(img_base64)
    np_img = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    return img

def dummy_sign_language_recognition(img):
    # Placeholder logic
    # Replace this with ML model inference for actual sign language detection
    height, width = img.shape[:2]
    return "Detected: Hello" if height > 0 and width > 0 else "No Sign Detected"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    img_base64 = data['image']
    img = decode_image(img_base64)

    result = dummy_sign_language_recognition(img)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
