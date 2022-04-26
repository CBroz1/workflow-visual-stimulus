# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: venv-viz
#     language: python
#     name: venv-viz
# ---

# # DataJoint U24 - Workflow Visual Stimulus

# ## Configure MATLAB engine
#
# Following [these instructions](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html) configure your python environment to have access to your MATLAB engine. In a Mac terminal, for example, one might run the following to install the relevant engine.
#
# ```bash
# # cd "/Applications/MATLAB_R2021b.app/extern/engines/python"
# python setup.py install
# ```
#
# You will also need to [download Psychtoolbox](http://psychtoolbox.org/download).
#
# ## Configure DataJoint
#
# - To run `workflow-visual-stimulaiton`, we need to set up the DataJoint configuration file, called `dj_local_conf.json`, unique to each machine.
#
# - The config only needs to be set up once. If you have gone through the configuration before, directly go to [02-Workflow-Structure](./02-WorkflowStructure_Optional.ipynb).
#
# - By convention, we set the config up in the root directory of workflow package. After you set up DataJoint once, you may be interested in [setting a global config](https://docs.datajoint.org/python/setup/01-Install-and-Connect.html).
#

import os
# change to the upper level folder to detect dj_local_conf.json
if os.path.basename(os.getcwd())=='notebooks': os.chdir('..')
assert os.path.basename(os.getcwd()).startswith('workflow'), ("Please move to the "
                                                              + "workflow directory")

# ### Credentials
#
# Now let's set up the host, user and password in the `dj.config` variable

import datajoint as dj
import getpass
dj.config['database.host'] = '{YOUR_HOST}'
dj.config['database.user'] = '{YOUR_USERNAME}'
dj.config['database.password'] = getpass.getpass() # enter the password securily

# You should be able to connect to the database at this stage.

import datajoint as dj
dj.conn()

# ### Database prefix
#
# Giving a prefix to schema could help on the configuration of privilege settings. For example, if we set prefix `neuro_`, every schema created with the current workflow will start with `neuro_`, e.g. `neuro_lab`, `neuro_subject`, `neuro_session` etc.
#
# The prefix could be configurated as follows in `dj.config`:

dj.config['custom'] = {'database.prefix': 'neuro_'}

# ### Root directories 
#
# + `vis_stim_root_data_dir` field indicates the root directory for `MISSING`

# If there is only one root path.
dj.config['custom']['vis_stim_root_data_dir'] = '/tmp/test_data'
# If there are multiple possible root paths:
dj.config['custom']['vis_stim_root_data_dir'] = ['/tmp/test_data']

dj.config

# In the database, every path is **relative to this root path**. The benefit is that the absolute path could be configured for each machine, and when data transfer happens, we just need to change the root directory in the config file. The workflow supports **multiple root directories**. If there are multiple possible root directories, specify the root as a list.
#
# In the context of the workflow, all the paths saved into the database or saved in the config file need to be in the **POSIX standards** (Unix/Linux), with `/`. The path conversion for machines of any operating system is taken care of inside the elements.

# ## Save the config

# With the proper configurations, we could save this as a file, either as a local json file, or a global file.

dj.config.save_local()

# ls

# Local configuration file is saved as `dj_local_conf.json` in the root directory of this workflow package. Next time if you change your directory to `workflow-visual-stimulus` before importing datajoint and the pipeline packages, the configurations will get properly loaded.
#
# If saved globally, there will be a hidden configuration file saved in your root directory. The configuration will be loaded no matter where the directory is.

# +
# dj.config.save_global()
# -

# ### Linking Module
#
# While DataJoint Elements in python have a way generating a schema-agnostic link to an upstream table, MATLAB is more difficult to parameterize in this manner. Before running the `element-visual-stimulus` schema, you'll need to change the foreign key reference in `stimulus.Sync` and `stimulus.Trial`. For demonstration purposes, we'll link these tables to `session.Session`

# # Next Step

# After the configuration, we will be able to review the workflow structure with [02-workflow-structure-optional](02-workflow-structure-optional.ipynb).


