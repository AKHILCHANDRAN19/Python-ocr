import os
from PIL import Image
import pytesseract

# Path to the Download folder
download_folder = '/storage/emulated/0/Download/'

# List of supported image extensions
supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# Process each file in the Download folder
for filename in os.listdir(download_folder):
    if filename.lower().endswith(supported_extensions):
        file_path = os.path.join(download_folder, filename)
        
        try:
            # Open the image file
            with Image.open(file_path) as img:
                # Perform OCR on the image
                text = pytesseract.image_to_string(img)
                
                # Print the extracted text
                print(f"Extracted Text from {filename}:")
                print(text)
                print("-" * 40)
        except Exception as e:
            print(f"Could not process {filename}: {e}")
