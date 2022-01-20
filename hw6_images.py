# ----------------------------------------------------------
# --------              HW 6: Images               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Sarah Cryan
# Time spent: 4 hours
# Collaborators and sources: Jaydon 
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


import cImage as image
import os.path


# -------------------------------
# EXAMPLE FUNCTION: RED FILTER
# -------------------------------
# Here is an example of a transformation function. Note that this
# function is called from the main() function below.

def red_filter(img):
    """ (Image object) -> Image object
    Returns a copy of img where the blue and green have been filtered
    out and only red remains.
    """
    red_only_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w): # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel = img.getPixel(x, y)
            red = pixel.getRed() # get original red value
            redPixel = image.Pixel(red, 0, 0)
            red_only_img.setPixel(x, y, redPixel) # replace pixel
    return red_only_img # return filtered image


#--------------------------------
# GRADED FUNCTIONS
#--------------------------------
# Fill in docstrings and code for all of the functions required by the
# homework assignment. For your convenience, each of the function
# definitions have been started for you. However, note that all of the
# functions are currently defined to return None. You will need to change
# that for all of these functions.

## Part 1

def flip_horizontal(img):
    ''' (ImageObject) -> ImageObject
    Returns an image that has been flipped horizontally so the pixels that
    were on the left side are now on the right side.
    '''
    flip_hori_img = img.copy()
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w): # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel = img.getPixel(x,y)
            flip_hori_img.setPixel(w-1-x,y,pixel) # move pixels to opposite x-axis location 
    return flip_hori_img #returns horizontal image


def rotate_clockwise(img):
    ''' (ImageObject) -> ImageObject
    Returns an image that has been rotated 90 degrees to the right,
    so the pixels are reset onto a new image. The new image uses the
    old width as the height and the old height as the width
    '''
    w = img.getWidth()
    h = img.getHeight()
    rotate_img = image.EmptyImage(h,w) #sets the new image so the width is old height & the height is the old width
    for x in range(w): # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel = img.getPixel(x,y)
            rotate_img.setPixel(h-1-y,x,pixel) #resets the pixel. x becomes the height coordinate
            # h-1-y is because: h is out of range, so h-1; h-1-y is so the picture isn't flipped horizontally
            
    return rotate_img #returns rotated image


def to_negative(img):
    ''' (ImageObject) -> ImageObject
    Returns an image that has the negative colors. A negative color is
    255 - however much the original color was on the RGB scale for each
    color. 
    '''
    neg_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w): # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel = img.getPixel(x, y)
            red = pixel.getRed() # get original red value
            green = pixel.getGreen()# get original green value
            blue = pixel.getBlue()# get original blue value
            newPixel = image.Pixel(255-red, 255-green, 255-blue)
            neg_img.setPixel(x, y, newPixel) # replace pixel
    return neg_img # return negative color image
    

def to_grayscale(img):
    ''' (ImageObject) -> ImageObject
    Returns an image in grey scale instead of color. Grey scale occurs
    on the RGB scale when R = G = B. The function gets the RGB of a given
    pixel and finds their average numerical value. Then it sets the pixel
    color to that average for R, G, and B, creating grey-scale colors.
    '''
    gray_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w): # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel = img.getPixel(x, y)
            red = pixel.getRed() # get original red value
            green = pixel.getGreen()# get original green value
            blue = pixel.getBlue()# get original blue value
            avgC = (red+green+blue)//3
            newPixel = image.Pixel(avgC, avgC, avgC) #R,G, and B should be avgC to produce grey-scale
            gray_img.setPixel(x, y, newPixel) # replace pixel
    return gray_img # return grey-scale image


def scale_up(img):
    ''' (ImageObject) -> ImageObject
    Reutns an image that is twice as long and twice as wide as the original
    image. An individual pixel from the original image will correlate to
    4 pixels on the scaled up image.
    '''
    w = img.getWidth()
    h = img.getHeight()
    up_scale = image.EmptyImage(2*w,2*h) #A new image will be created so it is twice as
    #long and wide compared to the original, so w and h must be doubled
    
    for x in range(w): # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel = img.getPixel(x,y)
            red = pixel.getRed() # get original red value
            green = pixel.getGreen()# get original green value
            blue = pixel.getBlue()# get original blue value
            newPixel = image.Pixel(red, green, blue)
            up_scale.setPixel(2*x,2*y,newPixel)#bottom left of the 4 new pixels
            up_scale.setPixel(2*x+1,2*y,newPixel)#top left of the 4 new pixels
            up_scale.setPixel(2*x,2*y+1,newPixel)#bottom right of the 4 new pixels
            up_scale.setPixel(2*x+1,2*y+1,newPixel)#top right of the 4 new pixels
                       
    return up_scale # returns scaled up image



