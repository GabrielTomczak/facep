from imutils import face_utils
import dlib
import cv2
import math
from PIL import Image

class FaceAnalysis():
    def __init__(self, name):
        self.name = name

    def chinSize(self, firstPoint, secondPoint):
        x1, y1 = firstPoint
        x2, y2 = secondPoint
        pointA = x2 - x1
        pointB = y2 - y1
        chinSize = math.sqrt(math.pow(pointA, 2) + math.pow(pointB, 2))
        return chinSize

    def noseSize(self, firstPoint, secondPoint):
        x1, y1 = firstPoint
        x2, y2 = secondPoint
        pointA = x2 - x1
        pointB = y2 - y1
        noseSize = math.sqrt(math.pow(pointA, 2) + math.pow(pointB, 2))
        return noseSize

    def eyeSize(self, firstPoint, secondPoint):
        x1, y1 = firstPoint
        x2, y2 = secondPoint
        pointA = x2 - x1
        pointB = y2 - y1
        eyeSize = math.sqrt(math.pow(pointA, 2) + math.pow(pointB, 2))
        return eyeSize

    def faceSize(self, firstPoint, secondPoint):
        x1, y1 = firstPoint
        x2, y2 = secondPoint
        pointA = x2 - x1
        pointB = y2 - y1
        faceSize = math.sqrt(math.pow(pointA, 2) + math.pow(pointB, 2))
        return faceSize

    def px_to_cm(self, pixels, ppcm):
        centimeters = pixels / ppcm
        return centimeters

    def getImageResolution(self, camera):
        width    = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        height   = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        ratio    = camera.get(cv2.CAP_PROP_POS_AVI_RATIO)
        duration = camera.get(cv2.CAP_PROP_POS_MSEC) / 1000
        frames   = ratio * duration * camera.get(cv2.CAP_PROP_FPS)
        ppcm     = (width/frames) * 2.54
        return ppcm

    def getImagePixels(self, camera, image):
        width    = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        height   = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        ratio    = camera.get(cv2.CAP_PROP_POS_AVI_RATIO)
        duration = camera.get(cv2.CAP_PROP_POS_MSEC) / 1000
        frame    = image
        height, width, channel = frame.shape
        num_pixels = width * height * channel
        return num_pixels

face = FaceAnalysis("teste")
model = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model)
camera = cv2.VideoCapture(0)
# cv2.imwrite("face.jpg", image)
# if ret:
while True:
    # ppcm = face.getImageResolution(camera)
    ret, image = camera.read()
    pixels = face.getImagePixels(camera, image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # for (x, y) in shape:
            # cv2.circle(image, (x,y), 2, (0, 255, 0), -1)
            # cv2.circle(image, (shape[8]), 2, (0, 255, 0), -1)
            # cv2.circle(image, (shape[33]), 2, (0, 255, 0), -1)

        print("Queixo: %.2f cm" % face.chinSize(shape[8], shape[33]))
        print("Nariz: %.2f cm" % face.noseSize(shape[27], shape[33]))
        print("Olhos: %.2f cm" % face.eyeSize(shape[36], shape[45]))

    cv2.imshow("Output", image)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
camera.release()
