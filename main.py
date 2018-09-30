from PIL import Image
import numpy as np
import random

def rgb_to_hex(rgb_vals):
    return '{:02x}{:02x}{:02x}'.format(*rgb_vals)

def hex_to_rgb(hex_val):
    rgb_vals = []
    for i in range(0, 3):
        num = int(hex_val[2*i: 2*i + 2], 16)
        rgb_vals.append(num)
    
    return np.array(rgb_vals)

def flood_fill(hex_array, x, y, color, tol):

    if hex_array[x, y] != "ffffff":
        return

    q = []
    hex_array[x, y] = color
    q.append((x, y))

    while len(q) != 0:
        a, b = q.pop()
        if (b - 1) > 0 and hex_array[a, b - 1] == "ffffff":
            hex_array[a, b - 1] = color
            q.append((a, b - 1))
        
        if (b + 1) < hex_array.shape[1] and hex_array[a, b + 1] == "ffffff":
            hex_array[a, b + 1] = color
            q.append((a, b + 1))
        
        if (a - 1) > 0 and hex_array[a - 1, b] == "ffffff":
            hex_array[a - 1, b] = color
            q.append((a - 1, b))
        
        if (a + 1) < hex_array.shape[0] and hex_array[a + 1, b] == "ffffff":
            hex_array[a + 1, b] = color
            q.append((a + 1, b))

    return

    

def color_image(hex_array):
    for x in range(hex_array.shape[0]):
        for y in range(hex_array.shape[1]):
            if hex_array[x, y] == 'ffffff':
                tol = int('d3d3d3', 16)
                rand_color = [random.randint(0, 255) for i in range(0, 3)]
                color = rgb_to_hex(rand_color)
                flood_fill(hex_array, x, y, color, tol)


def main():
    img = Image.open("data/test5.png").convert('RGB')
    img_array = np.array(img)

    hex_array = np.apply_along_axis(rgb_to_hex, 2, img_array)

    color_image(hex_array)

    rgb_array = np.zeros(img_array.shape)
    
    for x in range(hex_array.shape[0]):
        for y in range(hex_array.shape[1]):
            rgb_array[x, y, ] = hex_to_rgb(hex_array[x, y])

    new_img = Image.fromarray(rgb_array.astype('uint8'), 'RGB')
    new_img.show()
    new_img.save('result.jpg')

    

if __name__ == "__main__":
    main()
    