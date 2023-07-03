import cv2
import mediapipe as mp
import math
import json
import os

def calcDistance (point1, point2):
  return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def showFace(image):
  cv2.imshow('Análise Facial', image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def calcThird(third, trme):
  thirdValue = third * 100
  trmeValue = thirdValue / trme
  return trmeValue

def faceHeightAnalysis(faceHeight):
  if (faceHeight < 75):
    return 'Altura: Face longa - Indica preenchimento de malar.'
  elif (faceHeight > 75):
    return 'Altura: Face curta - Indica preenchimento de terço inferior.'

def faceWidthAnalysis(sex, faceWidth):
  if (faceWidth < 75 and sex == "female"):
    return 'Largura: Zi zi muito grande - Indica prenchimento mandibula/mento.'
  elif (faceWidth > 75 and sex == "female"):
    return 'Largura: Go go muito grande - Indica preenchimento zigomatico/malar.'
  elif (faceWidth < 75 and sex == "male"):
    return 'Largura: Zi zi muito grande - Indica prenchimento mandibula/mento.'
  elif (faceWidth > 75 and sex == "male"):
    return 'Largura: Face com tamanho ideal.'

def lowerThirdAnalysis(sex, third):
  if (sex == "male" and third > 36):
    return 'Terço Inferior - Destacar terço médio Zi zi/Go go.'
  elif (sex == "male" and third < 36):
    return 'Terço Inferior - Destacar terço inferior'
  elif (sex == "female" and third > 33):
    return 'Terço Inferior - Destacar terço médio Zi zi/Go go.'
  elif (sex == "female" and third < 33):
    return 'Terço Inferior - Destacar terço inferior'

def middleThirdAnalysis(sex, third):
  if (sex == "male" and third > 30):
    return 'Terço Médio - Destacar terço inferior.'
  elif (sex == "male" and third < 30):
    return 'Terço Médio - Destacar malar CK3.'
  elif (sex == "female" and third > 33):
    return 'Terço Médio - Destacar terço inferior.'
  elif (sex == "female" and third < 33):
    return 'Terço Médio - Destacar malar CK3.'

def upperThirdAnalysis(sex, third):
  if (sex == "male" and third > 34):
    return 'Terço Superior - Destacar terço médio e inferior.'
  elif (sex == "male" and third < 34):
    return 'Terço Superior - Avaliar conjunto de terços.'
  elif (sex == "female" and third > 34):
    return 'Terço Superior - Destacar terço médio e inferior.'
  elif (sex == "female" and third < 34):
    return 'Terço Superior - Avaliar conjunto de terços.'


faceModel = mp.solutions.face_mesh
model = faceModel.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)

image = cv2.imread('C:/Users/lucas/Downloads/face.png')
original_width, original_height = image.shape[:2]

new_width = 450
new_height = 600

resized_image = cv2.resize(image, (new_width, new_height))
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

processedModel = model.process(image_rgb)

if processedModel.multi_face_landmarks:
    for face_landmarks in processedModel.multi_face_landmarks:
      #trme - Testa ao queixo (Face)
      point1 = face_landmarks.landmark[10]
      point2 = face_landmarks.landmark[175]

      #Zizi - Orelha
      point3 = face_landmarks.landmark[34]
      point4 = face_landmarks.landmark[264]

      #Gogo - Mandibula
      point5 = face_landmarks.landmark[58]
      point6 = face_landmarks.landmark[288]

      #SnN - Nariz e sobrancelha
      point7 = face_landmarks.landmark[2]
      point8 = face_landmarks.landmark[9]

      height, width, _ = image.shape
      point1_px = int(point1.x * width), int(point1.y * height)
      point2_px = int(point2.x * width), int(point2.y * height)
      point3_px = int(point3.x * width), int(point3.y * height)
      point4_px = int(point4.x * width), int(point4.y * height)
      point5_px = int(point5.x * width), int(point5.y * height)
      point6_px = int(point6.x * width), int(point6.y * height)
      point7_px = int(point7.x * width), int(point7.y * height)
      point8_px = int(point8.x * width), int(point8.y * height)

      cv2.circle(image, point1_px, 5, (0, 255, 0), -1)
      cv2.circle(image, point2_px, 5, (0, 255, 0), -1)
      cv2.circle(image, point3_px, 5, (0, 255, 0), -1)
      cv2.circle(image, point4_px, 5, (0, 255, 0), -1)
      cv2.circle(image, point5_px, 5, (0, 255, 0), -1)
      cv2.circle(image, point6_px, 5, (0, 255, 0), -1)
      cv2.circle(image, point7_px, 5, (0, 255, 0), -1)
      cv2.circle(image, point8_px, 5, (0, 255, 0), -1)

      trmeDistance = calcDistance(point1_px, point2_px)
      ziziDistance = calcDistance(point3_px, point4_px)
      gogoDistance = calcDistance(point5_px, point6_px)
      snnDistance  = calcDistance(point7_px, point8_px)
      lowerThird   = calcDistance(point2_px, point7_px)
      middleThird  = calcDistance(point7_px, point8_px)
      upperThird   = calcDistance(point1_px, point8_px)

      focal_length = 22

      trme         = (trmeDistance * focal_length / width)
      zizi         = ziziDistance * focal_length / width
      gogo         = gogoDistance * focal_length / width
      snn          = snnDistance  * focal_length / width
      lowerThird   = lowerThird   * focal_length / width
      middleThird  = middleThird  * focal_length / width
      upperThird   = upperThird   * focal_length / width

      faceHeight = (zizi / trme) * 100
      faceWidth  = (gogo / zizi) * 100

      lower  = calcThird(lowerThird, trme)
      middle = calcThird(middleThird, trme)
      upper  = calcThird(upperThird, trme)
      upper += 3

      data = {
      "Trme_zizi": round(faceHeight, 2),
      "Trme_zizi_desc": faceHeightAnalysis(faceHeight),
      "Zizi_Gogo": round(faceWidth, 2),
      "Zizi_Gogo_desc": faceWidthAnalysis("male", faceWidth),
      "terco_inferior": round(lower),
      "terco_inferior_desc": lowerThirdAnalysis("male", lower),
      "terco_meio": round(middle),
      "terco_meio_desc": middleThirdAnalysis("male", middle),
      "terco_superior": round(upper),
      "terco_superior_desc": upperThirdAnalysis("male", upper),
      }

      json_data = json.dumps(data)
      print(json_data)

# showFace(image)
os.remove('C:/Users/lucas/Downloads/face.png')