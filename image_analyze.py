from PIL import Image

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

image_path = "Screenshot 2024-02-08 095410.png"
image = Image.open(image_path)

image = image.convert("RGB")

width, height = image.size

pixel_values = []

level = height / 2

for x in range(width):
    pixel = image.getpixel((x, level))
    pixel_values.append(pixel)

# Now pixel_values is a list containing tuples of RGB values for each pixel
print(pixel_values)
bar_start = 0
bar_end = 0
toner_level = 0
# Find where the bar starts
switch = False
switch2 = True
for i in range(len(pixel_values)):
    if pixel_values[i] == BLACK:
        bar_start = i
        break

# Find where the bar ends
for i in range(bar_start, len(pixel_values)):
    if pixel_values[i] == WHITE and switch2:
        toner_level = i
        switch = True
        switch2 = False
    if switch and pixel_values[i] == BLACK:
        bar_end = i
        break

#print start, end, and toner level
print("Bar starts at: ", bar_start)
print("Toner level at: ", toner_level)
print("Bar ends at: ", bar_end)

# Calculate the width of the bar
bar_width = bar_end - bar_start

# Calculate the toner level
toner_level = toner_level - bar_start

# Calculate the percentage of toner left
toner_percentage = (toner_level / bar_width) * 100

print("Toner percentage: ", toner_percentage)


