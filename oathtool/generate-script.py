import argparse

try:
    from importlib.resources import files  # type: ignore
except ImportError:  # pragma: nocover
    from importlib_resources import files  # type: ignore

import path
import autocommand


parser = argparse.ArgumentParser()
parser.add_argument('target', nargs='?', type=path.Path, default=path.Path('oathtool'))


@autocommand.autocommand(__name__, parser=parser)
def make_standalone_script(target):
    """
    On Unix-like systems, create an 'oathtool' executable
    script that stands alone without this Python library.
    """
    code = (files('oathtool') / '__init__.py').read_text()
    shebang = '#!/usr/bin/env python'
    hook = '__name__ == "__main__" and main()'
    text = '\n'.join((shebang, code, hook))
    resolved = target.expanduser()
    resolved.write_text(text)
    resolved.chmod('a+x')
