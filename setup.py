# -*- coding: utf-8 -*-
import os.path
import setuptools


def read(*path_elements):
    """Read a file."""
    with open(os.path.join(*path_elements)) as f:
        return f.read()

version = '2.22'

setuptools.setup(
    name='icemac.ab.locales',
    version=version,
    description=(
        "Translations for icemac.addressbook and icemac.ab.* packages."),
    long_description='\n\n'.join([read('README.rst'), read('CHANGES.rst')]),
    keywords='icemac addressbook address book locales translation i18n',
    author='Michael Howitz',
    author_email='icemac@gmx.net',
    url='https://pypi.org/project/icemac.ab.locales',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: German',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['icemac', 'icemac.ab'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.i18n',
    ],
    extras_require=dict(
        extract=[
            'icemac.ab.calendar',
            'icemac.ab.importer',
            'icemac.ab.importxls',
            'icemac.addressbook >= 9.0.dev0',
        ],
        extractZopeMimetype=[
            'zope.mimetype',
        ],
        compile=[
            'python-gettext'
        ],
    ),
)
