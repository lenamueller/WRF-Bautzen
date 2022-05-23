import cdsapi
import sys


# retrieve arguments
year = sys.argv[1]
month = sys.argv[2].zfill(2)
day = sys.argv[3].zfill(2)
hour = sys.argv[4].zfill(2)

# set filename structure
filename = f'ERA5_ML_{year}_{month}_{day}_{hour}'

# ERA5 catalogue:
# https://apps.ecmwf.int/data-catalogues/era5/?axis_date=2021-09-01&axis_time=00:00:00&axis_levelist=1&axis_param=155,77,248,129,152,203,247,246,133,75,76,130,131,132,135,138&stream=oper&levtype=ml&expver=1&month=sep&year=2021&type=an&class=ea

# download data
c = cdsapi.Client()
c.retrieve(
    'reanalysis-era5-complete', # Requests follow MARS syntax
    {

        "class": "ea",
        'date':f'{year}-{month.zfill(2)}-{day.zfill(2)}',
        "expver": "1",
        "levelist": "1/to/137",
        "levtype": "ml",
        'param': '75/76/77/129/130/131/132/133/135/138/152/155/203/246/247/248',
        "stream": "oper",
        'time': f'{hour.zfill(2)}:00:00',
        "type": "an",
        'grid': "0.25/0.25",
        'area': [62, -5, 35, 35,], # max lat, min lon, min lat, max lon (or "62/-5/35/35")
        'format': "grib"

    },
    f'/scratch/ws/0/s4300795-bautzen-era5/metdata/{filename}.grib')
