import netCDF4 as nc


# print varibales' meta data
fn = 'met_em.d01.2021-09-06_00:00:00.nc'
ds = nc.Dataset(fn)
for var in ds.variables.values():
    print(var)