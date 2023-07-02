import cv2 as cv
import numpy as np
import mediapipe as mp
mp_face_mesh = mp.solutions.face_mesh
cap = cv.VideoCapture[0]

with mp_face_mesh.FaceMesh(max_num_faces=1, 
refine_landarks=True,
min_detection_confidence= 0.5,
min_tracking_confidence=0.5) as face_mesh:
    while True: 
        ret, frame = cap.read()
        if not ret:
            break
    frame = cv.flip(frame, 1)
    rgb_frame = cv.cvtColor(frame. cv.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)
    if results.multi_face_landmarks:
        print(results.multi_face_landmarks)
    cv.imshow('img', frame)
    key = cv.waitKey(1)
    
cap.release()
cv.destroyAllWindows()
