#!/bin/bash

# exit on first error
set -e

# run virtual environment
source /scratch/ws/0/s4300795-bautzen-era5/myenv/bin/activate

# load taurus modules
module --force purge
module load modenv/scs5
module load Python/3.8.6

#!/bin/sh
# download ERA5 surface data
#for i in {0..23}; do python API_ERA5_sfc.py 2021 9 6 $i; done
#for i in {0..23}; do python API_ERA5_sfc.py 2021 9 7 $i; done
#for i in {0..23}; do python API_ERA5_sfc.py 2021 9 8 $i; done
#for i in {0..23}; do python API_ERA5_sfc.py 2021 9 9 $i; done
#for i in {0..23}; do python API_ERA5_sfc.py 2021 9 10 $i; done

# download ERA5 upper air data
for i in {16..23}; do python API_ERA5_ml.py 2021 9 6 $i; done
for i in {0..23}; do python API_ERA5_ml.py 2021 9 7 $i; done
for i in {0..23}; do python API_ERA5_ml.py 2021 9 8 $i; done
for i in {0..23}; do python API_ERA5_ml.py 2021 9 9 $i; done
for i in {0..23}; do python API_ERA5_ml.py 2021 9 10 $i; done

# deactivate virtual environment
deactivate
