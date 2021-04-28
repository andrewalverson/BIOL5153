#!/bin/bash

#SBATCH --job-name=conda
#SBATCH --partition comp72
#SBATCH --nodes=1
#SBATCH --tasks-per-node=32
#SBATCH --time=72:00:00
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=student@uark.edu

module load intel/18.0.1 impi/18.0.1 mkl/18.0.1
module load python/3.7.3-anaconda

conda init bash
source activate ~/.conda/envs/transdecoder

cd $SLURM_SUBMIT_DIR
rsync -arl * /scratch/$SLURM_JOB_ID/

cd /scratch/$SLURM_JOB_ID
# job command here

cd $SLURM_SUBMIT_DIR
rsync -arl /scratch/$SLURM_JOB_ID/* .

