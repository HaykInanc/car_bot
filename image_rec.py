

def rec_number(img):
	import keras_ocr
	import numpy as np
	pipeline = keras_ocr.pipeline.Pipeline()
	# prediction_groups = pipeline.recognize([img])
	prediction_groups = pipeline.recognize([np.asarray(img)])
	# print('-_-'*20+str(keras_ocr.tools.read('https://1gai.ru/uploads/posts/2015-06/1433446564_bestcars2015lead.jpg')))
	word_list = [(word[0], word[1][0][0]) for word in prediction_groups[0]]
	word_list.sort(key=lambda a: a[1])
	return ' '.join([word[0] for word in word_list])