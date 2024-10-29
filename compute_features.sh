#!/bin/bash

## Begin SLURM Batch Commands
#SBATCH --cpus-per-task=31
#SBATCH --partition=cpu
#SBATCH --mem=59G
#SBATCH --mail-user leydene@vcu.edu
#SBATCH --mail-type=ALL
#SBATCH --output compute_features.log

module load anaconda3
conda activate testenv
python remove_labels.py sequences_training.txt

## ** END Of SLURM Batch Commands **
## END
