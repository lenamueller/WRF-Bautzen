#!/bin/bash

# run interactive job
srun -n 1 -c 1 --time=12:00:00 --mem-per-cpu=1700 /scratch/ws/0/s4300795-bautzen-era5/Download_metdata/entrypoint.sh
