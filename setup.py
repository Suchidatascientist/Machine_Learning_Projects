from setuptools import find_packages, setup
from typing import List

# declaring Variable for setup functions
PROJECT_NAME="housing_predictor"
VERSION="0.0.1"
AUTHOR="Shloka Rajesh"
DESCRIPTION="This is first FSDS Nov 21 batch Machine Leraning project"
PACKAGES=["housing"]
REQUIRNMENT_FILE_NAME="requirnments.txt"


def get_requirnments_list()->List[str]:
    """
    Description: This function is going to return list of requirement 
    mention in requirements.txt file
    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    """

    with open (REQUIRNMENT_FILE_NAME) as requirnment_file:
        return requirnment_file.readlines().remove("-e .")



setup(
   name=PROJECT_NAME,
   version=VERSION,
   author=AUTHOR,
   description=DESCRIPTION,
   packages=find_packages(),
   install_requires=get_requirnments_list()
)

