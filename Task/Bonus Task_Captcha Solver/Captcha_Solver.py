from PIL import Image
import pytesseract
import cv2
import urllib.request
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "https://www.amazon.com/errors/validateCaptcha"

def get_src(captcha_img):
	for img in captcha_img:
		src = img.get_attribute("src")
		if "captcha" in src:
			return src

def download_captcha(captch_url):
	f = open('captcha.jpg','wb')
	f.write(urllib.request.urlopen(captch_url).read())
	f.close()


def solve_captcha():
	image = cv2.imread('captcha.jpg')
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
	gray = cv2.medianBlur(gray, 3)
	filename = "{}.png".format("temp")
	cv2.imwrite(filename, gray)
	text = pytesseract.image_to_string(Image.open('temp.png'))
	return text

def try_captcha(driver):
	captcha_img = driver.find_elements_by_tag_name("img")
	download_captcha(get_src(captcha_img)) #downloading-img
	answer = solve_captcha()
	time.sleep(1)
	input_field = driver.find_element_by_id("captchacharacters")
	if input_field == None:
		print("Captcha Solved")
		drive.close()
	else:
		input_field.send_keys(answer)
		time.sleep(3)
		try_captcha(driver)


driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
try_captcha(driver) #continues to run till it's successfull






   