"""
AMAZON CAPTCHA SOLVER
"""
DOWNLOAD THE MODULES
pip install pillow, open-cv, selenium, pytesseract

1. Using selenium to perform the automation
2. First, locating the capatcha image and downloading it locally
3. Converting the image to grayscale using cv2 module, which is easier to read for the OCR
4. Grayscale image is read by the OCR (Pytesseract module) which converts the input image to text output
NOTE: Must install the pytesseract.exe for the process!
5. Text output is then entered in the input field of amazon using selenium
6. Function keeps calling itself until it gets access



NOTE: With the use of deep learning the task accuracy can be increased further, OCR accuracy is not that good but it works!