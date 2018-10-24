import os
from setuptools import setup, find_packages  

data_files = ['*', 'templates/*']
directories = ["static"]
while len(directories) != 0:
    directory = directories.pop(0)
    directory_suffix = directory
    directory = os.path.join("TreePlot", directory)
    files = os.listdir(directory)
    for _file in files:
        _file_suffix = os.path.join(directory_suffix, _file)
        _file = os.path.join(directory, _file)
        if os.path.isdir(_file):
            directories.append(_file_suffix)
        else:
            data_files.append(_file_suffix)

setup(  
    name = "TreePlot",  
    version = "1.0",  
    keywords = ["tree", "plot"],  
    description = "Web based tree visualization tool.",  
    long_description = "Web based tree visualization tool.",  
    license = "MIT Licence",  
  
    url = "https://github.com/changzeng/TreePlot",  
    author = "changzeng",  
    author_email = "liaochangzeng@zuoyebang.com",  
  
    packages=['TreePlot'],
    package_dir={'TreePlot':'TreePlot'},
    package_data={'TreePlot':data_files},
    platforms = "any",  
    install_requires = [
        "flask"
    ],  
  
    scripts = [],  
    entry_points = {  
        'console_scripts': [  
            'plot_tree=TreePlot:plot_from_shell'  
        ]  
    }  
)
