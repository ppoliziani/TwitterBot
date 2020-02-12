import random, sys, datetime, time


def setup():
    size(800, 800)
    # Before we deal with pixels
    loadPixels()
    changePixels()


def changePixels():
    for x in range(width):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        # Loop through every pixel row
        for y in range(height):
            # Use the formula to find the 1D location
            loc = x + y * width;
            if (x % 2 == 0):  # If we are an even column
                pixels[loc] = color(r, g, b)
            else:  # If we are an odd column
                pixels[loc] = color(r, g, b)

    # When we are finished dealing with pixels
    updatePixels()
    # daily saveing -> saveFrame(str(datetime.datetime.now().date()) + ".jpg")
    saveFrame(("Pictures\ " + str(datetime.datetime.now().time().strftime('%H:%M')) + ".jpg").replace(":", "-"))

    time.sleep(2)
    sys.exit()

