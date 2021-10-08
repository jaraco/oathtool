.. image:: https://img.shields.io/pypi/v/oathtool.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/oathtool.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/oathtool

.. image:: https://github.com/jaraco/oathtool/workflows/tests/badge.svg
   :target: https://github.com/jaraco/oathtool/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://readthedocs.org/projects/skeleton/badge/?version=latest
..    :target: https://skeleton.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2021-informational
   :target: https://blog.jaraco.com/skeleton

TOTP code generator based on oathtool.

Usage
=====

Command-line::

    $ python -m oathtool $key

API::

    >>> oathtool.generate_otp(key)

Create standalone script (Unix)::

    $ python -m oathtool.generate-script
    $ ./oathtool $key

Don't want to install oathtool, but just want the script? Use
`pip-run <https://pypi.org/project/pip-run>`_::

    $ pip-run oathtool -- -m oathtool.generate-script
    $ ./oathtool $key


``generate-script`` also takes an arbitrary target path in
case you wish to generate the script elsewhere::

    $ python -m oathtool.generate-script ~/bin/my-oathtool

Or install with `pipx <https://pipxproject.github.io/pipx/>`_::

    $ pipx install oathtool
    $ oathtool $key
