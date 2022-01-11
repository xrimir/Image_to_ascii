import math
import sys
from PIL import Image


class ImageFile:
    def __init__(self):
        self.image_path = sys.argv[1]
        self.image = Image.open(self.image_path)
        self.image_width, self.image_height = self.image.size
        self.ratio = self.image_height / self.image_width
        self.pixels = self.image.getdata()
        self.ascii_img = ""
        self.grayscale = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '

    def set_image_width(self, width):
        self.image_width = width

    def set_image(self, image_object):
        self.image = image_object

    def set_pixels(self, image_pixels):
        self.pixels = image_pixels

    def resize_image(self, new_image_width=200):
        self.set_image(self.image.resize((new_image_width, int(new_image_width * self.ratio))))
        self.set_pixels(self.image.getdata())
        self.set_image_width(new_image_width)

    def get_character(self, y):

        # gray_step = 255 / len(self.grayscale)
        # result = math.floor(y / gray_step)
        return self.grayscale[math.floor(len(self.grayscale) * y / 255)]

    def image_ascii_to_file(self, filename):
        f = open(filename, 'w')
        f.write(self.ascii_img)
        f.close()

    def image_to_ascii(self):
        counter = 1
        for pixel in self.pixels:
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            y = math.floor(0.2627 * r + 0.67 * g + 0.06 * b)
            self.ascii_img += self.get_character(y)
            if counter % self.image_width == 0:
                self.ascii_img += "\n"
            counter += 1


img = ImageFile()
img.resize_image()
img.image_to_ascii()
img.image_ascii_to_file("ascii_image.txt")
