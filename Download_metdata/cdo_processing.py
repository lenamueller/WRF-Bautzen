import os

files_ml = []
files_sfc = []

for file in os.listdir("metdata"):
    if file.startswith("ERA5_ML"):
        files_ml.append(file)
    if file.startswith("ERA5_SFC"):
        files_sfc.append(file)
    
# Reduce ML data to variables: z (only sfc), t (levels), q (levels), lnsp (only sfc), u (levels), v (levels)
for fn in files_ml:
    print("file", fn)
    cmd = f"cdo selname,z,t,q,lnsp,u,v metdata/{fn} ERA5/{fn}"
    os.system(cmd)
    
# Recuce SFC data to variables: var165 (u 10m), var166 (v 10m), var167 (T 2m), var151 (MSLP), var34 (sea sfc T), var134 (surface pressure)
for fn in files_sfc:
    print("file", fn)
    cmd = f"cdo selname,var165,var166,var167,var151,var34,var134 metdata/{fn} ERA5/{fn}"
    os.system(cmd)