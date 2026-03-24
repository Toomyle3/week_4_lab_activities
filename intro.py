from pathlib import Path
from PIL import Image

image_path = Path(__file__).parent / "Assets" / "cat.jpg"
image = Image.open(image_path)

# Print some information about the image
print(image.size)
print(image.filename)
print(image.format)

image.show()

# Flip the cat image horizontally and vertically
flipped_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
flipped_horizontal.show()
flipped_vertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
flipped_vertical.show()

# Rotate the cat image by 90 degrees
rotated_image = image.transpose(Image.Transpose.ROTATE_90)
rotated_image.show()

# exercise
img_rotated = image.rotate(30)
img_rotated.save('img_rotated.png', 'png')