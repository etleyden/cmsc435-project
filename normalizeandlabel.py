import sys
import pandas as pd
#USAGE: CALL FROM COMMAND LINE python normalizeandlabel.py {FEATURECSV} features.csv
def main():
    if len(sys.argv) < 1:
        print("Missing feature.CSV filepath. Exiting...")
        sys.exit()
    fname = sys.argv[1]
    features = sys.argv[2]
    try:
        df = pd.read_csv(fname)
        feats = pd.read_csv(features)

        df = df.div(df.sum(axis=1), axis=0)
        out =  pd.concat([df, feats], axis=1)
        out.to_csv("norm_labeled_features.csv")

    except Exception as e:
        print("Exception " + e + " has occured.")

if __name__ == "__main__":
    main()
