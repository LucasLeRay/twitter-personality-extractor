from io import StringIO
import os
from pathlib import Path
from typing import Union

import boto3
import pandas as pd

from src.directories import directories

LOCAL_STORAGE = "local"
S3_STORAGE = "s3"


def _store_local(data: pd.DataFrame, *, path: Union[str, Path]):
    data.to_csv(path)


def _store_s3(data: pd.DataFrame, *, path: Union[str, Path]):
    bucket = os.getenv("AWS_S3_BUCKET")

    csv_buffer = StringIO()
    data.to_csv(csv_buffer)
    key = str(path).replace(f"{directories.output}/", "")

    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket, key).put(Body=csv_buffer.getvalue())


def store(
    data: pd.DataFrame,
    *,
    path: Union[str, Path],
    mode: str = LOCAL_STORAGE
):
    store_mapper = {
        LOCAL_STORAGE: _store_local,
        S3_STORAGE: _store_s3
    }
    store_func = store_mapper[mode]
    store_func(data, path=path)
