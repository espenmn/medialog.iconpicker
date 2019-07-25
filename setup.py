from setuptools import setup, find_packages
import os

version = '0.7'

setup(name='medialog.iconpicker',
      version=version,
      description="Iconpicker for Plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Espen Moe-Nilssen',
      author_email='espen@medialog.no',
      url='http://github.com/espenmn/medialog.iconpicker',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['medialog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.behavior',
          'collective.js.bootstrap',
          'medialog.controlpanel',
          'plone.api',
           'collective.z3cform.datagridfield',
           'lineage.registry',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      )
