import cv2
import dlib

def faceDectection(img):

    # # read the image
    imgDetect = img
    # conver img to grayscale: 3D -> 2D
    gray = cv2.cvtColor(src=imgDetect, code=cv2.COLOR_BGR2GRAY)

    # dlib: Load Face Recognition Detector
    face_detector = dlib.get_frontal_face_detector()

    # load the predictor:
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # use detector to find face landmarks
    faces = face_detector(gray)

    for face in faces:
        x1 = face.left()  # left Point
        y1 = face.top()  # top Point
        x2 = face.right()  # right Point
        y2 = face.bottom()  # bottom Point

        # Draw a rectangle
        cv2.rectangle(img=imgDetect, pt1=(x1, y1), pt2=(
            x2, y2), color=(0, 255, 0), thickness=3)

        face_features = predictor(image=gray, box=face)

    return imgDetect
