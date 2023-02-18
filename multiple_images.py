#glob (short for global) is used to return all file paths that match a specific pattern.
#We can use glob to search for a specific file pattern, or perhaps more usefully, search for
#files where the filename matches a certain pattern by using wildcard characters
import glob
import PIL
import os
import matplotlib.pyplot as plt
from PIL import Image
file = 'C:\\Users\\barry\\Desktop\\bkkk\\bk\\*' #file = 'C:\\Users\\barry\\Desktop\\bkkk\\bk\\*.png' #for png files
glob.glob (file)
print (glob.glob(file))
print ('\t')


images = [Image.open (image) for image in glob.glob (file)] #list comprehension
# plt.imshow (images[5]) #here we try to plot the sixth image in the file to verify

#VISUALIZATION THROUGH ITERATION
print ('VISUALIZING MULTIPLE IMAGES')
rows = 2
cols = 3
plt.figure(figsize = (5,5))
for i in range (0, rows*cols):
    plt.subplot (rows, cols, i+1)
    plt.imshow (images[i])

plt.subplots_adjust(left=0.1,
                    bottom=0.5,
                    right=1.5,
                    top=1.5,
                    wspace=0.4,
                    hspace=0.4)
