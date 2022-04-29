import csv
from workflow_visual_stimulus.pipeline import subject, session  # , trial, event


def ingest_general(csvs, tables, skip_duplicates=True, verbose=True,
                   allow_direct_insert=False):
    """
    Inserts data from a series of csvs into their corresponding table:
        e.g., ingest_general(['./lab_data.csv', './proj_data.csv'],
                                 [lab.Lab(),lab.Project()]
    ingest_general(csvs, tables, skip_duplicates=True, verbose=True,
                   allow_direct_insert=False)
        :param csvs: list of relative paths to CSV files.  CSV are delimited by commas.
        :param tables: list of datajoint tables with ()
        :param verbose: print number inserted (i.e., table length change)
        :param skip_duplicates: skip items that are either (a) duplicates within the csv
                                or (b) already exist in the corresponding table
        :param allow_direct_insert: Permit insertion directly into calculated tables
    """
    for csv_filepath, table in zip(csvs, tables):
        with open(csv_filepath, newline='') as f:
            data = list(csv.DictReader(f, delimiter=','))
        if verbose:
            prev_len = len(table)
        table.insert(data, skip_duplicates=skip_duplicates,
                     # Ignore extra fields because some CSVs feed multiple tables
                     ignore_extra_fields=True, allow_direct_insert=allow_direct_insert)
        if verbose:
            insert_len = len(table) - prev_len     # report length change
            print(f'\n---- Inserting {insert_len} entry(s) '
                  + f'into {table.table_name} ----')


def ingest_subjects(subject_csv_path='./user_data/subjects.csv',
                    skip_duplicates=True, verbose=True):
    """
    Ingest subjects listed in the subject column of ./user_data/subjects.csv
    """
    csvs = [subject_csv_path]
    tables = [subject.Subject()]

    ingest_general(csvs, tables, skip_duplicates=skip_duplicates, verbose=verbose)


def ingest_sessions(session_csv_path='./user_data/session/sessions.csv',
                    skip_duplicates=True, verbose=True):
    """
    Inserts data from a sessions csv into corresponding session schema tables
    By default, uses data from workflow_session/user_data/session/
    :param session_csv_path:     relative path of session csv
    :param skip_duplicates=True: datajoint insert function param
    :param verbose: print number inserted (i.e., table length change)
    """
    csvs = [session_csv_path, session_csv_path, session_csv_path, session_csv_path,
            session_csv_path]
    tables = [session.Session(), session.SessionDirectory(),
              session.SessionNote(), session.ProjectSession(),
              session.SessionExperimenter()]

    ingest_general(csvs, tables, skip_duplicates=skip_duplicates, verbose=verbose)


if __name__ == '__main__':
    ingest_subjects()
    ingest_sessions()
