### Filters sentences with misplaced punctuation at the end

To remove sentences from the source and the target file having misplaced punctuation or no trailing punctuation at the end. In some cases, the sentences are simply modified to remove the unwanted punctuation at the end.

```
python punctuation_filter.py --s <source> --t <target>
```

where `source` and `target` are respectively the paths to the files containing sources and corresponding target paraphrases.
