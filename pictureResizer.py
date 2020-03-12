from PIL import  Image
import sys
size = 256,256




logic = []

rawInPath = raw_input("Please in put file path :\n")

while rawInPath :

	rawOutPath = r"%s" %rawInPath 
	print '\n:This is '+rawOutPath
	inPath = rawOutPath.replace('\\','/')

	# find index of EXT
	indexIn = rawInPath.index('.')
	# clean name contain for name only etc. noman.mov cleanIn is noman
	cleanIn = (inPath[:indexIn])

	print (cleanIn)

	outPath = cleanIn + '_thumb.PNG'
	 

	print outPath

	im = Image.open(inPath)
	im.thumbnail(size)
	im.save(outPath, 'PNG')
	print 'DONE'


	rawInPath = raw_input("Please in put file path :\n")
	

else:
	print("end progress")
