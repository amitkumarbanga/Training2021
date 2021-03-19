# List of List of List
# RGB Color

pixel1 = [312, 0, 84]
pixel2 = [165, 556, 15]
pixel3 = [385, 510, 45]
pixel4 = [552, 915, 455]
pixel5 = [382, 122, 545]
pixel6 = [785, 200, 156]
pixel7 = [115, 100, 51]
pixel8 = [592, 841, 80]
pixel9 = [889, 78, 865]

image = [[pixel1, pixel2, pixel3],
          [pixel4, pixel5, pixel6],
          [pixel7, pixel8, pixel9]]

print(len(image))
print(len(image[0]))
print(len(image[0][0]))
print(image[0][1])

print("IMAGE")
for pixels in image:
    for pixel in pixels:
        print(pixel, end="\n")

print()
