from pathlib import Path
from typing import Union

import pandas as pd


def store(df: pd.DataFrame, *, path: Union[str, Path]):
    df.to_csv(path)
