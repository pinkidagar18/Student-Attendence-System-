import os
import cv2
import numpy as np
import pickle
from .detector import detect_faces

# Paths for models
RECOGNIZER_PATH = 'face_recognition/models/trainer.yml'
LABEL_MAP_PATH = 'face_recognition/models/label_map.pkl'

# Ensure directory exists
os.makedirs('face_recognition/models', exist_ok=True)

# Initialize recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Dictionary to store student_id to label mapping
student_id_map = {}

# Try to load existing model if it exists
try:
    recognizer.read(RECOGNIZER_PATH)
    with open(LABEL_MAP_PATH, 'rb') as f:
        student_id_map = pickle.load(f)
except (cv2.error, FileNotFoundError):
    # Model doesn't exist yet, will be created when training
    pass

def train_recognizer(image, student_id):
    """
    Train the face recognizer with a new face
    
    Args:
        image: Image containing the face
        student_id: ID of the student
        
    Returns:
        Boolean indicating success
    """
    # Detect faces in the image
    faces = detect_faces(image)
    
    if len(faces) != 1:
        # Either no face or multiple faces detected
        return False
    
    # Extract the face region
    x, y, w, h = faces[0]
    face_img = image[y:y+h, x:x+w]
    
    # Convert to grayscale for face recognition
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    
    # Get a new label for this student
    if student_id in student_id_map.values():
        # Find the label for this student_id
        label = [k for k, v in student_id_map.items() if v == student_id][0]
    else:
        # Assign a new label
        if len(student_id_map) == 0:
            next_label = 1
        else:
            next_label = max(student_id_map.keys()) + 1
        label = next_label
        student_id_map[label] = student_id
    
    # Prepare data for training
    faces = [gray]
    labels = [label]
    
    # Train the recognizer
    try:
        try:
            # Try updating existing model
            recognizer.update(faces, np.array(labels))
        except:
            # First face, train from scratch
            recognizer.train(faces, np.array(labels))
        
        # Save the model
        recognizer.write(RECOGNIZER_PATH)
        
        # Save the student_id mapping
        with open(LABEL_MAP_PATH, 'wb') as f:
            pickle.dump(student_id_map, f)
        
        return True
    except Exception as e:
        print(f"Error training recognizer: {e}")
        return False

def recognize_face(image):
    """
    Recognize a face in an image
    
    Args:
        image: Image containing the face to recognize
        
    Returns:
        student_id if face recognized, None otherwise
    """
    # Detect faces in the image
    faces = detect_faces(image)
    
    if len(faces) != 1:
        # Either no face or multiple faces detected
        return None
    
    # Extract the face region
    x, y, w, h = faces[0]
    face_img = image[y:y+h, x:x+w]
    
    # Convert to grayscale for face recognition
    gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
    
    try:
        # Try to recognize the face
        label, confidence = recognizer.predict(gray)
        
        # Lower confidence value means better match in LBPH
        if confidence < 70:  # Threshold can be adjusted
            return student_id_map.get(label)
    except Exception as e:
        print(f"Error recognizing face: {e}")
        pass
    
    return None