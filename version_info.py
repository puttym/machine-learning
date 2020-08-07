import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn

from tabulate import tabulate

def get_version_list():
    """Get version number of the imported libraries and write them
    to a list."""
    version_list = [['Python', sys.version],
                    ['Scipy', scipy.__version__],
                    ['Numpy', numpy.__version__],
                    ['Matplotlib', matplotlib.__version__],
                    ['Pandas', pandas.__version__],
                    ['Scikit-Learn', sklearn.__version__]]
    
    return version_list

def main():
    print(tabulate(get_version_list(), headers = ['Library', 'Version']))

if __name__ == '__main__':
    main() 
