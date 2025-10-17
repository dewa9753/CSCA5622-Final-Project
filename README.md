# CSCA5622-Final-Project

This project is about analyzing a Formula 1 dataset to predict certain outcomes of future races using supervised learning.

Problem statement: Predict the winner of a race without knowing the qualifying results with a test accuracy of above 90%.

Brief description of how the project works:
    - lib/settings.py:
        - global constants module that can be used to configure the entire process from importing data to analyzing the results
    - process_data.py:
        - runs 3 subprocesses: lib/import_data.py, lib/clean_data.py, and lib/consolidate_data.py
        - this combines all the useful data into one .csv file for ease of use during model creation and testing
    - get_results.py:
        - runs 2 subprocesses: lib/train_models.py, lib/test_models.py
        - it will also analyze the predictions from the output of lib/make_predictions.py and print the results out neatly
