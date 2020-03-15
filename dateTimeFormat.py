# python 3
import datetime
import pyperclip


# install pyper here
# C:\Python27\Scripts>pip.exe install pyperclip

date = datetime.datetime.now()
currentDate = date.strftime('%m.%b.%d.%a_')
print (currentDate)
pyperclip.copy(currentDate)
