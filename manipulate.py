from PIL import Image

# import an image
image = Image.open('Assets/Insects/1_Gammar 2021_1_2021_06_03-13-19-23-879.PNG')
#  flip
image_transpose = image.transpose(Image.Transpose.ROTATE_90)
# rotation
image_rotate = image.rotate(45, expand = False, center = (0,0))
# crop
image_crop = image.crop((800,600,1600,1600))
# resize
image_resize = image.resize((1000,600))
# applying multiple transformations to an image in a single line of
#code
combined_image = image.transpose(Image.Transpose.ROTATE_90).resize((2000,1500)).rotate(10)
combined_image.show()