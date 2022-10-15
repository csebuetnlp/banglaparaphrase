#!/bin/bash
while getopts i:p:l:h: flag
do
    case "$flag" in
        i) input=${OPTARG};;
        p) pinc_threshold=${OPTARG};;
        l) bert_low=${OPTARG};;
        h) bert_high=${OPTARG};;
    esac
done
git clone https://github.com/banglakit/bengali-stemmer.git
cp PINCScore/filterPINC.py bengali-stemmer/
python bengali-stemmer/filterPINC.py --l $input --t "PINC-filtered.jsonl" --p $pinc_threshold
rm -r bengali-stemmer
pip install git+https://github.com/csebuetnlp/normalizer
git clone https://github.com/Tiiiger/bert_score
cd bert_score
pip install .
rm bert_score/score.py bert_score/utils.py
cp "../BERTScore/utils/score.py" bert_score/
cp "../BERTScore/utils/utils.py" bert_score/
cp "../BERTScore/logBERT.py" bert_score/
python "bert_score/logBERT.py" --l "../PINC-filtered.jsonl" --t "BERTlog.jsonl"
rm "../PINC-filtered.jsonl"
python "../BERTScore/filterBanglaBert.py" --j "BERTlog.jsonl" --s "../source.bn" --t "../target.bn" --l $bert_low --u $bert_high
rm "BERTlog.jsonl"
cd ..
rm -r bert_score
