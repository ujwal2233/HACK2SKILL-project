import pytesseract
from PIL import Image

# Open the image file
img = Image.open('ikik.jpg')

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(img)

# Print the extracted text
print(extracted_text)
