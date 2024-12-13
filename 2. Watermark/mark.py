from PIL import Image, ImageDraw, ImageFont

# Load the image
image = Image.open("../1. digital-signature/udom.jpg")

# Create a drawing context
draw = ImageDraw.Draw(image)

# Set the watermark text and font
watermark_text = input("Write the Digital Signature: ")

font = ImageFont.truetype("arial.ttf", size=36)

# Get the width of the watermark text
text_length = draw.textlength(watermark_text, font=font)

# To get both width and height, we use textbbox
bbox = draw.textbbox((0, 0), watermark_text, font=font)
text_width = bbox[2] - bbox[0]  # width is the difference between right and left
text_height = bbox[3] - bbox[1]  # height is the difference between top and bottom

# Position for watermark
width, height = image.size
position = (width - text_width - 10, height - text_height - 10)

# Add watermark
draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)

# Save the image
image.save("watermarked_photo.jpg")

