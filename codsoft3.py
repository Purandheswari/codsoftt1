import urllib.request
from PIL import Image, ImageDraw, ImageFont
import os

def get_caption(image_url):
  try:
    filename, _ = os.path.splitext(os.path.basename(image_url))
    filename = filename.upper()  # Ensure uppercase for extension check

    # Download image
    urllib.request.urlretrieve(image_url, filename)

    # Open image and convert to RGB mode if necessary
    img = Image.open(filename)
    if not img.mode == 'RGB':
        img = img.convert('RGB')

    # Add caption with consistent formatting
    draw = ImageDraw.Draw(img)
    font_path = "Arial Bold.ttf"  # Replace with your desired font path
    font_size = 35
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = draw.textsize("Your Caption Here", font=font)
    x = (img.width - text_width) // 15 + 25  # Consistent padding
    y = img.height - 100  # Position at the bottom

    draw.text((x, y), "Your Caption Here", (255, 0, 0), font=font)  # Red color

    # In this case, we don't save the image, so return it directly
    return img

  except Exception as e:
    print(f"Error processing image '{filename}': {e}")
    return None

# Example usage (replace with your image URL)
image_url = "https://dfstudio-d420.kxcdn.com/wordpress/wp-content/uploads/2019/06/digital_camera_photo-1080x675.jpg"
captioned_image = get_caption(image_url)

if captioned_image:
  # You can now display the captioned image using libraries like OpenCV or PIL's show() method
  captioned_image.show()  # Example using PIL's show()
else:
  print("Error processing image.")
