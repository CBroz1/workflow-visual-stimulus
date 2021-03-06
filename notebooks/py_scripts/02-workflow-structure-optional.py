# -*- coding: utf-8 -*-
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

# This notebook gives a brief overview of the workflow structure and introduce some useful DataJoint tools to facilitate the exploration. DataJoint needs to be pre-configured before running this notebook, if you haven't set up the configuration, refer to notebook [01-configure](01-configure.ipynb).

import os
# change to the upper level folder to detect dj_local_conf.json
if os.path.basename(os.getcwd())=='notebooks': os.chdir('..')
assert os.path.basename(os.getcwd()).startswith('workflow'), ("Please move to the "
                                                              + "workflow directory")

# ## Schemas and tables

# The current workflow is composed of multiple database schemas. The upstream elements (Lab, Animal, and Session) each correspond to a module within `workflow_visual_stimulus.pipeline`

import datajoint as dj
from workflow_visual_stimulus.pipeline import lab, subject, session

# Each module contains a schema object that enables interaction with the schema in the database.

session.schema.list_tables()

# The table classes in the module corresponds to a table in the schema in the database.

# + Each datajoint table class inside the module corresponds to a table inside the schema. For example, the class `ephys.EphysRecording` correponds to the table `_ephys_recording` in the schema `neuro_ephys` in the database.
# preview table columns and contents in a table
session.Session()

# + The first time importing the modules, empty schemas and tables will be created in the database. [markdown]
# # + By importing the modules for the first time, the schemas and tables will be created inside the database.
# # + Once created, importing modules will not create schemas and tables again, but the existing schemas/tables can be accessed and manipulated by the modules.
# -
# ## DataJoint tools to explore schemas and tables

# + The schemas and tables will not be re-created when importing modules if they have existed. [markdown]
# # + `dj.list_schemas()`: list all schemas a user has access to in the current database
# + `dj.list_schemas()`: list all schemas a user could access.
dj.list_schemas()

# + `dj.Diagram()`: plot tables and dependencies. 

# + `dj.Diagram()`: plot tables and dependencies
# plot diagram for all tables in a schema
dj.Diagram(session)
# -

# **Table tiers**: 
#
# Manual table: green box, manually inserted table, expect new entries daily, e.g. Subject, ProbeInsertion.  
# Lookup table: gray box, pre inserted table, commonly used for general facts or parameters. e.g. Strain, ClusteringMethod, ClusteringParamSet.  
# Imported table: blue oval, auto-processing table, the processing depends on the importing of external files. e.g. process of Clustering requires output files from kilosort2.  
# Computed table: red circle, auto-processing table, the processing does not depend on files external to the database, commonly used for     
# Part table: plain text, as an appendix to the master table, all the part entries of a given master entry represent a intact set of the master entry. e.g. Unit of a CuratedClustering.
#
# **Dependencies**:  
#
# One-to-one primary: thick solid line, share the exact same primary key, meaning the child table inherits all the primary key fields from the parent table as its own primary key.     
# One-to-many primary: thin solid line, inherit the primary key from the parent table, but have additional field(s) as part of the primary key as well
# secondary dependency: dashed line, the child table inherits the primary key fields from parent table as its own secondary attribute.

# + `dj.Diagram()`: plot the diagram of the tables and dependencies. It could be used to plot tables in a schema or selected tables.
# plot diagram of tables in multiple schemas
dj.Diagram(subject) + dj.Diagram(session)
# -

# plot diagram with 1 additional level of dependency downstream
dj.Diagram(lab.Lab) + 1

# plot diagram with 2 additional levels of dependency upstream
dj.Diagram(session.Session) - 1

# + `heading`: [markdown]
# # + `describe()`: show table definition with foreign key references.
# -
session.Session.describe();

# + `heading`: show attribute definitions regardless of foreign key references

# + `heading`: show table attributes regardless of foreign key references.
session.Session.heading

# + probe [markdown]
# # Major DataJoint Elements installed in the current workflow
# + ephys [markdown]
# # + [`lab`](https://github.com/datajoint/element-lab): lab management related information, such as Lab, User, Project, Protocol, Source.
# -

dj.Diagram(lab)

# + [`animal`](https://github.com/datajoint/element-animal): general animal information, User, Genetic background, Death etc.

dj.Diagram(subject)

# + [subject](https://github.com/datajoint/element-animal): contains the basic information of subject, including Strain, Line, Subject, Zygosity, and SubjectDeath information.
subject.Subject.describe();

# + [`session`](https://github.com/datajoint/element-session): General information of experimental sessions.

dj.Diagram(session)

# + [session](https://github.com/datajoint/element-session): experimental session information
session.Session.describe();

# + [`ephys`](https://github.com/datajoint/element-array-ephys): Neuropixel based probe and ephys information

# + [probe and ephys](https://github.com/datajoint/element-array-ephys): Neuropixel based probe and ephys tables
dj.Diagram(probe) + dj.Diagram(ephys)
# -

# ## Summary and next step
#
# + This notebook introduced the overall structures of the schemas and tables in the workflow and relevant tools to explore the schema structure and table definitions.
#
# + In the next notebook [03-process](03-process.ipynb), we will further introduce the detailed steps running through the pipeline and table contents accordingly.
