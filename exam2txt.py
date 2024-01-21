import configparser
import img2pdf
import os
import sys
from poe_api_wrapper import PoeApi

# Read the API key from the config.ini file
config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')
api_key = config.get('KEYS', 'POE_KEY')

if api_key == '"YOUR_POE_KEY"':
    raise ValueError(
        "Please replace 'YOUR_POE_KEY' with your actual POE key in the config.ini file.")

client = PoeApi(api_key)

bot = "gpt3_5"
base_prompt = "extract the text from this and do not translate it"

# If a file path is provided in the command line, use it
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    if file_path.endswith(".pdf"):
        pdf_files = [file_path]
    elif file_path.endswith((".jpg", ".png", ".jpeg")):
        image_files = [file_path]
    else:
        raise ValueError(
            "Invalid file type. Please provide a PDF or image file.")
else:
    # Otherwise, get the list of image and pdf files in the current directory
    image_files = [f for f in os.listdir() if f.endswith(
        (".jpg", ".png", ".jpeg"))]
    pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]

# If there are no PDF files in the directory, convert the images to PDF
if not pdf_files and image_files:
    pdf_data = img2pdf.convert(image_files)

    with open("output_pdf.pdf", "wb") as f:
        f.write(pdf_data)
    pdf_files.append("output_pdf.pdf")
elif not pdf_files and not image_files:
    raise ValueError("No PDF or image files found.")

# send each pdf file to the poe api and get the extracted text
for pdf_file in pdf_files:
    for chunk in client.send_message(bot, base_prompt, file_path=[pdf_file]):
        pass
    with open(f"{os.path.splitext(pdf_file)[0]}.txt", "w", encoding="utf-8") as f:
        f.write(chunk["text"])
