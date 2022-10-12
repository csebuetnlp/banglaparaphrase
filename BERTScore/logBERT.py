from score import score
import torch
from nltk import ngrams
import argparse
import matplotlib.pyplot as plt
import numpy as np
import jsonlines
import json


def generate_bertscore_logs(jsonl_file, target_file):
    """
    generates the logs by processing jsonl input file and writes the parallel sentences with bertscore to target file

    Args:
        jsonl_file (file object) : file to be read
        target_file (file object) : file to be written the logs to
    Returns:
        None
    """

    tracks = []
    linecount = 0
    refs = []
    cands = []
    originalrefs = []
    originalcands = []
    lines = 0
    for line in jsonl_file.iter():
        lines += 1
        tracks.append(0)
        for key, values in line.items():
            tracks[linecount] += len(values)
            originalkey = key
            key = key.strip()
            for value in enumerate(values):
                originalrefs.append(originalkey)
                originalcands.append(value[-1])
                refs.append(key)
                cands.append(value[-1].strip())
        linecount += 1
        if linecount == 4000:
            _, _, F1 = score(cands, refs, lang='bn', verbose=False)
            F1_list = F1.tolist()
            bertindex = 0
            for track in tracks:
                objtowrite = {}
                objtowrite[originalrefs[bertindex]] = []
                for i in range(track):
                    objtowrite[originalrefs[bertindex]].append(
                        (originalcands[bertindex], F1_list[bertindex]))
                    bertindex += 1
                json.dump(objtowrite, target_file, ensure_ascii=False)
                target_file.write("%s" % '\n')
            tracks = []
            refs = []
            cands = []
            originalrefs = []
            originalcands = []
            linecount = 0
            print(lines)

    _, _, F1 = score(cands, refs, lang='bn', verbose=False)
    F1_list = F1.tolist()
    bertindex = 0
    for track in tracks:
        objtowrite = {}
        objtowrite[originalrefs[bertindex]] = []
        for i in range(track):
            objtowrite[originalrefs[bertindex]].append(
                (originalcands[bertindex], F1_list[bertindex]))
            bertindex += 1
        json.dump(objtowrite, target_file, ensure_ascii=False)
        target_file.write("%s" % '\n')
    tracks = []
    refs = []
    cands = []
    originalrefs = []
    originalcands = []
    linecount = 0
    print(lines)


if __name__ == '__main__':

    # Create the parser
    parser = argparse.ArgumentParser(
        description='path to jsonl input file and generated log file')

    # Add the arguments
    parser.add_argument('--l',
                        metavar='l',
                        type=str,
                        help='the path to the jsonl file with sources and corresponding paraphrases')

    parser.add_argument('--t',
                        metavar='t',
                        type=str,
                        help='the path to the generated log file')

    # Execute the parse_args() method
    args = parser.parse_args()

    jsonl_path = args.l
    target_path = args.t

    jsonl_file = jsonlines.open(jsonl_path)
    target_file = open(target_path, 'w', encoding='utf-8')

    generate_bertscore_logs(jsonl_file, target_file)

    # closing all the files
    jsonl_file.close()
    target_file.close()
