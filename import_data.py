import kagglehub
import os
import sys
import shutil
import settings
from pathlib import Path

if len(sys.argv) > 1 and sys.argv[1] == '--force':
    if os.path.exists('data_original'):
        shutil.rmtree('data_original')
        print(f"Force re-downloading: removed '{settings.ORIGINAL_DATA_ROOT}' directory to re-download the data.")

# Download latest version
path = kagglehub.dataset_download("jtrotman/formula-1-race-data")

try:
    shutil.move(path + '\\', './')
    Path('104').rename(settings.ORIGINAL_DATA_ROOT)
    print(f"Successfully downloaded data to '{settings.ORIGINAL_DATA_ROOT}'!")
except Exception as e:
    print(f"Error moving downloaded data to '{settings.ORIGINAL_DATA_ROOT}': {e}")
