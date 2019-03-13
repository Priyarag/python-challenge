#import dependencies needed
import os
import re

# Make a reference to the txt files folder path
txtfilepath = os.path.join(os.path.dirname(__file__),"..","PyParagraph")
#loop through the files in the folder
for file in os.listdir( txtfilepath ):
  #Check if the file is a txt file and analyse the passage
  if file.endswith( ".txt" ):
      #print the filename
      print(file)
      #open the file
      file_read = open(file,"r")
      #Using read() method read the content of the file and store it to paragraph
      paragraph = file_read.read()
      #using Regular expressions find the words in the paragraph
      # "^": This expression matches the start of a string
      # "w+": This expression matches the alphanumeric character in the string
      words=re.findall(r'\w+', paragraph)
      #finr the word count using len function
      word_count = (len(words))
      #print the total number of words
      print(f"Approximate Word Count: {word_count}")
      #get approximate sentences using reg ex
      sentence = re.split("(?<=[.!?]) +", paragraph)
      #print(sentence)
      #get Approximate sentence count
      sentence_count = len(sentence)
      print(f"Approximate Sentence Count: {sentence_count}")
      #get approximate word count after a space using split
      words_after_a_space = re.findall(r'\s', paragraph)
      #print(words_after_a_space)
      #Get all letters by not looking at spaces
      length_chars = re.findall(r'[^\s]', paragraph)
      #Get appx_letter_count per word
      appx_letter_count = round(len(length_chars)/len(words_after_a_space),1)
      print(f"Approximate Letter Count: {appx_letter_count}")
      #Get Average sentence length (in words)
      avg_length = round(len(words)/len(sentence),0)
      print(f"Average Sentence Length: {avg_length}")
      