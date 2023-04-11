from PIL import Image
import os

folder_path = "palm"
files = os.listdir(folder_path)

for file_name in files:
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
        image_path = os.path.join(folder_path, file_name)
        image = Image.open(image_path)
        rotated_image = image.rotate(180)
        rotated_image_path = os.path.join(folder_path, "rotated_" + file_name)
        rotated_image.save(rotated_image_path)
        print(f"{file_name} is rotated and saved as {rotated_image_path}")
