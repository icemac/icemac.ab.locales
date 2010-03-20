# -*- coding: utf-8 -*-
# Copyright (c) 2009-2010 Michael Howitz
# See also LICENSE.txt

import os.path
import setuptools

def read(*path_elements):
    return "\n\n" + file(os.path.join(*path_elements)).read()

version = '0.4'

setuptools.setup(
    name='icemac.ab.locales',
    version=version,
    description=(
        "Translations for icemac.addressbook and icemac.ab.* packages."),
    long_description=(
        read('README.txt') +
        read('CHANGES.txt')
        ),
    keywords='icemac addressbook address book locales translation i18n',
    author='Michael Howitz',
    author_email='icemac@gmx.net',
    url='http://pypi.python.org/pypi/icemac.ab.locales',
    license='ZPL 2.1',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Zope3',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: German',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
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
            'icemac.addressbook',
            'icemac.ab.importer',
            'icemac.ab.importxls',
            ],
        extractZopeMimetype = [
            'zope.mimetype',
            ],
        ),
    )
