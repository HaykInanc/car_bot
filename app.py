from imageai.Detection import ObjectDetection
from PIL import Image
import cv2


def run_model():
	detector = ObjectDetection()
	detector.setModelTypeAsYOLOv3()
	detector.setModelPath("yolo.h5")
	detector.loadModel()
	return detector


def getDetections(detector, imageUrl):
	return detector.detectObjectsFromImage(input_image=imageUrl, 
												 output_image_path="image2new.jpg", 
												 minimum_percentage_probability=30)

def crope(imgPath, box_points, i):
	img = Image.open(imgPath)
	cropped_img = img.crop(box_points)
	cropped_img.save(f'results/result_{i}.jpg')

def saveImage(url, name):
	response = requests.get(url)
	with open(f'{name}.jpg', 'wb') as f:
		f.write(response.content)