import cv2
import pytesseract
from PIL import Image
import pandas as pd
import os


def read_image(path_to_img):
    # Set the path to tesseract executable
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

    # Load the image
    # change to link-up with the front-end file drop feature
    image = cv2.imread(path_to_img)

    # Preprocess the image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_image = cv2.threshold(
        gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Extract text from the image
    text = pytesseract.image_to_string(thresh_image)

    # Process the text and convert it into a dataframe
    lines = text.split('\n')
    data = []

    for line in lines:
        tokens = line.split()
        if len(tokens) >= 2:
            description = ' '.join(tokens[:-1])
            price = tokens[-1]
            try:
                float_price = float(price.replace(',', '').replace('$', ''))
                data.append([description, float_price])
            except ValueError:
                continue

    df = pd.DataFrame(data, columns=['description', 'price'])

    return df


def main():
    df = read_image("backend\model\data\CSBill1.png")
    print(df)
    return df


if __name__ == "__main__":
    main()
