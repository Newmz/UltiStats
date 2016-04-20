from PIL import Image

#This function generates an image we will use for debugging the data. It takes 
#a vector of boolean values named successLines that denotes whether each line of
#the file had an error or not.
def debugging_image(successLines, fname):
	imgLocation = open(fname,"w")
	imgLocation.close()

	height = len(successLines)
	width  = 100
	img = Image.new('RGB', (width, height))
	imgList = []
	red = 255,0,0
	green = 0,255,0
	for line in successLines:
		for i in range(0,width):
			if line:
				imgList.append(green)
			else:
				imgList.append(red)
	#print tuple(imgList)
	img.putdata(tuple(imgList))
	img.save(fname)