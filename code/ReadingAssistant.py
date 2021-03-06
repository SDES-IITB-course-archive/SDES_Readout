#!/usr/env python

import ReadAssist as ReadAssist
from underlined_word_extract import UnderlinedWordExtract
import os
import time
import sys


while True:
	myText = UnderlinedWordExtract()
	myReader = ReadAssist.ReadAssist()
	#myUnderline = Sonal underline class()
####Wait for start
	os.system('clear')
	print "Enter 1 to start the Read Assister"
	start = raw_input()

	if (start == '1'):

#Step 1: ##Capture Image
		if sys.argv[2] == 'C':
			myReader.ClickPic()  #Image saved in clicked.bmp

#Step 2: ##Convert to complete text
		myReader.ConverttoText(sys.argv[1], "fulltext.txt")
		
#Step 3: ##Extract out underline and convert to text with another name
	#myUnderline.detectunderline("clicked.bmp")
		if sys.argv[2] != 'C':
			myText.extract_underlined_text(sys.argv[1],"underlined.bmp")

		if sys.argv[2] == 'C':
			myReader.ConverttoText(sys.argv[1], "underlined.txt")	
		else:
			myReader.ConverttoText("underlined.bmp", "underlined.txt")	
#myReader.ConverttoText("Extractedpic","underlined.txt")

#Step 4: #Read from the underlined file and pass the string to a variable data as shown

		with open ("underlined.txt", "r") as myfile:
    			data=myfile.read().replace('\n', '')


#Step 5 ##Ask for user options
		print "Enter 1 for reading entire text, 2 for meaning, 3 for wiki, 4 for image"
		mychoice = raw_input()
## Options 

#1. Read the entire text : Call The SpeachtoText
#Exit and let the loop continnue
		if(mychoice == '1'):
			myReader.SpeakText("fulltext.txt")
			time.sleep(6)


#2. Meaning : Call the meaning function and pass data
#This function writes data to meaning.txt file
#Call SpeechtoText on this file and read out
#Exit and let the loop continnue
		elif(mychoice == '2'):
			myReader.GetMeaning(data)
			myReader.SpeakText("meaning.txt")
			time.sleep(6)


#3. Wiki :Call the wiki function and pass data
#This function writes data to wiki.txt file
#Call SpeechtoText on this file and read out
#Exit and let the loop continnue
		elif(mychoice == '3'):
			myReader.GetWiki(data)
			myReader.SpeakText("wiki.txt")
			time.sleep(6)


#4 Image : Call Image function followed by Image show
#Exit and let the loop continnue
		elif(mychoice == '4'):
			myReader.GetImage(data)
			myReader.ShowImage()
		

##Let the loop continue
	else:
		continue
	del myReader
	del myText
#Now call 
