import subprocess
import sys

import pytest

test_key = 'MZXW6YTBOJUWU23MNU'


def test_execution():
    cmd = [sys.executable, '-m', 'oathtool', test_key]
    subprocess.check_call(cmd)


def test_error_execution():
    cmd = [sys.executable, '-m', 'oathtool']
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_call(cmd)


def test_generate_script(tmpdir):
    target = tmpdir / 'oathtool'
    cmd = [sys.executable, '-m', 'oathtool.generate-script', str(target)]
    subprocess.check_call(cmd)
    assert target.isfile()


def test_piped_input():
    cmd = [sys.executable, '-m', 'oathtool']
    subprocess.run(cmd, input=test_key, check=True, text=True, encoding='utf-8')
