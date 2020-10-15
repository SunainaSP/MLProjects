from PIL import Image, ImageEnhance
img = Image.open("Sample3.jpeg")
img_con = ImageEnhance.Bri(img)
img_con.enhance(1.0).show("100% more contrast")
