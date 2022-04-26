from setuptools import setup, find_packages
from os import path

pkg_name = 'workflow_visual_stimulus'
here = path.abspath(path.dirname(__file__))

long_description = """"
# Pipeline for visual stimulation

Build a full ephys pipeline using the DataJoint elements
+ [element-lab](https://github.com/datajoint/element-lab)
+ [element-animal](https://github.com/datajoint/element-animal)
+ [element-session](https://github.com/datajoint/element-session)
+ [element-event](https://github.com/datajoint/element-event)
+ [element-visual-stimulus](https://github.com/datajoint/element-visual-stimulus)
"""

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

with open(path.join(here, pkg_name, 'version.py')) as f:
    exec(f.read())

setup(
    name='workflow-visual-stimulus',
    version=__version__,
    description="Pipeline for visual stimulation",
    long_description=long_description,
    author='DataJoint',
    author_email='info@datajoint.com',
    license='MIT',
    url='https://github.com/datajoint/workflow-visual-stimulus',
    keywords='neuroscience datajoint stimuli gratings',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=requirements,
)
