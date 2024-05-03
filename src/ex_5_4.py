"""ex_5_4.py"""
import numpy as np
from pathlib import Path

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

# Use these predefined paths.  Note: automated tests expect these paths
# Changing these paths will cause tests to fail.

rootdir = get_repository_root()
datadir = rootdir / "data"
outputdir = rootdir / "outputs"
inputfile = datadir / "ex_5_4-data.csv"
outputfile = outputdir / "ex_5_4-processed.csv"

data_in_file = np.loadtxt(inputfile)

data_in_file[data_in_file<0] = 0

np.savetxt(outputfile, data_in_file, fmt='%.2e')

