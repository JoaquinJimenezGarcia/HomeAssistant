import face_recognition as face_recognition
import cv2 as cv2
import numpy as np
import requests
import json
import yaml
import os

# IP for voice service
ip_voice = "http://localhost:5001/"

path = os.getcwd()

with open(path+"/config.yaml", "r") as f:
    config = yaml.load(f)

people = config['people']

print(people)

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
people_images = []
for person in people:
    people_images.append(face_recognition.load_image_file(path+'/' + person['picture_path']))

people_face_encodig = []
for person_image in people_images:
    people_face_encodig.append(face_recognition.face_encodings(person_image)[0])

# Create arrays of known face encodings and their names
known_face_encodings = []
for person_face_encodig in people_face_encodig:
    known_face_encodings.append(person_face_encodig)

known_face_names = []
for face_name in people:
    known_face_names.append(face_name['name'])

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
known_person = False
first_time_found = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                known_person = True

                if known_person and first_time_found:
                    print('Hello %s. How are you today?' % name)
                    first_time_found = False
            else:
                known_person = False
                # Set to true so it can enter in the previous if next time it found a face
                first_time_found = True

                print('There is a stranger in the room. Please exit or I will call security.')
            face_names.append(name)

    process_this_frame = not process_this_frame

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

def server_request(api_path):
    try:
        requests.get(ip_voice + api_path)
        
        return "Sended to voice service"
    except:
        return "Sorry, there was an error trying to connect to voice service."