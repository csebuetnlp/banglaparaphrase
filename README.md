### Filtering Scheme
![filter_pipeline](images/filter_sequence.png)

| Filter Name | Significance | Filtering Parameters |
| ----------- | ----------- |----------------------------|
| PINC | Ensure diversity in generated paraphrase | 0.65, 0.76, 0.80|
| BERTScore   | Preserve semantic coherence with the source |lower 0.91 - 0.93, upper 0.98|
|N-gram repetition|Reduce n-gram repetition during inference|2 - 4 grams|
| Punctuation | Prevent generating non-terminating sentences during inference | N/A |

In the respective folders, instructions on how to run certain filtering and scoring scripts are provided.

### Run the full pipeline
Install requirements from [requirements](https://github.com/csebuetnlp/banglaparaphrase/blob/master/requirements.txt) and then run the following command.
```
bash filter.sh -i <input> -p <pinc_threshold> -l <lower_bert_score_threshold> -h <higher_bert_score_threshold>
```
Where `input` is the path to the jsonl file containing sentences and their corresponding paraphrases as key value pairs, `pinc_threshold` is the threshold for PINCScore, `lower_bert_score_threshold` and `higher_bert_score_threshold` are the limits for BERTScore in scale of 0 to 1.

This will generate two files named `source.bn` and `target.bn` in the working directory containing the filtered pairs after passing through all the filtering steps.
