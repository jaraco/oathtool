import path

try:
    from importlib.resources import files  # type: ignore
except ImportError:
    from importlib_resources import files  # type: ignore

import autocommand


@autocommand.autocommand(__name__)
def make_standalone_script(path: path.Path):
    """
    On Unix-like systems, create an 'oathtool' executable
    script that stands alone without this Python library.
    """
    code = (files('oathtool') / '__init__.py').read_text()
    shebang = '#!/usr/bin/env python'
    hook = '__name__ == "__main__" and main()'
    text = '\n'.join((shebang, code, hook))
    path.write_text(text)
    path.chmod('a+x')
