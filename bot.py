import telebot
from app import *
from imageai.Detection import ObjectDetection
from PIL import Image
import cv2
import requests
from image_rec import rec_number



bot = telebot.TeleBot(token)

detector = run_model()

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello!")



@bot.message_handler(content_types=['photo'])
def photo_handler(m):
	file = bot.get_file(m.photo[-1].file_id)

	link = f'https://api.telegram.org/file/bot{token}/{file.file_path}'
	username = f'{m.from_user.first_name} {m.from_user.last_name} ({m.from_user.username})'
	saveImage(link, username)
	result = getDetections(detector, f'{username}.jpg')
	result_numbers = []

	for eachObject in result:
		if eachObject["percentage_probability"] > 90 and eachObject["name"] == 'car':
			print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
			img = Image.open(f'{username}.jpg')
			cropped_img = img.crop(eachObject["box_points"])
			# print('-_-'*20+str(type(cropped_img)))
			image_name = rec_number(cropped_img)
			cropped_img.save(f'results/{image_name}.jpg')
			result_numbers.append(image_name)
			# crope(f'{username}.jpg', eachObject["box_points"], i)
			
	bot.send_message(m.from_user.id, '\n'.join(result_numbers))

bot.polling()