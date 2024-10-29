#!/bin/bash

## Begin SLURM Batch Commands
#SBATCH --cpus-per-task=15
#SBATCH --partition=cpu
#SBATCH --mem=59G
#SBATCH --mail-user leydene@vcu.edu
#SBATCH --mail-type=ALL
#SBATCH --output compute_features.log

module load anaconda3
conda activate testenv
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o TPC_features.csv -j TPC
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o BTC_features.csv -j BTC
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o AAI_features.csv -j AAI
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o RRI_features.csv -j RRI
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o PRI_features.csv -j PRI
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o DDR_features.csv -j DDR
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o SEP_features.csv -j SEP
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o SPC_features.csv -j SPC
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o SER_features.csv -j SER
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o ACR_features.csv -j ACR
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o CTC_features.csv -j CTC
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o CeTD_features.csv -j CeTD
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o PAAC_features.csv -j PAAC
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o APAAC_features.csv -j APAAC
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o QSO_features.csv -j QSO
python pfeature_comp/src/pfeature_comp.py -i proteins.txt -o SOC_features.csv -j SOC

## ** END Of SLURM Batch Commands **
## END
