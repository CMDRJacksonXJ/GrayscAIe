from PIL import Image
from numpy import ravel
from numpy import asarray

r = 0
comparison_iteration = 0
unsureness_cross = 0
unsureness_circle = 0
unsureness_rtld = 0
unsureness_bfcheckerboard = 0
unsureness_grayscale = 0
reg1 = 0.0
reg2 = 0.0
reg3 = 0.0
pixel_count = 16
take = []
results_list = []
minimum_result = 0
min_index = 0

img = Image.open('input.png')
image_as_list = asarray(img)
# Make sure the input image is named "input.png" and is a 4x4 image.
# Neural Network:
# Give it a 4x4 grayscale image and it will decide whether it is a circle or cross.
cross_pixels = [0, 253, 253, 0, 253, 0, 0, 253, 253, 0, 0, 253, 0, 253, 253, 0]
circle_pixels = [253, 0, 0, 253, 0, 253, 253, 0, 0, 253, 253, 0, 253, 0, 0, 253]
rtld_pixels = [253, 253, 253, 0, 253, 253, 0, 253, 253, 0, 253, 253, 0, 253, 253, 253]
bfcheckerboard_pixels = [0, 253, 0, 253, 253, 0, 253, 0, 0, 253, 0, 253, 253, 0, 253, 0]
grayscale_pixels = [253, 253, 125, 125, 253, 125, 125, 125, 125, 125, 125, 0, 125, 125, 0, 0]
# Note: Due to floating point shenanigans, the max. grayscale color-value is 253 rather than 255.
raveled_list = (ravel(image_as_list))
while r < pixel_count:
    reg1 = raveled_list[(4 * r) + 0]
    reg2 = raveled_list[(4 * r) + 1]
    reg3 = raveled_list[(4 * r) + 2]
    take.append(reg1 + reg2 + reg3)
    r += 1


while comparison_iteration < pixel_count:
    unsureness_circle += abs(circle_pixels[comparison_iteration] - take[comparison_iteration])
    unsureness_cross += abs(cross_pixels[comparison_iteration] - take[comparison_iteration])
    unsureness_rtld += abs(rtld_pixels[comparison_iteration] - take[comparison_iteration])
    unsureness_bfcheckerboard += abs(bfcheckerboard_pixels[comparison_iteration] - take[comparison_iteration])
    unsureness_grayscale += abs(grayscale_pixels[comparison_iteration] - take[comparison_iteration])

    comparison_iteration += 1

results_list.append(unsureness_circle)
results_list.append(unsureness_cross)
results_list.append(unsureness_rtld)
results_list.append(unsureness_bfcheckerboard)
results_list.append(unsureness_grayscale)
minimum_result = min(results_list)
min_index = results_list.index(minimum_result)

if min_index == 0:
    print("Input image is a Circle")
    print("Unsureness: " + str(unsureness_circle / 100))
if min_index == 1:
    print("Input image is a Cross")
    print("Unsureness: " + str(unsureness_cross / 100))
if min_index == 2:
    print("Input image is a Right-To-Left Diagonal")
    print("Unsureness: " + str(unsureness_rtld / 100))
if min_index == 3:
    print("Input image is a Black-first Checkerboard")
    print("Unsureness: " + str(unsureness_bfcheckerboard / 100))
if min_index == 4:
    print("Input image is a Grayscale")
    print("Unsureness: " + str(unsureness_grayscale / 100))

print("\n")
print("Unsureness for all shapes:")
print("Circle: " + str(unsureness_circle / 100))
print("Cross: " + str(unsureness_cross / 100))
print("Right-To-Left Diagonal: " + str(unsureness_rtld / 100))
print("Black-first Checkerboard: " + str(unsureness_bfcheckerboard / 100))
print("Grayscale: " + str(unsureness_grayscale / 100))
