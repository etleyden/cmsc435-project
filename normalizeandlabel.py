import sys
import pandas as pd

#USAGE: CALL FROM COMMAND LINE python normalizeandlabel.py {FEATURECSV} features.csv
def main():
    if len(sys.argv) < 1:
        print("Usage: python normalizeandlabel.py [FEATURE1.CSV, FEATURE2.CSV,] [LABELCSV]. Exiting...")
        sys.exit()

    # fname = sys.argv[1:-1]
    fname = sys.argv[1:]
    # labels = sys.argv[-1:][0]

    # print(f"Features: {fname}\nLabels: {labels}")
    out = pd.DataFrame()
    
    try:
        for feat in fname:
            feats = pd.read_csv(feat)

            # min-max normalization for all features
            feats = normalize_columns(feats, feats.columns.values)

            out =  pd.concat([out, feats], axis=1)

        # append labels
        # labels = pd.read_csv(labels)
        # out = pd.concat([out, labels], axis=1)

        out.to_csv("normalized_data.csv", index=False)

    except Exception as e:
        print("Exception " + e + " has occured.")

def normalize_columns(df, columns):
    # Copy the dataframe to avoid modifying the original one
    df_normalized = df.copy()

    # Apply min-max normalization to each specified column
    for column in columns:
        min_value = df_normalized[column].min()
        max_value = df_normalized[column].max()

        # Avoid division by zero
        if max_value - min_value != 0:
            df_normalized[column] = (df_normalized[column] - min_value) / (max_value - min_value)
        else:
            df_normalized[column] = 0  # If all values are the same, normalize to 0

    return df_normalized
    
if __name__ == "__main__":
    main()
