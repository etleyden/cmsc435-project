import sys
import os
import subprocess
import pandas as pd

if len(sys.argv) < 1:
    print("Missing sequences filepath. Exiting...")
    sys.exit()

seq_fpath = sys.argv[1]

def remove_chars(string, chars_to_remove):
    translation_table = str.maketrans("", "", chars_to_remove)
    return string.translate(translation_table)

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
def main():
    labels = []
    with open(seq_fpath) as f:
        lines = f.readlines()
        print(f"{len(lines)} lines in the input.")
        count = 0
        NNAA = "BJOUZX"
        with open("proteins.txt", "w+") as p:
            for line in lines:
                line = line.split(",")
                prot = line[0]
                badSeq = False
                for i in prot:
                    if i in NNAA:
                        count += 1
                        badSeq = True
                        break
                if badSeq:
                    prot = remove_chars(prot, NNAA)
                p.write(f"{prot}\n")
                labels.append(line[1].strip())

    
    # list of features and array of commands
    features = ["AAC", "PCP"]
    commands = [f"python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o {feature}_features.csv -j {feature}" for feature in features]

    # run the commands in their own processes
    pids = []
    for command in commands:
        pid = os.fork()
        if pid == 0:
            if not os.path.exists(f"{feature}_features.csv"):
                result = subprocess.run(command, shell=True)
                os._exit(result.returncode)
            else:
                print(f"Features {feature} already computed. Skipping.")
                os._exit(0)
        else:
            pids.append(pid)

    results = []
    # wait for the processes to complete
    for pid in pids:
        results.append(os.waitpid(pid, 0)[1])

    final_df = pd.DataFrame()
    for idx, feature in enumerate(features):
        if results[idx] == 0:
            features = pd.read_csv("{feature}_features.csv")
            features = normalize_columns(features, features.columns.values)
            final_df = pd.concat([final_df, features], axis=1)
        else:
            print(f"Feature set: {feature} threw an error")
        final_df["Labels"] = labels

        final_df.to_csv("features.csv", index=False)
    else:
        print("There was an error while using pfeature to compute features")
        sys.exit()

if __name__ == "__main__":
    main()
    sys.exit()
    
        
