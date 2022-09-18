from tkinter.ttk import Style
import nltk
import websearch
from difflib import SequenceMatcher
import pandas as pd


nltk.download('stopwords')
nltk.download('punkt')


stop_words = set(nltk.corpus.stopwords.words('english')) 

#Function for generating tokens
#Returns words from a string passed as input.

def purifyText(string):
    words = nltk.word_tokenize(string)
    return (" ".join([word for word in words if word not in stop_words]))


#Function for matching results over the web based on the text.

def webVerify(string, results_per_sentence):
    sentences = nltk.sent_tokenize(string)
    matching_sites = []
    for url in websearch.searchBing(query=string, num=results_per_sentence):
        matching_sites.append(url)
    for sentence in sentences:
        for url in websearch.searchBing(query = sentence, num = results_per_sentence):
            matching_sites.append(url)
    
    for url in websearch.searchGoogle(query=string, num=results_per_sentence):
        matching_sites.append(url)
    for sentence in sentences:
        for url in websearch.searchGoogle(query = sentence, num = results_per_sentence):
            matching_sites.append(url)

    return (list(set(matching_sites)))

#Similarity function
#The function calculates and compares instances to get a ratio for them.

def similarity(str1, str2):
    return (SequenceMatcher(None,str1,str2).ratio())*100


# Generate report function
# Passed input text or file text as parameters.

def report(text):

    matching_sites = webVerify(purifyText(text), 2)
    matches = {}

    for i in range(len(matching_sites)):
        matches[matching_sites[i]] = similarity(text, websearch.extractText(matching_sites[i]))

    matches = {k: v for k, v in sorted(matches.items(), key=lambda item: item[1], reverse=True)}

    sum=0
    for k, v in matches.items():
        sum += v
    matches["TOTAL SIMILARITY"] = sum
    
    return matches

# Return Table function
# Used for returning data-frame to the final report page.
def returnTable(dictionary):

    df = pd.DataFrame({'Similarity (%)': dictionary})
    #df = df.fillna(' ').T
    #df = df.transpose()
    return df.to_html(classes="table ")


# Driver code
if __name__ == '__main__':
    report('This is a pure test')
