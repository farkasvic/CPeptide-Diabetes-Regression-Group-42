import pandas as pd
import os
import click

@click.command()
@click.option(
    '--csv-path',
    type = str,
    default = 'data/processed',
    help='filepath for the processed csv file')