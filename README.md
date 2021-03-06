# DataJoint Workflow - Visual Stimulus

Workflow for visual stimuli, including gratings, launched via 
[Psychtoolbox](http://psychtoolbox.org/).

A complete workflow can be built using the DataJoint Elements.
+ [element-lab](https://github.com/datajoint/element-lab)
+ [element-animal](https://github.com/datajoint/element-animal)
+ [element-session](https://github.com/datajoint/element-session)

This repository provides demonstrations for:
1. Set up a workflow using DataJoint Elements (see
[workflow_visual_stimulus/pipeline.py](workflow_array_ephys/pipeline.py))
2. Displaying gratings.

See the [Element Visual Stimulus description](https://elements.datajoint.org/description/array_ephys/) for the background information and development timeline. For more information on the DataJoint Elements project, please visit https://elements.datajoint.org.  This work is supported by the National Institutes of Health.

## Workflow architecture

<!-- The electrophysiology workflow presented here uses components from 4 DataJoint 
Elements ([element-lab](https://github.com/datajoint/element-lab), 
[element-animal](https://github.com/datajoint/element-animal), 
[element-session](https://github.com/datajoint/element-session),
[element-array-ephys](https://github.com/datajoint/element-array-ephys)) 
assembled together to form a fully functional workflow.

![element-visual-stimulus](images/attached_array_ephys_element.svg) -->

## Installation instructions

The installation instructions can be found at the 
[DataJoint Elements documentation](https://elements.datajoint.org/usage/install/).

## Interacting with the DataJoint workflow

Please refer to the workflow-specific 
[Jupyter notebooks](/notebooks) 
for an in-depth explanation of how to run the workflow.

## Citation

If your work uses DataJoint and DataJoint Elements, please cite the respective Research Resource Identifiers (RRIDs) and manuscripts.

+ DataJoint for Python or MATLAB
    + Yatsenko D, Reimer J, Ecker AS, Walker EY, Sinz F, Berens P, Hoenselaar A, Cotton RJ, Siapas AS, Tolias AS. DataJoint: managing big scientific data using MATLAB or Python. bioRxiv. 2015 Jan 1:031658. doi: https://doi.org/10.1101/031658

    + DataJoint ([RRID:SCR_014543](https://scicrunch.org/resolver/SCR_014543)) - DataJoint for `<Select Python or MATLAB>` (version `<Enter version number>`)

+ DataJoint Elements
    + Yatsenko D, Nguyen T, Shen S, Gunalan K, Turner CA, Guzman R, Sasaki M, Sitonic D, Reimer J, Walker EY, Tolias AS. DataJoint Elements: Data Workflows for Neurophysiology. bioRxiv. 2021 Jan 1. doi: https://doi.org/10.1101/2021.03.30.437358

    + DataJoint Elements ([RRID:SCR_021894](https://scicrunch.org/resolver/SCR_021894)) - Element Array Electrophysiology (version `<Enter version number>`)
