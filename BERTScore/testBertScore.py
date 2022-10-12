# Must Be Kept at /bert_score/bert_score folder

from score import score
import numpy as np
from nltk import ngrams
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='path to source and prediction')

# Add the arguments
parser.add_argument('--s',
                    metavar='s',
                    type=str,
                    help='the path to the source')

    
parser.add_argument('--p',
                    metavar='p',
                    type=str,
                    help='the path to the generated prediction file')

args = parser.parse_args()

pred_path = args.p
source_path = args.s

with open(pred_path) as f:
    cands = [line.strip() for line in f]

with open(source_path) as f:
    refs = [line.strip() for line in f]


P, R, F1 = score(cands, refs, lang='bn', verbose=True)


P_mean = P.mean()
R_mean = R.mean()
F1_mean= F1.mean()

print(f"System level precision: {P_mean :.3f}")
print(f"System level recall: {R_mean:.3f}")
print(f"System level F1 score: {F1_mean:.3f}")