#!/usr/bin/env python
import os
from Cython.Build import cythonize
from distutils.extension import Extension

from distutils.core import setup

HERE = os.path.dirname(__file__)
exec(open(os.path.join(HERE, "construct", "version.py")).read())

#extensions = cythonize([
#    Extension("construct.adapters", ["construct/adapters.pyx"], extra_compile_args=['-pg'], extra_link_args = ['-pg']),
#    Extension("construct.core", ["construct/core.pyx"], extra_compile_args=['-pg'], extra_link_args = ['-pg']),
#    Extension("construct.macros", ["construct/macros.pyx"], extra_compile_args=['-pg'], extra_link_args = ['-pg']),
#    Extension("construct.debug", ["construct/debug.pyx"], extra_compile_args=['-pg'], extra_link_args = ['-pg']),
#    Extension("construct.lib.binary", ["construct/lib/binary.pyx"], extra_compile_args=['-pg'], extra_link_args = ['-pg']),
#    Extension("construct.lib.bitstream", ["construct/lib/bitstream.pyx"], extra_compile_args=['-pg'], extra_link_args = ['-pg']),
#    Extension("construct.lib.container", ["construct/lib/container.pyx"], extra_compile_args=['-pg'], extra_link_args = ['-pg']),
#    Extension("construct.lib.expr", ["construct/lib/expr.pyx"], extra_compile_args=['-pg'], extra_link_args = ['-pg']),
#    Extension("construct.lib.hex", ["construct/lib/hex.pyx"], extra_compile_args=['-pg'], extra_link_args = ['-pg']),
#    Extension("construct.lib.py3compat", ["construct/lib/py3compat.pyx"], extra_compile_args=['-pg'], extra_link_args = ['-pg']),
#], force=True, emit_linenums=True)

extensions = cythonize([
    Extension("construct.adapters", ["construct/adapters.pyx"]),
    Extension("construct.core", ["construct/core.pyx"], extra_compile_args=['-DCYTHON_TRACE=1']),
    Extension("construct.macros", ["construct/macros.pyx"]),
    Extension("construct.debug", ["construct/debug.pyx"]),
    Extension("construct.lib.binary", ["construct/lib/binary.pyx"]),
    Extension("construct.lib.bitstream", ["construct/lib/bitstream.pyx"]),
    Extension("construct.lib.container", ["construct/lib/container.pyx"]),
    Extension("construct.lib.expr", ["construct/lib/expr.pyx"]),
    Extension("construct.lib.hex", ["construct/lib/hex.pyx"]),
    Extension("construct.lib.py3compat", ["construct/lib/py3compat.pyx"]),
], force=True, emit_linenums=True)

setup(
    name="construct",
    ext_modules=extensions,
    version="2.5.2",
    packages=[
        'construct',
        'construct.lib',
        'construct.formats',
        'construct.formats.data',
        'construct.formats.executable',
        'construct.formats.filesystem',
        'construct.formats.graphics',
        'construct.protocols',
        'construct.protocols.application',
        'construct.protocols.layer2',
        'construct.protocols.layer3',
        'construct.protocols.layer4',
    ],
    license="MIT",
    description="A powerful declarative parser/builder for binary data",
    long_description=open(os.path.join(HERE, "README.rst")).read(),
    platforms=["POSIX", "Windows"],
    url="http://construct.readthedocs.org",
    author="Tomer Filiba, Corbin Simpson",
    author_email="tomerfiliba@gmail.com, MostAwesomeDude@gmail.com",
    provides=["construct"],
    build_requires=['cython'],
    install_requires=['cython', 'six', 'cyordereddict'],
    keywords="construct, declarative, data structure, binary, parser, builder, pack, unpack",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
)
