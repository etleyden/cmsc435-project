This is the folder with each file created from generating predictions on the blind set. They were created in this order:

1. `sequences_test_no_labels.txt` is the blind set as given by Dr. Kurgan
2. `cleaned_sequences.txt` removes BJOUZX or whatever the character sequence was
3. `test_*.csv` are the generated features from `pfeature_comp`
4. `normalized_data.csv` combines the separate feature files and normalizes them using min-max normalization.
5. `predictions.csv` is the generated file from AI Studio containing predictions
6. `pred_labels.txt` is the labels themselves. This was created in a live python environment rather than a written script, so the code for that isn't in this repository, or anywhere for that matter. 