# python 3
import datetime
import pyperclip

# Note
# add year 

# install pyper here
# C:\Python27\Scripts>pip.exe install pyperclip

date = datetime.datetime.now()
currentDate = date.strftime('%y.%m.%b.%d.%a_')
print (currentDate)
pyperclip.copy(currentDate)





