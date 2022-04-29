import datajoint as dj
import matlab.engine as eng

from element_animal import subject
from element_lab import lab
from element_session import session_with_datetime as session
from element_event import trial, event

from element_animal.subject import Subject
from element_lab.lab import Source, Lab, Protocol, User, Project
from element_session.session_with_datetime import Session

from .paths import get_vis_stim_root_data_dir, get_session_directory

if 'custom' not in dj.config:
    dj.config['custom'] = {}

db_prefix = dj.config['custom'].get('database.prefix', '')

__all__ = ['subject', 'lab', 'session', 'trial', 'event',
           'Subject', 'Source', 'Lab', 'Protocol', 'User', 'Project', 'Session',
           'get_vis_stim_root_data_dir', 'get_session_directory']

# Activate "lab", "subject", "session" schema ---------------------------------

lab.activate(db_prefix + 'lab')

subject.activate(db_prefix + 'subject', linking_module=__name__)

Experimenter = lab.User
session.activate(db_prefix + 'session', linking_module=__name__)

# Activate "event" and "trial" schema ---------------------------------

trial.activate(db_prefix + 'trial', db_prefix + 'event', linking_module=__name__)

# MATLAB startup
# mat = eng.start_matlab()
# element_path = dj.config['custom'].get('vis_stim_dir', '') # Path to element-visual-stim
# s = mat.genpath(element_path)
# mat.addpath(s, nargout=0)
# # try:
# dj.conn().query(f"CREATE SCHEMA IF NOT EXISTS `{db_prefix}stimulus`")
# # except DataJointError:
# #     pass # ProgrammingError 1007, "Can't create database 'X_stimulus'; database exists"
# stimulus = dj.schema(db_prefix + 'stimulus')
# mat.stimulus.getSchema(nargout=0)
# mat.stimulus.createTables(nargout=0)
# mat.stimulus.Clip()
# mat.stimulus.Condition()
# mat.stimulus.Grate()
# mat.stimulus.Movie()
# mat.stimulus.MovieClass()
# mat.stimulus.SingleDot()
# mat.stimulus.Trial()

# Pipeline Stimulus referenced by +stimulus/getSchema.m

# schema = dj.schema(db_prefix + 'pipeline')

# @schema
# class Stimulus(dj.Manual):
#     definition = """
#     -> Session
#     stim_id : int
#     """

def list_prefix_schemas():
    return [x for x in dj.list_schemas() if x.startswith(db_prefix)]

def list_stim_tables():
    return dj.Schema(f"{db_prefix}stimulus").list_tables()
