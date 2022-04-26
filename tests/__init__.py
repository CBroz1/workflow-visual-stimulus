# run all tests:
# pytest -sv --cov-report term-missing --cov=workflow_array_ephys -p no:warnings tests/
# run one test, debug:
# pytest [above options] --pdb tests/tests_name.py -k function_name

import os
import sys
import pathlib
# import pytest
# import datajoint as dj

# from workflow_array_ephys.paths import get_vis_stim_root_data_dir
# from element_interface.utils import find_full_path


# ------------------- SOME CONSTANTS -------------------

_tear_down = False
verbose = False

test_user_data_dir = pathlib.Path('./tests/user_data')
test_user_data_dir.mkdir(exist_ok=True)

sessions_dirs = ['subject1/session1',
                 'subject2/session1',
                 'subject2/session2',
                 'subject3/session1',
                 'subject4/experiment1',
                 'subject5/session1',
                 'subject6/session1']

# --------------------  HELPER CLASS --------------------


class QuietStdOut:
    """If verbose set to false, used to quiet tear_down table.delete prints"""
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout

# ---------------------- FIXTURES ----------------------
