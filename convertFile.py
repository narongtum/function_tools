import sys
from PyQt4 import QtGui, QtCore
import os
import subprocess



FFMPEG = r'C:\\ffmpeg-20140629-git-8657612-win64-static\\bin\\ffmpeg.exe'
inPath = []
def convertFile(filePath):
	print filePath
	inPath = str(filePath)
	# find index of EXT
	indexIn = inPath.index('.')
	# clean name contain for name only etc. noman.mov cleanIn is noman
	cleanIn = (inPath[:indexIn])
	print (cleanIn)
	outPath = cleanIn + '_small.mov'
	print 'input path is %s' %inPath
	cmd ='%s -y -i %s -vcodec libx264 -vprofile baseline -crf 22 -bf 0 -pix_fmt yuv420p -f mov %s' %( FFMPEG , inPath , outPath)
	subprocess.call(cmd)
	print('\nconverted path file is ' +str(outPath))




# add drap and drop behavior
class Button(QtGui.QPushButton):
	def __init__(self, parent):
		super(Button, self).__init__(parent)
		self.setAcceptDrops(True)
		#self.setDragDropMode(QAbstractItemView.InternalMove)

	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.acceptProposedAction()
		else:
			super(Button, self).dragEnterEvent(event)

	def dragMoveEvent(self, event):
		super(Button, self).dragMoveEvent(event)


	def dropEvent(self, event):
		if event.mimeData().hasUrls():
			for url in event.mimeData().urls():
				#print str(url.toLocalFile())
				filePath = url.toLocalFile()
				convertFile( filePath )
			event.acceptProposedAction()
		else:
			super(Button,self).dropEvent(event)


class MyWindow(QtGui.QWidget):
	def __init__(self):
		super(MyWindow,self).__init__()
		#self.setGeometry(100,100,300,400)
		self.setGeometry(400,400,160,160)
		self.setWindowTitle("nomanFFMPEG converter")

		self.btn = Button(self)
		#self.btn.setGeometry(QtCore.QRect(90, 90, 61, 51))
		self.btn.setGeometry(QtCore.QRect(400, 400, 160, 160))
		self.btn.setText("Drop file here")
		layout = QtGui.QVBoxLayout(self)
		layout.addWidget(self.btn)
		self.setLayout(layout)











if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	window = MyWindow()
	window.show()
	sys.exit(app.exec_())
