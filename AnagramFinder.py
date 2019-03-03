from tkinter import *
from string import ascii_lowercase
import time

window=Tk()

PrimeNumDict = {'é':163,'!':157,'\'':151,'-':149,' ':139,'q':137,'w':131,'x':127,'y':113,'z':109,'c':107,
	'ž':103, 'þ':103, 'ð':101,'š':101,'f':97,'ö':89,'b':83,'ü':79,'j':73,'õ':71,'ä':67,'g':61,'h':59,
	'd':53,'v':43,'p':41,'o':37,'m':31,'n':29,'r':23,'k':19,'l':17,'u':13,'t':11,'s':7,'e':5,'i':3,'a':2
	}

def iteratelemmad():
	start = time.time()
	global list_word
	list_word=[]
	global list_key
	list_key=[]
	global input_key
	input_key=1
	global list_positions
	list_positions=[]


	with open("lemmad.txt") as ite:
		with open("uniquekeylist.txt", "w") as ote:
			for line in ite:
				line=line.strip()
				line=line.lower()

				wordkey=1

				for i in line:

					numW = weightnumber(i)
					wordkey=wordkey*numW
				
				ote.write(str(wordkey)+"\n")
	
	list_word=listlemmad()
	
	list_key=listkeys()
	
	input_key=generateInputKey()
	
	list_positions=keyPosition()
	global word_match
	word_match=[]
	if list_positions==None:
		pass
	else:
		word_match=wordsForPositions()
	end = time.time()
	totaltime=(end - start)
	if word_match==None:
		pass
	else:
		for i in word_match:
			t1.insert(END,word_match)
			t1.insert(END,"\n")
			print(word_match)
	print(totaltime)
	t1.insert(END,"Time Taken: ")
	t1.insert(END,totaltime)
	t1.insert(END," seconds\n")

def listlemmad():
	with open("lemmad.txt") as lemmad:
		oriWordList = []
		for line in lemmad:
			line=line.rstrip('\n')
#			line=str(line.lower())
			oriWordList.append(line) #ADDED word 2 oriWordList 4m text file. We will use this, not text file
	return oriWordList

def listkeys():
	with open("uniquekeylist.txt") as uniquekeylist:
		oriKeyList = []
		for line in uniquekeylist:
			line=line.rstrip('\n')
			line=str(line.lower())
			oriKeyList.append(line) #ADDED word 2 oriKeyList 4m text file. We will use this, not text file
	return oriKeyList

def generateInputKey():
	global input_word
	input_word=input_word_here.get()
	input_word1=input_word.lower()
	input_word=input_word1.strip()
	try:
		if len(input_word)<1:
			t1.insert(END,"No word entered\n") #if no input word = then this
		else:
			input_word_key=1 
			for i2 in input_word:
				char_key = weightnumber(i2)
				input_word_key = input_word_key*char_key
			input_word_key = str(input_word_key) #calculated key of inputed word
			return (input_word_key)
	except KeyError as error:
		t1.insert(END,"Input contains an ALIEN Alphabet / Character\n")

def wordsForPositions():
	words_for_key = []
	for i in list_positions:
		word_for_key = list_word[i]
		if list_word[i].lower() != input_word:
			words_for_key.append(word_for_key)
	if words_for_key==[]:
		t1.insert(END,"Word in list but no Anagram\n")
	else:
		return words_for_key

	
def keyPosition():
	list_pos=[i for i, e in enumerate(list_key) if e == input_key]
	if list_pos==[]:
		t1.insert(END,"No Anagram Found\n")
	else:
		return list_pos

def weightnumber(charhere):
	charweight=int(PrimeNumDict[charhere])
	return charweight

b1=Button(window,text="Find Anagram",command=iteratelemmad)
b1.grid(row=0,column=0)


input_word_here=StringVar()
e1=Entry(window,textvariable=input_word_here)
e1.grid(row=0,column=2)



#DisplayResult
t1=Text(window,height=10,width=50)
t1.grid(row=1,column=2)

window.mainloop()

