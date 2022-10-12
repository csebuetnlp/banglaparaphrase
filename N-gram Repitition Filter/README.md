### Filter sentences with N-gram repeats

To remove sentences from the source and target file having n-gram repeats in the target file. The value of n is set to 2 by default. After removal, both the filtered source and target sentences are obtained.

```
python n_gram_repeatition_filter.py --s <source> --t <target>
```

where `source` and `target` are respectively the paths to the files containing sources and corresponding target paraphrases.
