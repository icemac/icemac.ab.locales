# -*- coding: utf-8 -*-
# Copyright (c) 2009-2012 Michael Howitz
# See also LICENSE.txt

import os.path
import setuptools

def read(*path_elements):
    return file(os.path.join(*path_elements)).read()

version = '2.1'

setuptools.setup(
    name='icemac.ab.locales',
    version=version,
    description=(
        "Translations for icemac.addressbook and icemac.ab.* packages."),
    long_description='\n\n'.join([read('README.rst'), read('CHANGES.rst')]),
    keywords='icemac addressbook address book locales translation i18n',
    author='Michael Howitz',
    author_email='icemac@gmx.net',
    url='http://pypi.python.org/pypi/icemac.ab.locales',
    license='ZPL 2.1',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope3',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Natural Language :: German',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
        ],
    packages=setuptools.find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['icemac', 'icemac.ab'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.i18n',
        ],
    extras_require = dict(
        extract = [
            'icemac.ab.calendar',
            'icemac.ab.importer',
            'icemac.ab.importxls',
            'icemac.addressbook',
            ],
        extractZopeMimetype = [
            'zope.mimetype',
            ],
        compile=[
            'python-gettext'
            ],
        ),
    )
