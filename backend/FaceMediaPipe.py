import cv2
import mediapipe as mp
import math
import numpy as np

def calc_distance(point1, point2):
  point1_array = np.array(point1)
  point2_array = np.array(point2)
  return np.linalg.norm(point2_array - point1_array) * conversion_factor


def display_landmarks():
  mp_drawing.draw_landmarks(
  image, face_landmarks,
  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
  connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1)
  )

# Inicialização do MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
model = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.5)

conversion_factor = 0.1
image = cv2.imread('images/photo.jpg')
original_width, original_height = image.shape[:2]

new_width = 450
new_height = 600

resized_image = cv2.resize(image, (new_width, new_height))
image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

# Processar a image
result = model.process(image_rgb)

# Verificar se foram encontrados pontos de referência
if result.multi_face_landmarks:
    for face_landmarks in result.multi_face_landmarks:
      point1 = face_landmarks.landmark[288] #azul
      point2 = face_landmarks.landmark[58] #verde

      # Converter coordenadas normalizadas para coordenadas da image
      height, width, _ = resized_image.shape
      point1_px = int(point1.x * width), int(point1.y * height)
      point2_px = int(point2.x * width), int(point2.y * height)

      # Desenhar pontos de referência na image
      cv2.circle(resized_image, point1_px, 5, (255, 0, 0), -1)
      cv2.circle(resized_image, point2_px, 5, (0, 255, 0), -1)

      # Calcular e exibir a distância entre os pontos
      # distance = calc_distance(point1_px, point2_px)

      distance_in_pixels = math.sqrt((point2_px[0] - point1_px[0])**2 + (point2_px[1] - point1_px[1])**2)
      focal_length = 22
      distance_in_cm = distance_in_pixels * focal_length / width
      cv2.putText(resized_image, f'Distancia: {distance_in_cm:.2f} cm', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('MediaPipe Face Landmarks', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
