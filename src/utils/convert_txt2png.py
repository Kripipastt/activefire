from PIL import Image


def convert_txt_to_png(txt_file_path, png_file_path):
    try:
        with open(txt_file_path, 'r') as f:
            lines = f.readlines()

        lines = [line.strip().replace(" ", "") for line in lines]

        width = len(lines[0])
        height = len(lines)

        img = Image.new('L', (width, height))

        for y in range(height):
            for x in range(width):
                pixel_value = int(lines[y][x])
                color = 0 if pixel_value == 0 else 255
                img.putpixel((x, y), color)

        img.save(png_file_path)
        print(f"Save image from: {png_file_path}")

    except Exception as e:
        print(f"Error: {e}")


txt_file = 'input.txt'
png_file = 'output.png'

convert_txt_to_png(txt_file, png_file)