import pandas as pd
import numpy as np
import os
import sys
import settings

## functions
def get_original_data(file_name):
    df = pd.read_csv(settings.ORIGINAL_DATA_ROOT + file_name)
    df.replace(to_replace=r'\N', value=np.nan, inplace=True)
    return df

def create_clean_data(df, columns_to_drop, output_file_name):
    df_cleaned = df.drop(columns_to_drop, axis=1)
    df_cleaned = df_cleaned.dropna()
    df_cleaned.to_csv(settings.CLEAN_DATA_ROOT + output_file_name, index=False)
    print(f'Cleaned {output_file_name} and created {settings.CLEAN_DATA_ROOT + output_file_name}')

## clean data if not already cleaned
if __name__ == '__main__':

    # check for --force argument to re-clean data
    if len(sys.argv) > 1:
        if sys.argv[1] == '--force':
            if os.path.exists(settings.CLEAN_DATA_ROOT):
                import shutil
                shutil.rmtree(settings.CLEAN_DATA_ROOT)
                print(f'Force cleaning: removed \'{settings.CLEAN_DATA_ROOT}\' directory to re-clean the data.')

    # create clean root directory if it doesn't exist
    if not os.path.exists(settings.CLEAN_DATA_ROOT):
        os.makedirs(settings.CLEAN_DATA_ROOT)

    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'circuits_clean.csv'):
        df = get_original_data('circuits.csv')
        create_clean_data(
            df,
            ['url', 'circuitRef', 'lat', 'lng', 'alt', 'location', 'country'],
            'circuits_clean.csv'
        )
    
    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'constructor_results_clean.csv'):
        df = get_original_data('constructor_results.csv')
        create_clean_data(    
            df,
            [],
            'constructor_results_clean.csv'
        )
    
    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'constructor_standings_clean.csv'):
        df = get_original_data('constructor_standings.csv')
        create_clean_data(
            df,
            ['positionText'],
            'constructor_standings_clean.csv'
        )
    
    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'constructors_clean.csv'):
        df = get_original_data('constructors.csv')
        create_clean_data(
            df,
            ['url', 'nationality'],
            'constructors_clean.csv'
        )
    
    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'drivers_standings_clean.csv'):
        df = get_original_data('driver_standings.csv')
        create_clean_data(
            df,
            ['positionText'],
            'drivers_standings_clean.csv'
        )

    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'drivers_clean.csv'):
        df = get_original_data('drivers.csv')
        create_clean_data(
            df,
            ['driverRef', 'number', 'code', 'url', 'dob', 'nationality'],
            'drivers_clean.csv'
        )

    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'lap_times_clean.csv'):
        df = get_original_data('lap_times.csv')
        create_clean_data(
            df,
            [],
            'lap_times_clean.csv'
        )
    
    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'pit_stops_clean.csv'):
        df = get_original_data('pit_stops.csv')
        create_clean_data(
            df,
            ['time'],
            'pit_stops_clean.csv'
        )

    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'qualifying_clean.csv'):
        df = get_original_data('qualifying.csv')
        create_clean_data(
            df,
            [],
            'qualifying_clean.csv'
    )
        
    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'races_clean.csv'):
        df = get_original_data('races.csv')
        create_clean_data(
            df,
            ['url', 'time', 'name', 'fp1_date', 'fp1_time', 'fp2_date', 'fp2_time', 'fp3_date', 'fp3_time', 'quali_date', 'quali_time', 'sprint_date', 'sprint_time'],
            'races_clean.csv'
        )

    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'results_clean.csv'):
        df = get_original_data('results.csv')
        create_clean_data(
            df,
            ['number', 'positionText', 'positionOrder'],
            'results_clean.csv'
        )

    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'sprint_results_clean.csv'):
        df = get_original_data('sprint_results.csv')
        create_clean_data(
            df,
            ['number', 'positionText', 'positionOrder'],
            'sprint_results_clean.csv'
        )

    if not os.path.exists(settings.CLEAN_DATA_ROOT + 'status_clean.csv'):
        df = get_original_data('status.csv')
        create_clean_data(
            df,
            [],
            'status_clean.csv'
        )