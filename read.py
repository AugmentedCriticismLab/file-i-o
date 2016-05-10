import re 

#wordslist= the list THAT CONTAINS ALL the words in a sentence 
# datalist= the list that contains all of the senteces 

with open("read_it.txt", "r") as myfile: #input is in txt file called read_it 
    data=myfile.read() 
    print data  # printing contents of text file 
datalist = data.split('.') #breaking text file into sentences
print datalist  # printing text file which is now a list of sentences 

sentenceNum= len(datalist)-1 # getting the length of list (how many santences are in file)
print sentenceNum 

print datalist[2]

i=0 
while i < sentenceNum: # looping through every sentence in the text file 
	wordCount = len(re.findall(r'\w+', datalist[i]))
	wordslist = re.findall(r'\w+', datalist[i])
	print wordCount
	print wordslist
	print wordslist[2]
#	j=0 
#	while j < wordCount: # looping through every sentence in the text file 


	i= i + 1 

 
