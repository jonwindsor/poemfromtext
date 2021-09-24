#Import Statements
!pip install pronouncing
import pronouncing
import random
import re
import requests

##Textblob Import
from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

##File Import
result = requests.get('https://www.gutenberg.org/files/66057/66057-0.txt')
text = result.text
text = text.replace("“","\"").replace("”","\"")
blob = TextBlob(text)

#Preliminary Code by Zach Whalen
five = []
seven = []

for sentence in blob.sentences:
  clean_sentence = re.sub(r'[,\.\"“”\?\!\;\-\&]_', ' ', str(sentence)).replace('’','\'')
  sentence_phonemes = []

  for word in clean_sentence.split():
    word_phonemes = pronouncing.phones_for_word(word)
    if (len(word_phonemes) > 0):
      sentence_phonemes.append(word_phonemes[0])
  syllables = 0

  for p in sentence_phonemes:
    syllables += pronouncing.syllable_count(p)

  if syllables is 5:
    five.append(sentence.upper())

  if syllables is 7:
    seven.append(sentence.upper())

nounList = []
for w,pos in blob.tags:
  if pos == 'NN':
      nounList.append(w.upper())
      
adjList = []
for x,pos in blob.tags:
  if pos == 'JJ':
      adjList.append(x.upper())
 
line0 = ""
line1 = ""
line2 = ""
line3 = ""

line0 = random.choice(nounList)
line1 = random.choice(five)
line2 = random.choice(seven)
line3 = random.choice(five)

print("- " + line0 + " -\n")
print(line1 + "\n")
print(*line2 + "\n")
print(line3 + "\n")