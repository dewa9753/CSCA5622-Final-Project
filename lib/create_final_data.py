from settings import DATA_ROOT
import pandas as pd
import sys
import os

form_data_path = lambda filename: f'{DATA_ROOT}/{filename}.csv'

if __name__ == '__main__':
    if len(sys.argv) > 1 and '--force-final' in sys.argv:
        if os.path.exists(form_data_path('final_data')):
            os.remove(form_data_path('final_data'))
            print(f"Force re-creating: removed '{form_data_path('final_data')}' to re-create the final data.")
    
    if not os.path.exists(form_data_path('final_data')):
        # load cleaned data
        dfs = {}
        for file in os.listdir(DATA_ROOT):
            key = file.replace('_clean.csv', '')
            dfs[key] = pd.read_csv(form_data_path(key + '_clean'))
    
        ## Calculate the final data features
        final_df = dfs['results'].copy()
        final_df.rename(columns={'finalMilliseconds': 'finalTime'}, inplace=True)

        # insert q1,q2,q3 columns from qualifying data
        qualifying_times_df = dfs['qualifying']
        qualifying_times_df.drop(columns=['qualifyingPosition'], inplace=True)
        qualifying_times_df[['q1', 'q2', 'q3']] = qualifying_times_df[['q1', 'q2', 'q3']].applymap(lambda x: '00:' + x)
        qualifying_times_df['q1'] = (pd.to_timedelta(qualifying_times_df['q1']).dt.seconds*1000).astype('int64')
        qualifying_times_df['q2'] = (pd.to_timedelta(qualifying_times_df['q2']).dt.seconds*1000).astype('int64')
        qualifying_times_df['q3'] = (pd.to_timedelta(qualifying_times_df['q3']).dt.seconds*1000).astype('int64')
        final_df = final_df.merge(qualifying_times_df, on=['raceId', 'driverId', 'constructorId'], how='left')

        # insert constructor standing
        constructor_standings_df = dfs['constructor_standings']
        constructor_standings_df.rename(columns={'position': 'constructorPosition'}, inplace=True)
        final_df = final_df.merge(constructor_standings_df[['raceId', 'constructorId', 'constructorPosition']], on=['raceId', 'constructorId'], how='left')

        final_df.drop(columns=['totalLaps', 'raceId', 'points', 'finalTime', 'fastestLap', 'fastestLapTime', 'fastestLapSpeed', 'statusId'], inplace=True)
        final_df.sort_values(by=['driverId'], inplace=True)
        final_df.drop_duplicates(inplace=True)
        final_df.dropna(inplace=True)

        # save final data
        final_df.to_csv(form_data_path('final_data'), index=False)
        print(f"Created final data at '{form_data_path('final_data')}'")

