from setuptools import setup

setup(name='dftbook',
      version='0.0.2',
      description='Module for setting up dft-book tutorials',
      url='http://github.com/jkitchin/dftbook',
      author='John Kitchin',
      author_email='jkitchin@andrew.cmu.edu',
      license='GPL',
      platforms=[],
      packages=['dftbook'],
      scripts=[],
      include_package_data=True,
      install_requires=[],
      long_description='''A module to setup Quantum Espresso and the computational environment for dft-book tutorials.''',)

# (shell-command "rm -fr build dist dftbook.egg-info")
# (shell-command "python setup.py sdist bdist_wheel")
# (shell-command "twine upload dist/*")
