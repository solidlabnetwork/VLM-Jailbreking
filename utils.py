from platform import processor
from xml.parsers.expat import model
from PIL import Image, ImageDraw, ImageFont
import textwrap
import torch



def create_photocard_with_caption(test_image, title_text, malicious_caption):
    """Create a photocard with a large, clear caption and no extra padding."""
    from PIL import ImageFont

    img_width, img_height = test_image.size

    # Try to use FreeMono Bold, fallback to default
    try:
        font_path = "FreeMonoBold.ttf"
        caption_font = ImageFont.truetype(font_path, 14)
        title_font = ImageFont.truetype(font_path, 20)
    except:
        caption_font = ImageFont.load_default()
        title_font = ImageFont.load_default()

    # Estimate caption height (2 lines for title + caption, adjust as needed)
    dummy_img = Image.new('RGB', (img_width, 1000))
    draw = ImageDraw.Draw(dummy_img)
    title_height = draw.textsize(title_text, font=title_font)[1]
    # Word wrap caption to fit image width
    import textwrap
    wrapped_caption = textwrap.fill(malicious_caption, width=60)
    caption_lines = wrapped_caption.split('\n')
    caption_height = sum([draw.textsize(line, font=caption_font)[1] for line in caption_lines])

    total_height = img_height + title_height + caption_height + 20  # 20px spacing

    # Create new image
    photocard = Image.new('RGB', (img_width, total_height), (255, 255, 255))
    photocard.paste(test_image, (0, 0))

    draw = ImageDraw.Draw(photocard)
    # Draw title centered
    title_w, title_h = draw.textsize(title_text, font=title_font)
    draw.text(((img_width - title_w) // 2, img_height + 5), title_text, fill=(60, 60, 60), font=title_font)

    # Draw caption below title
    y_pos = img_height + 5 + title_h + 10
    for line in caption_lines:
        line_w, line_h = draw.textsize(line, font=caption_font)
        draw.text(((img_width - line_w) // 2, y_pos), line, fill=(80, 80, 80), font=caption_font)
        y_pos += line_h

    return photocard

