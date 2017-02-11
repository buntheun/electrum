from distutils.core import setup
setup(name='elcspendfrom',
      version='1.0',
      description='Command-line utility for electrum "coin control"',
      author='Gavin Andresen',
      author_email='gavin@electrumfoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