def findAvgPixel(pix1, pix2, pix3, pix4):
    '''(pixel, pixel, pixel, pixel) ->pixel
    Returns the pixel that has the RGB combination
    of the average red, average green, and average blue
    of the 4 pixels for its RBG combination.
    '''
    red = 0
    green = 0
    blue = 0
    pixelList = [pix1,pix2,pix3,pix4] #We discussed that this is acceptable because we have
    #iterated through short lists in class before
    for pixel in pixelList:
        red+=pixel.getRed()
        green+=pixel.getGreen()
        blue+=pixel.getBlue()
        
    avgPixel = image.Pixel(red//4, green//4, blue//4)

    return avgPixel #returns a pixel with the average red, green, blue combination of the 4 pixels


def scale_down(img):
    ''' (ImageObject) -> ImageObject
    Returns an object that is half the width and half the height
    of the original image. 4 pixels will correlate to 1 pixel
    of the scaled down image. To do so properly, the single pixel
    should be the average color of the 4 original pixels.
    
    '''
    w = img.getWidth()
    h = img.getHeight()
    down_scale = image.EmptyImage(w//2,h//2)
    for x in range(w//2): # iterate through all (x, y) pixel pairs
        for y in range(h//2):
            pixel1=img.getPixel(2*x,2*y) # multiply by 2 access the pixels of the original image
            pixel2=img.getPixel(2*x+1,2*y)
            pixel3=img.getPixel(2*x,2*y+1)
            pixel4=img.getPixel(2*x+1,2*y+1)
            newPixel=findAvgPixel(pixel1,pixel2,pixel3,pixel4) #the helper function gets the average pixel 
            down_scale.setPixel(x,y,newPixel)
            
    return down_scale # returns a scaled down image



## Part 2


def merge(img1, img2, img3, img4):
    ''' (ImageObject, ImageObject, ImageObject, ImageObject) -> ImageObject
    Returns an image that merges the four images passed. This image is
    the average picture of the four images.
    '''
    w = img1.getWidth()
    h = img1.getHeight()
    mergeImg = image.EmptyImage(w,h)
    for x in range(w): # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel1=img1.getPixel(x,y)# get the pixel from image 1
            pixel2=img2.getPixel(x,y)# get the pixel from image 2
            pixel3=img3.getPixel(x,y)# get the pixel from image 3 
            pixel4=img4.getPixel(x,y)# get the pixel from image 4
            
            newPixel=findAvgPixel(pixel1,pixel2,pixel3,pixel4)
            #the helper function gets the average pixel 

            mergeImg.setPixel(x,y,newPixel)
            
    return mergeImg # returns the image with the average image of the four images 


## Challenge problem (optional)

def challenge(img):
    ''' (ImageObject) -> ImageObject
    
    '''
    return None


# -------------------------------
# HELPER FUNCTIONS
# -------------------------------
# These functions are provided to help you test your code. They are not graded.

def open_image(fname=None):
    ''' () -> ImageObject or None
    Return an Image object from file name, either given as a parameter or input
    by the user. Return None if the file does not exist or is not a .gif file.
    '''
    # if no filename given, get filename from user
    if not fname:
        fname = input("Enter an image filename: ")

    # check if .gif file
    if not fname[-4:] == '.gif':
        print("Error: "+fname+" is not a .gif file")
        return None

    # check if file does not exists
    if not os.path.exists(fname):
        print("Error: There is no " + fname + " file")
        return None

    # return image from file
    return image.Image(fname)


def display_image(img):
    ''' (ImageObject) -> NoneType
    Display an image. Note: You must click to close the image before the program
    can continue running.
    '''
    w = img.getWidth()
    h = img.getHeight()
    win = image.ImageWin("Image", w, h)
    img.draw(win)
    win.exitonclick()
    return None


def save_image(img, fname):
    ''' (ImageObject, str) -> NoneType
    Save an image to the file fname.
    '''
    img.save(fname)
    return None


#--------------------------------
# BEGIN MAIN FUNCTION
#--------------------------------
# The code below calls all of the transformation functions
# you wrote on the provided .gif files and displays the results.
# You can also test your code using another .gif image of your choice 
# by modifying this function.

def main():
    """ () -> NoneType
    Main Program that load image(s) from file(s) and performs
    transformations to those images as required for this homework. 
    """
    for imgname in ['colgate','rose','grid']:
        original_img = image.Image(f'img/{imgname}.gif')
        red_img = red_filter(original_img)
        display_image(red_img)

        horiz_img = flip_horizontal(original_img)
        if horiz_img is not None:
            display_image(horiz_img)
        else:
            print("incomplete: flip_horizontal is not implemented or still returns None")

        rot_image = rotate_clockwise(original_img)
        if rot_image is not None:
            display_image(rot_image)
        else:
            print("incomplete: rotate_clockwise is not implemented or still returns None")

        neg_image = to_negative(original_img)
        if neg_image is not None:
            display_image(neg_image)
        else:
            print("incomplete: to_negative is not implemented or still returns None")

        gray_img = to_grayscale(original_img)
        if gray_img is not None:
            display_image(gray_img)
        else:
            print("incomplete: to_grayscale is not implemented or still returns None")
        up_img = scale_up(original_img)
        if up_img is not None:
            display_image(up_img)
        else:
            print("incomplete: scale_up is not implemented or still returns None")

        down_img = scale_down(original_img)
        if down_img is not None:
            display_image(down_img)
        else:
            print("incomplete: scale_down is not implemented or still returns None")

    alex = image.Image('img/alex.gif')
    igor = image.Image('img/igor.gif')
    mike = image.Image('img/mike.gif')
    vincent = image.Image('img/vincent.gif')
    merged = merge(alex, igor, mike, vincent)
    if merged is not None:
        display_image(merged)
    else:
        print("incomplete: merge is not implemented or still returns None")


# start the main function, but only if this file is being run "directly"
if __name__ == '__main__':
    main()
