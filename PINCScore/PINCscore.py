import jsonlines
import json
import pandas as pd
import torch
from nltk import ngrams
import argparse
import os
import sys
from bengali_stemmer.rafikamal2014 import RafiStemmer


def stem_string(string):
    """
    returns a stemmed string without punctuations

    Args:
        string (str) : string to be stemmed
    Returns:
        stemmed_string (str) : stemmed version of the string
    """
    stemmer = RafiStemmer()
    punc = '''।,;:?!'."-[]{}()–—―~'''

    for ele in string:
        if ele in punc:
            string = string.replace(ele, "")
    words = string.split()
    return ' '.join([stemmer.stem_word(word) for word in words])


def calculateScore():
    N = 4
    datacount=0
    totalPINC=0
    for source in sourcefile:
        prediction=predictionfile.readline()
        datacount+=1
        source=stem_string(source)
        prediction=stem_string(prediction)
        pinc_sum=0
        for i in range(N):
            overlap_count = 0
            key_n_grams = list(ngrams(source.split(), i + 1))
            value_n_gram = list(ngrams(prediction.split(), i + 1))
            value_ngram_size = len(value_n_gram) 
            for key_i in range(len(key_n_grams)):
                for value_i in range(len(value_n_gram)):
                    if key_n_grams[key_i] == value_n_gram[value_i]:
                        overlap_count += 1  # increasing overlap count
                        value_n_gram.pop(value_i)  # removing the exact n gram after calculating overlap
                        break

            # calculating the pinc sum
            if value_ngram_size>0:
                pinc_sum += (1 - (overlap_count / value_ngram_size))
        pinc_sum = pinc_sum / N
        totalPINC+=pinc_sum
    PINCscore=totalPINC/datacount
    print("Average PINC Score : ",PINCscore)
                
        
                    


if __name__ == '__main__':

    # Create the parser
    parser = argparse.ArgumentParser(description='path to jsonL file, output source and output target')

    # Add the arguments
    parser.add_argument('--s',
                        metavar='s',
                        type=str,
                        help='the path to the source file')
    
    parser.add_argument('--p',
                        metavar='p',
                        type=str,
                        help='the path to the prediction file')

    # Execute the parse_args() method
    args = parser.parse_args()

    source_path = args.s
    prediction_path = args.p

    sourcefile = open(source_path,encoding='utf-8')
    predictionfile = open(prediction_path,encoding='utf-8')
    
    calculateScore()

    # closing all the files
    sourcefile.close()
    predictionfile.close()
