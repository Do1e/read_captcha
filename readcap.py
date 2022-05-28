import requests
import ddddocr
import cv2
import numpy as np
import sys

saveDir = "./pic/"
capurl = "https://authserver.nju.edu.cn/authserver/captcha.html"

session = requests.Session()

while 1:
	r = session.get(capurl)
	img = cv2.imdecode(np.frombuffer(r.content, np.uint8), cv2.IMREAD_COLOR)
	ocr = ddddocr.DdddOcr(show_ad=False)
	res = ocr.classification(r.content)
	cv2.imshow(res, img)
	key = cv2.waitKey(0)
	if key == 13:		# Enter
		with open(saveDir + res + ".jpg", "wb") as f:
			f.write(r.content)
	elif key == 27:		# Esc
		exit(0)
	else:
		flag = False
		if(key == 225 or key == 226):	# Shift
			flag = True
			res = ""
		else:
			res = chr(key)
		print(res, end="")
		sys.stdout.flush()
		
		while 1:
			key = cv2.waitKey(0)
			if key == 225 or key == 226:	# Shift
				flag = True
			elif key >= 97 and key <= 122:	# a-z
				if flag:
					res += chr(key).upper()
					flag = False
				else:
					res += chr(key)
			elif key >= 49 and key <= 57:	# 0-9
				res += chr(key)
			elif key == 8:					# Backspace
				res = res[:-1]
			elif key == 13:					# Enter
				break
			print("\b\b\b\b\b\b\b" + res, end="")
			sys.stdout.flush()
		print("\npress 'y' or 'Enter' to confirm")
		key = cv2.waitKey(0)
		if chr(key) == 'y' or key == 13:
			with open(saveDir + res + ".jpg", "wb") as f:
				f.write(r.content)
	cv2.destroyAllWindows()