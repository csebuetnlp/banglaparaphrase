### Setting up for BERTScore for using BanglaBERT encoding
Install requirements.
```
pip install git+https://github.com/csebuetnlp/normalizer
pip install jsonlines
```
Install BERTScore
```
git clone https://github.com/Tiiiger/bert_score
cd bert_score
pip install .
```
To use BanglaBERT encoding, replace the `bert_score/bert_score/score.py` and `bert_score/bert_score/utils.py` files with our corresponding provided files.
### Generate the log file
Place the `logBERT.py` inside the `bert_score/bert_score/` folder. Then generate the log file by running the following command from `bert_score/bert_score/` folder.
```
python logBERT.py --l <source> --t <target>
```
where `source` is the path to the jsonl file containing sentences and their corresponding paraphrases as key value pairs and `target` is the generated log file.
### Calculate BERTScore
To calculate bert score place the `testBertScore.py` inside the `bert_score/bert_score/` folder. Then generate the log file by running the following command from `bert_score/bert_score/` folder.
```
python testBertScore.py --s <source> --p <prediction>
```
where `source` and `prediction` are respectively the paths to the files containing sources and corresponding predictions.

### Filter with BERTScore
To filer with BERTScore using the log file run the following command.
```
python filterBanglaBert.py --j <log_file> --s <source> --t <target> --l <lower_limit> --u <upper_limit>
```
where `log_file` is the path to the log file, `source` and `target` are the path to the generated files containing the sources and their corresponding paraphrases. `lower_limit` and `upper_limit` are the limits for BERTScore in scale of 0 to 1. 
