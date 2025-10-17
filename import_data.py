import kagglehub
import os
import sys
import shutil
from pathlib import Path

if len(sys.argv) > 1 and sys.argv[1] == '--force':
    if os.path.exists('data_original'):
        shutil.rmtree('data_original')
        print("Force re-downloading: removed 'data_original' directory to re-download the data.")

# Download latest version
path = kagglehub.dataset_download("jtrotman/formula-1-race-data")

try:
    shutil.move(path + '\\', './')
    Path('104').rename('data_original')
    print(f"Successfully downloaded data to 'data_original/'!")
except Exception as e:
    print(f"Error moving downloaded data to 'data_original/': {e}")
