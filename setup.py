from setuptools import setup, find_packages
tests_require = ['interlude', ]

setup(name='samltest',
      version="1",
      description="SAML eval und tests",
      long_description="",
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'pysaml2',
      ],
      tests_require=tests_require,
      test_suite="samltest.tests.test_suite",
      extras_require = dict(
          test=tests_require,
      ),
)
