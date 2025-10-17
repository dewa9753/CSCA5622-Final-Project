from settings import DATA_ROOT
import pandas as pd
import sys
import os

form_data_path = lambda filename: f'{DATA_ROOT}/{filename}.csv'

def consolidate_data(paths, column_order):
    try:
        # assemble dataframes
        df_list = []
        for path in paths.values():
            df_list.append(pd.read_csv(path))

        # concat all dfs
        consolidated_df = pd.concat(df_list, ignore_index=False)

        # reorder columns
        consolidated_df = consolidated_df[column_order]

        return consolidated_df
    except Exception as e:
        print(f"Error consolidating data: {e}")
        return None
    
def save_data(df, output_filename, force=False):
    if type(df) == type(None) or df.empty == True:
        print("The final dataframe has no rows. Exiting...")
        return
    try:
        if force or (not force and not os.path.exists(form_data_path(output_filename))):
            df.to_csv(form_data_path(output_filename), index=False)
            print(f"Consolidated data saved to {output_filename}.csv")
    except Exception as e:
        print(f"Error saving consolidated data: {e}")


reference_data_paths = {
    'circuits': form_data_path('circuits_clean'),
    'drivers': form_data_path('drivers_clean'),
    'races': form_data_path('races_clean'),
    'constructors': form_data_path('constructors_clean'),
    'status': form_data_path('status_clean'),
}

training_data_paths = {
    'lap_times': form_data_path('lap_times_clean'),
    'qualifying': form_data_path('qualifying_clean'),
    'results': form_data_path('results_clean'),
    'pit_stops': form_data_path('pit_stops_clean'),
    'constructors_standings': form_data_path('constructor_standings_clean'),
    'drivers_standings': form_data_path('drivers_standings_clean'),
    'constructor_results': form_data_path('constructor_results_clean'),
    'sprint_results': form_data_path('sprint_results_clean'),
}

reference_data_column_order = [
    'raceId', 'year',
    'driverId', 'driverForename', 'driverSurname',
    'constructorId', 'constructorName',
    'circuitId', 'circuitName',
    'statusId', 'statusText'
]

training_data_column_order = [
    'year', 'raceId', 'driverId', 'constructorId', 'lapNumber', 'positionInLap', 'lapTime', 'lapMilliseconds',
    'qualifyingPosition', 'q1', 'q2', 'q3'
]


if __name__ == "__main__":
    should_force = False
    if len(sys.argv) > 1 and '--force-consolidate' in sys.argv:
        should_force = True

    # consolidate reference data
    ref_df = consolidate_data(
        reference_data_paths,
        reference_data_column_order
    )
    if(type(ref_df) != type(None) and ref_df.empty == False):
        save_data(
            ref_df,
            'reference_data',
            should_force
        )
    
    """
    # consolidate useful data
    training_df = consolidate_data(
        training_data_paths,
        training_data_column_order
    )
    if(training_df.empty == False):
        save_data(
            training_df,
            'training_data',
            should_force
        )
    """