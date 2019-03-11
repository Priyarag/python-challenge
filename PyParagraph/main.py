#import modules needed
import os
import re
import glob
txtfilepath = os.path.join(os.path.dirname(__file__),"..","PyParagraph")
file_content =[]
# files = glob.glob(txtfilepath)
# for filename in files:
#     print(files)

for file in os.listdir( txtfilepath ):
  if file.endswith( ".txt" ):
      print(file)
      file_read = open(file,"r")
      paragraph = file_read.read()
      words=re.findall(r'\w+', paragraph)
      word_count = (len(words))
      print(f"Approximate Word Count: {word_count}")
      sentence = re.split("(?<=[.!?]) +", paragraph)
      sentence_count = len(sentence)
      print(f"Approximate Sentence Count: {sentence_count}")
      length_chars = re.findall(r'[^\s"]', paragraph)
      appx_letter_count = round(len(length_chars)/len(words),2)
      print(f"Approximate Letter Count: {appx_letter_count}")
      avg_length = round(len(words)/len(sentence),0)
      print(f"Average Sentence Length: {avg_length}")
      