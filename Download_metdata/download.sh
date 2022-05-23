#!/bin/bash

# run interactive job
srun -n 1 -c 1 --time=12:00:00 --mem-per-cpu=1700 /home/s4300795/wrf/Bautzen/entrypoint.sh
