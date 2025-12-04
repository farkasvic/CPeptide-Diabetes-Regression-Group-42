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
@click.option('--data-dir', type=str, default='data/raw', help='Directory to store downloaded and processed data')


def main(url, data_dir):
    """
    Download and extract diabetes dataset from remote URL.
    
    Downloads the zip file from the specified URL, saves it to the data directory,
    and extracts the .dat file contained within.
    """
    
    os.makedirs(data_dir, exist_ok=True)
    
  
    response = requests.get(url)

    
    zip_bytes = BytesIO(response.content)
    
    with zipfile.ZipFile(zip_bytes, "r") as zip_ref:
        dat_files = [f for f in zip_ref.namelist() if f.endswith(".dat")]
        dat_content = zip_ref.read(dat_files[0]).decode("utf-8")
        dat_filename = os.path.basename(dat_files[0])
        
        output_path = os.path.join(data_dir, dat_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(dat_content)
        
        print(f"✓ Downloaded and saved: {output_path}")
        print(f"✓ Extracted .dat file: {dat_filename}")
        print(f"✓ Dataset ready for processing")


if __name__ == '__main__':
    main()