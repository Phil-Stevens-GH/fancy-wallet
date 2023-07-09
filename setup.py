from setuptools import setup, find_packages
 
setup(
    name='PhilSfancywallet', 
    packages=find_packages(),
#    email='gmartins@fancywhale.ca',
#    author='Gui Martins',
    install_requires=[
        'click',
        'requests'
    ],
    version='0.0.2',
    long_description="""# Markdown supported!\n\n* Cheer\n* Celebrate\n""",
    long_description_content_type='text/markdown',     
    entry_points='''
    [console_scripts]
    PhilSfancywallet=PhilSfancywallet:PhilSfancywallet
    '''
)