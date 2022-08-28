# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dwg_number/__init__.py
from dwg_number import __version__ as version

setup(
	name="dwg_number",
	version=version,
	description="Drawing number registration app",
	author="y2mulyana",
	author_email="y2mulyana@admin.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
