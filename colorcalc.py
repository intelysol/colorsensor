# importing image object from PIL
import math
import struct
from PIL import Image, ImageDraw

R = 20270
G = 6184
B = 2031

RGBInt = R+G+B

# bitColor_16 = ((bitColor_8 + 1)*256) - 1
# 16 bit color value to 8 bit RGB color
B_bitColor_16 = int(B / 128)
G_bitColor_16 = int(G / 128)
R_bitColor_16 = int(R / 128)

print("Red: ", "Green: ", "Blue: ")
print(R_bitColor_16, G_bitColor_16, B_bitColor_16)

# 16 bit color to 8 bit rgb color value
B = B >> 7
G = G >> 7
R = R >> 7

print(R, G, B)

w, h = 220, 190
shape = [(40, 40), (w - 10, h - 10)]

# creating new Image object
img = Image.new('RGB', (500, 300), (128, 128, 128))

# create  rectangleimage
img1 = ImageDraw.Draw(img)
img1.rectangle(shape, fill=(R, G, B), outline="green")
img.show()


# def distance(c1, c2):
#     (r1,g1,b1) = c1
#     (r2,g2,b2) = c2
#     return math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)

# colors = list(rgb_code_dictionary.keys())
# closest_colors = sorted(colors, key=lambda color: distance(color, point))
# closest_color = closest_colors[0]
# code = rgb_code_dictionary[closest_color]


# private fun isMatchingColor(intColor1: Int, intColor2: Int, percent: Int = 90): Boolean {
#     val threadSold = 255 - (255 / 100f * percent)

#     val diffAlpha = abs(Color.alpha(intColor1) - Color.alpha(intColor2))
#     val diffRed = abs(Color.red(intColor1) - Color.red(intColor2))
#     val diffGreen = abs(Color.green(intColor1) - Color.green(intColor2))
#     val diffBlue = abs(Color.blue(intColor1) - Color.blue(intColor2))

#     if (diffAlpha > threadSold) {
#         return false
#     }

#     if (diffRed > threadSold) {
#         return false
#     }

#     if (diffGreen > threadSold) {
#         return false
#     }

#     if (diffBlue > threadSold) {
#         return false
#     }

#     return true
# }
