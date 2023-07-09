from setuptools import setup, find_packages
 
setup(
    name='fancywallet', 
    version='0.0.1',
    packages=find_packages(),
#    email='gmartins@fancywhale.ca',
#    author='Gui Martins',
    install_requires=[
        'click',
        'requests'
    ],
    entry_points='''
    [console_scripts]
    fancywallet=fancywallet:fancywallet
    '''
)