from PIL import Image

# Open the .tif image
image_path = 'snimci/LC08_L2SP_186029_20220701_20220708_02_T1_SR_B4.TIF'
image = Image.open(image_path)

# Display the image
image.show()

# Print some basic information about the image
print(f"Image format: {image.format}")
print(f"Image size: {image.size}")
print(f"Image mode: {image.mode}")
