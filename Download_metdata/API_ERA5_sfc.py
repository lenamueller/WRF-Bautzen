import cdsapi
import sys


# retrieve arguments
year = sys.argv[1]
month = sys.argv[2].zfill(2)
day = sys.argv[3].zfill(2)
hour = sys.argv[4].zfill(2)

# set filename structure
filename = f'ERA5_SFC_{year}_{month}_{day}_{hour}'

# download data
c = cdsapi.Client()
c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'format': 'grib',
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
            '2m_temperature', 'lake_bottom_temperature', 'lake_cover',
            'lake_depth', 'lake_ice_depth', 'lake_ice_temperature',
            'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor',
            'lake_total_layer_temperature', 'mean_sea_level_pressure', 'mean_wave_direction',
            'mean_wave_period', 'sea_surface_temperature', 'significant_height_of_combined_wind_waves_and_swell',
            'surface_pressure', 'total_precipitation',
        ],
        'year': f'{year}',
        'month': f'{month.zfill(2)}',
        'day': f'{day.zfill(2)}',
        'time': f'{hour.zfill(2)}:00',
        'area': [62, -5, 35, 35,], # max lat, min lon, min lat, max lon
    },

    f'/scratch/ws/0/s4300795-bautzen-era5/metdata/{filename}.grib')
