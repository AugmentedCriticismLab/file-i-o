import re 

#wordslist= the list THAT CONTAINS ALL the words in a sentence 
# datalist= the list that contains all of the senteces 

with open("read_it.txt", "r") as myfile: #input is in txt file called read_it 
    text=myfile.read() 
    print text  # printing contents of text file 
datalist = text.split('.') #breaking text file into sentences
#print datalist  # printing text file which is now a list of sentences 

sentenceNum= len(datalist)-1 # getting the length of list (how many santences are in file)
#print sentenceNum 

#print datalist[2]

i=0 
while i < sentenceNum: # looping through every sentence in the text file 
	wordCount = len(re.findall(r'\w+', datalist[i])) 
	wordslist = re.findall(r'\w+', datalist[i])
	#print wordCount
	#print wordslist
	j=0 
	while j <= wordCount-1: # looping through every sentence in the text file 
		data=wordslist[j]
		if j== wordCount-1:
			nextword= j-1 
		else:
			nextword= j+1
		if data ==wordslist[nextword]:
			print (wordslist[j], "is a repeated word")

		if data !=wordslist[nextword]: #it might not be a repeated word but it might be alitertion (check for alliteration)

			letter=list(wordslist[j]) # getting all of the letters

			if j== wordCount-1 or j== wordCount-2 :
				nextLetter="z"
				thirdLetter="x"
			else:
				nextLetter=(wordslist[j+1]) 
				thirdLetter=(wordslist[j+2])

			if letter[0] ==nextLetter[0] and nextLetter[0] == thirdLetter[0]:
				print("the program detects alliteration in the letter",letter[0])



		j= j+1

	i= i + 1 

    #letterlist = []
	#while k < wordCount: # looping through every sentence in the text file 
    #    letterlist.append(k)
   # letterlist = np.array(letterlist)




 
