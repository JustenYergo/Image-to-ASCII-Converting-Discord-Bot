import PIL.Image
import urllib.request

class AsciiConvert(object):
  
  def __init__(self):
    self._url = None

  @property
  def url(self):
    return self._url

  @url.setter
  def url(self, value):
    self._url = value

  @url.deleter
  def url(self):
    del self._url
  
#converter functiom
def ascii_converter(url):
  urllib.request.urlretrieve("{0}".format(url), "new.jpg")
 
  img_flag = True
  path="new.jpg"

  try: 
    img = PIL.Image.open(path)
    img_flag = True
  except:
    print(path, "Unable to find image ");
 
  width, height = img.size
  aspect_ratio = height/width
  new_width = 50
  new_height = aspect_ratio * new_width * 0.55
  img = img.resize((new_width, int(new_height)))
 
  img = img.convert('L')
 
  chars = ["█", "█", "▓", "▓", "▒", "▒", "░", "░", "░", "─", "─"]
 
  pixels = img.getdata()
  new_pixels = [chars[pixel//25] for pixel in pixels]
  new_pixels = ''.join(new_pixels)
  new_pixels_count = len(new_pixels)
  ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
  ascii_image = "\n".join(ascii_image)
 
  with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)
