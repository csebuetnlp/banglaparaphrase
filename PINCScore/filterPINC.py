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


def filter_dataset():

    N = 4
    PINC_THRESHOLD = 0.76
    linecount = 0

    print(f'Using {PINC_THRESHOLD} threshold')

    for line in f.iter():
        linecount += 1
        hasfound = False
        trgts = {}

        for key, values in line.items():
            original_key = key
            key = stem_string(key)
            stemmed_values = [stem_string(value) for value in values]
            trgts[original_key] = []

            for value_index, value in enumerate(stemmed_values):
                pinc_sum = 0

                for i in range(N):
                    overlap_count = 0
                    key_n_grams = list(ngrams(key.split(), i + 1))
                    value_n_gram = list(ngrams(value.split(), i + 1))
                    value_ngram_size = len(value_n_gram)

                    for key_i in range(len(key_n_grams)):
                        for value_i in range(len(value_n_gram)):
                            if key_n_grams[key_i] == value_n_gram[value_i]:
                                overlap_count += 1  # increasing overlap count
                                # removing the exact n gram after calculating overlap
                                value_n_gram.pop(value_i)
                                break

                    # calculating the pinc sum
                    if value_ngram_size > 0:
                        pinc_sum += (1 - (overlap_count / value_ngram_size))
                pinc_sum = pinc_sum / N

                if pinc_sum >= PINC_THRESHOLD:
                    hasfound = True
                    trgts[original_key].append(values[value_index])
        if hasfound:
            json.dump(trgts, target, ensure_ascii=False)
            target.write("%s" % '\n')
            if linecount % 10000 == 0:
                print(linecount)



if __name__ == '__main__':

    # Create the parser
    parser = argparse.ArgumentParser(
        description='path to the input and output file')

    # Add the arguments
    parser.add_argument('--l',
                        metavar='l',
                        type=str,
                        help='the path to the jsonl file with sources and corresponding predictions')

    parser.add_argument('--t',
                        metavar='t',
                        type=str,
                        help='the path to the generated target jsonl file')

    # Execute the parse_args() method
    args = parser.parse_args()

    jsonl_path = args.l
    target_path = args.t

    target = open(target_path, 'w', encoding='utf-8')
    f = jsonlines.open(jsonl_path)

    filter_dataset()

    # closing all the files
    target.close()
    f.close()
