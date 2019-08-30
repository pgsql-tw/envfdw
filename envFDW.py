"""
envFDW is a forign data wrapper for processing environment variables.
These operations are only session level.

CREATE SERVER envfdw_srv FOREIGN DATA WRAPPER multicorn OPTIONS ( wrapper 'multicorn.envFDW.FDW' );
CREATE FOREIGN TABLE envfdw ( var text, val text ) SERVER envfdw_srv;

Example:

SELECT * FROM envfdw; -- List all environment variables
INSERT INTO envfdw (var, val) VALUES ('abc', '1'), ('def', '2'); -- Add two new environment variables
UPDATE envfdw SET val='3' WHERE var='abc'; -- Set a new value to specified environment variables
DELETE FROM envfdw WHERE var='def'; -- Unset environment variables

"""
from multicorn import ForeignDataWrapper
import os

class FDW(ForeignDataWrapper):

    def __init__(self, options, columns):
        super(FDW, self).__init__(options, columns)

    def execute(self, quals, columns):
        rows = []
        for var in os.environ:
            row = {}
            row['var'] = var
            row['val'] = os.environ[var]
            rows.append(row)
        return rows
        
    @property
    def rowid_column(self):
        return 'var'
        
    def insert(self, new_values):
        os.environ[new_values['var']] = new_values['val']
        return new_values
     
    def update(self, old_values, new_values):
        os.environ[new_values['var']] = new_values['val']
        return new_values
        
    def delete(self, old_values):
        del os.environ[old_values]
