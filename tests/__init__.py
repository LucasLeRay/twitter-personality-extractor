from pathlib import Path
import sys

ROOT_DIR = Path(__file__).parents[1].resolve()
SRC_DIR = ROOT_DIR / 'src'

sys.path.append(str(SRC_DIR))