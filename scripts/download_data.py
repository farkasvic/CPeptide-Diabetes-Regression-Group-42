"""
Script to download and extract diabetes dataset from a remote URL.
"""

import click
import os
import requests
import zipfile
from io import BytesIO

@click.command()
@click.option('--url', type=str, default='https://sci2s.ugr.es/keel/dataset/data/regression/diabetes.zip',
              help='URL to download the dataset from'
)
@click.option('--data-dir', type=str, default='data/processed', help='Directory to store downloaded and processed data')
@click.option('--output-file', type=str, default='clean_diabetes.zip', help='Filename for the downloaded zip file')


def main(url, data_dir, output_file):
    """
    Download and extract diabetes dataset from remote URL.
    
    Downloads the zip file from the specified URL, saves it to the data directory,
    and extracts the .dat file contained within.
    """
    
    os.makedirs(data_dir, exist_ok=True)
    

    file_path = os.path.join(data_dir, output_file)
  
    print(f"Downloading data from {url}...")
    response = requests.get(url)
    

    print(f"Saving zip file to {file_path}...")
    with open(file_path, "wb") as f:
        f.write(response.content)
    

    print("Extracting .dat file from zip archive...")
    zip_bytes = BytesIO(response.content)
    
    with zipfile.ZipFile(zip_bytes, "r") as zip_ref:

        dat_files = [f for f in zip_ref.namelist() if f.endswith(".dat")]
        
        
        dat_content = zip_ref.read(dat_files[0]).decode("utf-8")
        
        output_dat_path = os.path.join(data_dir, dat_files[0])
        with open(output_dat_path, 'w', encoding='utf-8') as f:
            f.write(dat_content)
        
        print(f"✓ Downloaded and saved: {file_path}")
        print(f"✓ Extracted .dat file: {output_dat_path}")
        print(f"✓ Dataset ready for processing")


if __name__ == '__main__':
    main()