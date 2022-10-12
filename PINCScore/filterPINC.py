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


def filter_dataset(jsonl_file, target_file, pinc_threshold):
    """
    filters the jsonl file with the given pinc threshold and writes the parallel
    sentences to the target file

    Args:
        jsonl_file (file object) : file to be read and filtered
        target_file (file object) : file to be written to
        pinc_threshold (float): pinc threshold value
    Returns:
        None
    """

    N = 4
    linecount = 0

    for line in jsonl_file.iter():
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

                if pinc_sum >= pinc_threshold:
                    hasfound = True
                    trgts[original_key].append(values[value_index])
        if hasfound:
            json.dump(trgts, target_file, ensure_ascii=False)
            target_file.write("%s" % '\n')
            if linecount % 10000 == 0:
                print(linecount)


if __name__ == '__main__':

    # Create the parser
    parser = argparse.ArgumentParser(
        description='path to the input and output file and the pinc score threshold')

    # Add the arguments
    parser.add_argument('--l',
                        metavar='l',
                        type=str,
                        help='the path to the jsonl file with sources and corresponding paraphrases')

    parser.add_argument('--t',
                        metavar='t',
                        type=str,
                        help='the path to the generated target jsonl file')

    parser.add_argument('--p',
                        metavar='p',
                        type=float,
                        help='the desired pinc score threshold (0 - 1)')

    # Execute the parse_args() method
    args = parser.parse_args()

    jsonl_path = args.l
    target_path = args.t
    pinc_threshold = args.p

    target_file = open(target_path, 'w', encoding='utf-8')
    jsonl_file = jsonlines.open(jsonl_path)

    filter_dataset(jsonl_file, target_file, pinc_threshold)

    # closing all the files
    target_file.close()
    jsonl_file.close()
