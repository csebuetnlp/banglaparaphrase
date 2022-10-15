### Requirements
To run the scripts, they should be placed inside this project [bengali-stemmer](https://github.com/banglakit/bengali-stemmer).
### Calculate PINCScore

To calculate PINCScore between source and generated paraphrases run the following command from the mentioned project directory.

```
python PINCscore.py --s <source> --p <prediction>
```

where `source` and `prediction` are respectively the paths to the files containing sources and corresponding predictions.

### Filter with PINCScore

To filer with PINCScore run the following command from the mentioned project directory.

```
python filterPINC.py --l <source> --t <target> --p <pinc_score>
```

where `source` is the path to the jsonl file containing sentences and their corresponding paraphrases as key value pairs. `target` is the path to the generated jsonl file containing the pairs after filtering in the same format and `pinc_score` is the PINC score threshold to use to filter the source file.
