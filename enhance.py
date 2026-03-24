from PIL import Image, ImageEnhance
# import an image
image = Image.open('Assets/Insects/2_Sphaer 2021_1_2021_06_03-11-22-54-852.PNG')
# create an enhancer
vibrance_enhancer = ImageEnhance.Color(image)
contrast_enhancer = ImageEnhance.Contrast(image)
brightness_enhancer = ImageEnhance.Brightness(image)
sharpness_enhancer = ImageEnhance.Sharpness(image)
# apply the enhancer
enhanced_image = sharpness_enhancer.enhance(1.5)
# show
image.show()
enhanced_image.show()