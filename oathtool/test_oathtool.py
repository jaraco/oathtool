import sys
import subprocess

import pytest


def test_execution():
    cmd = [sys.executable, '-m', 'oathtool', 'MZXW6YTBOJUWU23MNU']
    subprocess.check_call(cmd)


def test_error_execution():
    cmd = [sys.executable, '-m', 'oathtool']
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_call(cmd)
