![filter_pipeline](images/filter_sequence.png)

| Filter Name | Significance | Filtering Parameters |
| ----------- | ----------- |----------------------------|
| PINC | Ensure diversity in generated paraphrase | 0.65, 0.76, 0.80|
| BERTScore   | Preserve semantic coherence with the source |lower 0.91 - 0.93, upper 0.98|
|N-gram repetition|Reduce n-gram repetition during inference|2 - 4 grams|
| Punctuation | Prevent generating non-terminating sentences during inference | N/A |

In the respective folders, instructions on how to run certain filtering and scoring scripts are provided.