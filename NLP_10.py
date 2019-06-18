from nltk.stem import PorterStemmer 
from nltk.tokenize import RegexpTokenizer
import sys

Text=str()
#with open("./a.txt", "r") as f:
with open(sys.argv[1], "r") as f:
    for line in f:
        Text+=line
tokenizer = RegexpTokenizer(r'\w+')
WORDS=tokenizer.tokenize(Text.lower())

ps = PorterStemmer() 
STEMMED_Text=str()
for w in WORDS: 
    STEMMED_Text+=ps.stem(w)+' '
    
text_file = open(sys.argv[2], "w")
text_file.write(STEMMED_Text)
text_file.close()

print("Output present in",sys.argv[2],"Done....")
