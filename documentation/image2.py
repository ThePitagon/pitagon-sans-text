"""
Author: Travis Tran
Email: tran@travis.guru
Github: travistran1989
Description: Generating a comparison image of two fonts by overlap same code characters.

Copyright 2023 Pitagon., JSC. All rights reserved.
"""
# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ git clone my-font
# $ cd my-font
# $ python3 documentation/image2.py --output documentation/image2.png

# Import modules from external python packages: https://pypi.org/
import math
import string
import argparse

from fontTools.ttLib import TTFont
from PIL import ImageFont, ImageDraw, Image

# Set the size of the font.
FONT_SIZE = 500
FONT_PATH_1 = "sources/release/v1.0.2/ttf/PitagonSansText-Regular.ttf"
FONT_PATH_2 = "fonts/ttf/PitagonSansText-Regular.ttf"
NUM_CHAR_LINE = 20
LINE_GAP = 50
PADDING_TOP = 50
PADDING_RIGHT = 50
PADDING_BOTTOM = 50
PADDING_LEFT = 50

# Handel the "--output" flag
# For example: $ python3 documentation/image2.py --output documentation/image2.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()


def get_unicode_chars(font_path):
    # Load the font using the fontTools library.
    font = TTFont(font_path)

    # Get a list of all the Unicode characters in the font.
    # The getBestCmap() function returns a dictionary that maps character codes to glyph names.
    cmap = font.getBestCmap()
    unicode_chars = [chr(code) for code in cmap.keys()]

    return unicode_chars


def get_max_char_size(font, chars):
    max_width = 0
    max_height = 0

    for char in chars:
        bbox = font.getbbox(char)
        if bbox is not None:
            width = bbox[2] - bbox[0]
            height = abs(bbox[3]) + abs(bbox[1])  # Take the absolute values
            max_width = max(max_width, width)
            max_height = max(max_height, height)

    return max_width, max_height


def generate_comparison_image(font_path1, font_path2, output_path, text=None):
    # Load the two fonts
    font1 = ImageFont.truetype(font_path1, FONT_SIZE)
    font2 = ImageFont.truetype(font_path2, FONT_SIZE)

    # Decide which characters to use.
    if text is None:
        # Use all printable ASCII characters.
        chars1 = set(get_unicode_chars(font_path1))
        chars2 = set(get_unicode_chars(font_path2))
        # Only compare characters that are present in both fonts.
        common_chars = list(chars1 & chars2)
        lines = [''.join(common_chars[i:i + NUM_CHAR_LINE]) for i in range(0, len(common_chars), NUM_CHAR_LINE)]
    elif isinstance(text, list):
        # Break each string in the list into lines based on the NUM_CHAR_LINE.
        lines = [text_line[i:i + NUM_CHAR_LINE] for text_line in text for i in range(0, len(text_line), NUM_CHAR_LINE)]
    else:
        # Break the text into lines based on the NUM_CHAR_LINE.
        lines = [text[i:i + NUM_CHAR_LINE] for i in range(0, len(text), NUM_CHAR_LINE)]
    print(f"Input: {lines}")
    print(f"Drawing...")
    max_chars_per_line = max(len(line) for line in lines)
    # print(f"max_chars_per_line: {max_chars_per_line}")
    num_lines = len(lines)
    # print(f"num_lines: {num_lines}")

    # Calculate the size of the image based on the number of characters and the size of the characters.
    max_width1, max_height1 = get_max_char_size(font1, ''.join(lines))
    max_width2, max_height2 = get_max_char_size(font2, ''.join(lines))
    char_width = max(max_width1, max_width2)
    char_height = max(max_height1, max_height2)
    # print(f"char_width: {char_width}, char_height: {char_height}")
    # The width of the image is the number of characters per line times the character width.
    image_width = PADDING_LEFT + max_chars_per_line * char_width + PADDING_RIGHT
    # The height of the image is the number of lines times the line height (character height plus line gap).
    image_height = PADDING_TOP + num_lines * char_height + (num_lines - 1) * LINE_GAP + PADDING_BOTTOM
    # print(f"image_width: {image_width}, image_height: {image_height}")

    # Create two new images, one for each text layer.
    layer1 = Image.new('RGBA', (image_width, image_height), (255, 255, 255, 0))  # Use RGBA for transparency.
    layer2 = Image.new('RGBA', (image_width, image_height), (255, 255, 255, 0))

    draw1 = ImageDraw.Draw(layer1)
    draw2 = ImageDraw.Draw(layer2)

    # Draw each character at the correct position.
    y = PADDING_TOP
    for i, line in enumerate(lines):
        x = PADDING_LEFT
        for j, char in enumerate(line):
            # print(f"Draw text {char} at {x}, {y}")
            draw1.text((x, y), char, fill=(0, 255, 0, 128), font=font1)
            draw2.text((x, y), char, fill=(255, 0, 255, 128), font=font2)
            x += char_width
        y += LINE_GAP + char_height

    # Blend the images together and save the result.
    output = Image.alpha_composite(layer1, layer2)
    output.save(output_path)


# Build and save the image
if __name__ == "__main__":
    output = args.output
    # If you don't provide the lines parameter, the function will generate an image that contains all characters that
    # are present in both fonts, arranged in lines of up to NUM_CHAR_LINE characters:
    # generate_comparison_image(FONT_PATH_1, FONT_PATH_2, output)

    # If you provide a single string, the function will generate an image that contains these characters, arranged in
    # lines of up to NUM_CHAR_LINE characters:
    # generate_comparison_image(FONT_PATH_1, FONT_PATH_2, output, "ABCDEFGH")
    # If the string is longer than NUM_CHAR_LINE characters, it will be split into multiple lines:
    generate_comparison_image(FONT_PATH_1, FONT_PATH_2, output, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # If you provide a list of strings, the function will generate an image with each string on a separate line:
    # generate_comparison_image(FONT_PATH_1, FONT_PATH_2, output, ["ABC", "DEF", "GHI"])
    # If a string in the list is longer than NUM_CHAR_LINE characters, it will be split into multiple lines:
    # generate_comparison_image(FONT_PATH_1, FONT_PATH_2, output,
    #                           ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKL", "MNOPQRSTUVWXYZ"])
    # Alphabet Characters
    # generate_comparison_image(FONT_PATH_1, FONT_PATH_2, output,
    #                           ["A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",
    #                            "a b c d e f g h i j k l m n o p q r s t u v w x y z"])
    # Numeric Characters
    # generate_comparison_image(FONT_PATH_1, FONT_PATH_2, output, ["0 1 2 3 4 5 6 7 8 9"])
    # Symbol Characters
    # generate_comparison_image(FONT_PATH_1, FONT_PATH_2, output,
    #                           [". , ? ! ; : ' \" ( ) [ ] { } - – — ... ·",
    #                            "+ - = * / < > ^ ~",
    #                            "$ € £ ¥ ¢",
    #                            "& @ # % _ | \ ` ¨ ´ °"])
    # Extended Characters
    # generate_comparison_image(FONT_PATH_1, FONT_PATH_2, output, ["é è ê ë á à â ä ñ ö ü ï ô û", "ç õ ò ì í î"])
    # Ligatures and Typographical Features
    # generate_comparison_image(FONT_PATH_1, FONT_PATH_2, output, ["ff fi fl ffi ffl"])

    print("Characters Comparison: Done")
