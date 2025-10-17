import subprocess
import sys
import settings

if __name__ == "__main__":
    args = ''
    if len(sys.argv) > 1 and sys.argv[1] == '--force':
        args = ' '.join(sys.argv[1:])
    try:
        result = subprocess.run(['py', 'import_data.py', args], capture_output=True, text=True, check=True)
        print(result.stdout)
        result = subprocess.run(['py', 'clean_data.py', args], capture_output=True, text=True, check=True)
        print(result.stdout)
        print("Data import and cleaning completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running subprocesses: {e.stderr}")