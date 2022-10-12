###Calculate PINCScore
To calculate PINCScore between source and generated paraphrases run the following command from this directory.
```
python PINCscore.py --s <source> --p <prediction>
```
where `source` and `prediction` are respectively the paths to the files containing sources and corresponding predictions.

###Filter with PINCScore
To filer with PINCScore run the following command from this directory.
```
python filterPINC.py --l <source> --t <target>
```
where `source` is the path to the jsonl file containing sentences and their corresponding paraphrases as key value pairs. `target` is the path to the generated jsonl file containing the pairs after filtering in the same format.