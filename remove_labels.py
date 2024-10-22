import sys
import subprocess
import pandas as pd

if len(sys.argv) < 1:
    print("Missing sequences filepath. Exiting...")
    sys.exit()

seq_fpath = sys.argv[1]

def remove_chars(string, chars_to_remove):
    translation_table = str.maketrans("", "", chars_to_remove)
    return string.translate(translation_table)

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

    
    result = subprocess.run([f"python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o features.csv -j AAC"], shell=True)

    if result.returncode == 0:
        features = pd.read_csv("features.csv")
        features["Labels"] = labels
        features.to_csv("features.csv")
    else:
        print("There was an error while using pfeature to compute features")
        sys.exit()

if __name__ == "__main__":
    main()
    sys.exit()
    
        
