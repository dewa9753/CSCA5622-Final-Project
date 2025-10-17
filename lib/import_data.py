import kagglehub
import os
import sys
import shutil
import settings
from pathlib import Path

if __name__ == "__main__":
    if len(sys.argv) > 1 and '--force-import' in sys.argv:
        if os.path.exists(settings.ORIGINAL_DATA_ROOT):
            shutil.rmtree(settings.ORIGINAL_DATA_ROOT)
            print(f"Force re-downloading: removed '{settings.ORIGINAL_DATA_ROOT}' directory to re-download the data.")

    if not os.path.exists(settings.ORIGINAL_DATA_ROOT):
        # Download latest version
        path = kagglehub.dataset_download(settings.DATA_NAME)

        try:
            shutil.move(path + '\\', './')
            Path('104').rename(settings.ORIGINAL_DATA_ROOT)
            print(f"Successfully downloaded data to '{settings.ORIGINAL_DATA_ROOT}/'!")
        except Exception as e:
            print(f"Error moving downloaded data to '{settings.ORIGINAL_DATA_ROOT}/': {e}")
