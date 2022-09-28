from config import sqlLiteConnection
import pandas as pd
import re
from tqdm import tqdm

def PFAnalysis():

    #SQLite Querying
    messages = pd.read_sql_query("select text FROM message WHERE is_from_me = 1", sqlLiteConnection)
    texts = messages['text']

    # Read in swear words
    with open('google_swear_words.txt') as f:
        swear_word_list = f.read().split(',')
    for i in range(len(swear_word_list)):
        swear_word_list[i] = swear_word_list[i].strip()

    # Swear Word Analysis
    swear_word_counter = 0
    word_counter = 0
    text_counter = 0
    swear_text_counter = 0
    for text in tqdm(texts):
        text_counter += 1
        newText = True
        if isinstance(text,str):
            for word in text.split(' '):
                word_counter += 1
                for swear in swear_word_list:
                    if(swear.lower() == word.lower()):
                        swear_word_counter += 1
                        if(newText == True):
                            swear_text_counter += 1
                            newText = False
    #TODO: Handle Multi-Word Swear Words

    # Print Results to console
    print("Profanity Usage Analysis Results")
    print('Swear/Total Words: '+str(swear_word_counter)+'/'+str(word_counter))
    print('Swear/Total Texts: ' + str(swear_text_counter)+'/'+str(text_counter))
    print('% of Words that are Swear Words: '+str(swear_word_counter / word_counter*100))
    print('% of Texts that are Swear Texts: ' + str(swear_text_counter / text_counter*100))
