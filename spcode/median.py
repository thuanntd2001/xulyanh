import Image, array, math, time
import psyco   # use optimizer - comment out these two
psyco.full()   # lines to deactivate the optimizer
# fast implementation:
def quantile(lst, f=0.5):
    """Returns the f%-quantile of a list. Returns the median for f=0.5. 
    Works only if all list members are integers in the range 0..255!"""
    l,r = 0,256
    targetCount = int(len(lst)*f)
    while l+1 < r:
        m = (l+r)/2
        count = 0
        for x in lst:
            if x < m: count += 1
        if count <= targetCount:
            l = m
        else:
            r = m
    return l
   
def filter(img):
    """filters a region of an image with a circular-shaped median/quantile filter.
    Takes a PIL-Image as parameter and returns the filtered image."""
    # extract access variables from image
    src = array.array('B', img.getdata())
    dst = array.array('B', img.getdata())
    w,h = img.size
    r = 10
    mask = []
    for dy in range(-r, r+1):
        dx = int(math.sqrt(r*r-dy*dy))
        for x in range(-dx,dx+1):
            mask += [(x,dy)]
    print(mask)
 # calculare address offsets for mask coordinates
    maskOfs = [x+w*y for x,y in mask]
    pixelsInMask = [0]*len(mask)
    starttime = time.clock()
    pixelsProcessed = 0
    # image processing loop
    for y in range(0+r,h-r):
        elapsed = time.clock()-starttime
        if elapsed > 0.1 and y % 10 == 0:
            print ("Applying filter: %3i / %3i: %0.2f %%; %0.1f p/s\r" % (y, h, (y-r)*100.0/(h-r*2), pixelsProcessed/elapsed))
        for x in range(0+r,w-r):
             # filter kernel
            i = 0
            # gather all the pixels in the filter mask into to pixelsInMask list
            base = x+y*w
            for ofs in maskOfs:	
                pixelsInMask[i] = src[base+ofs]
                i += 1
                dst[x+y*w] = quantile(pixelsInMask, 0.5)
                pixelsProcessed += 1

    imgDest = img.copy()
    imgDest.putdata(dst)
    print
    return imgDest

if __name__=="__main__":
    img = Image.open("your-bitmap-here.bmp")
    imgDest = filter(img)
    imgDest.show()


