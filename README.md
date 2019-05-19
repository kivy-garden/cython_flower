kivy-garden demo of cython flower
==================================

[![Coverage Status](https://coveralls.io/repos/github/kivy-garden/cython_flower/badge.svg?branch=master)](https://coveralls.io/github/kivy-garden/cython_flower?branch=master)
[![Build Status](https://travis-ci.com/kivy-garden/cython_flower.svg?branch=master)](https://travis-ci.com/kivy-garden/cython_flower)

A kivy garden flower that shows how to add flowers that requires cython compilation.

Flower information
-------------------

A kivy garden flower demo with cython code.

Install
---------

To install with pip::

    pip install kivy_garden.cython_flower

To build or re-build locally::

    PYTHONPATH=.:$PYTHONPATH python setup.py build_ext --inplace

Or to install as editable (package is installed, but can be edited in its original location)::

    pip install -e .

Usage
-------

```py
do_something
```

TODO
-------

* add your code

Contributing
--------------

Check out our [contribution guide](CONTRIBUTING.md) and feel free to improve the flower.

License
---------

This software is released under the terms of the MIT License.
Please see the [LICENSE.txt](LICENSE.txt) file.

How to release
===============

* update `__version__` in `kivy-garden/cython_flower/__init__.py` to the latest version.
* update `CHANGELOG.md` and commit the changes
* call `git tag -a x.y.z -m "Tagging version x.y.z"`
* for each python version you want to release call `python setup.py bdist_wheel`, which generates the wheels. Call once `python setup.py sdist` to generate the sdist. They are saved in the dist/* directory
* Make sure the dist directory contains the files to be uploaded to pypi and call `twine check dist/*`
* then call `twine upload dist/*` to upload to pypi.
* call `git push origin master --tags` to push the latest changes and the tags to github.
