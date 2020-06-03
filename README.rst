.. image:: https://img.shields.io/pypi/v/oathtool.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/oathtool.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/oathtool

.. image:: https://dev.azure.com/jaraco/oathtool/_apis/build/status/jaraco.oathtool?branchName=master
   :target: https://dev.azure.com/jaraco/oathtool/_build/latest?definitionId=1&branchName=master

.. image:: https://img.shields.io/travis/jaraco/oathtool/master.svg
   :target: https://travis-ci.org/jaraco/oathtool

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. .. image:: https://img.shields.io/appveyor/ci/jaraco/oathtool/master.svg
..    :target: https://ci.appveyor.com/project/jaraco/oathtool/branch/master

.. .. image:: https://readthedocs.org/projects/oathtool/badge/?version=latest
..    :target: https://oathtool.readthedocs.io/en/latest/?badge=latest


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
