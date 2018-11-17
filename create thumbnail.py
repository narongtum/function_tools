from PIL import  Image
import sys
size = 256,256




logic = []

logic = raw_input("press enter to continue or press anykey to exit:\n")

while logic == (''):

	#rawInPath =  r'D:\vectorStock\all\asset\2559\07_july\14_gear\final\gear.jpg'

	rawInPath = raw_input("Please in put file path :\n")

	inPath = rawInPath.replace('\\','/')

	print 'this is inPath %s' %inPath

	extPath = inPath.split('/')

	                     
	                    
	outPath = extPath[0] + '/' + extPath[1] + '/' + extPath[2]+'/'+extPath[3]+'/'+extPath[4] +'/'+ extPath[5] +'/'+extPath[6]
	 
	outFile = outPath+'/' + 'thumb.PNG'
	print outFile


	im = Image.open(inPath)
	im.thumbnail(size)
	im.save(outFile, 'PNG')
	print 'DONE'


	logic = raw_input("\npress enter to continue or press anykey to exit:\n")

else:
	print("end progress")




'''

rawInPath = raw_input("Please type path file : \n")





outFile = 'D:/vectorStock/all/asset/2559/07_july/03_abstractA/final/thumb.PNG'


im = Image.open('D:/vectorStock/all/asset/2559/07_july/03_abstractA/final/abstractA.jpg')
im.thumbnail(size)
im.save(outFile, 'PNG')
print 'DONE'










for inFile in sys.argv[1:]:
	outFile = os.path.splitext(inFile)[0] + '.thumbnail'
	if inFile != outFile:
		try:
			im = Image.open(r'D:/vectorStock/all/asset/2559/07_july/02_patternA/final/patternA.jpg')
			im.thumbnail(size)
			im.save(outFile, 'PNG')
			print 'DONE'
		except IOError:
			print 'cannot create thumbnail for', inFile
			'''
