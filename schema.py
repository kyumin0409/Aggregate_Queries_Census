from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func

'''
Schema definitions for sqlalchemy

sqlalchemy needs to be able to resolve valid attributes and their types. 
'''

metadata = MetaData()

hh_persons = Table('hh_persons', metadata,
    Column('p_id', Integer, primary_key=True),
    Column('hh_id', Integer),
    Column('AGEP', Integer),
    Column('RELP', Integer),
    Column('SEX', Integer),
    Column('RACAIAN', Integer),
    Column('RACASN', Integer),
    Column('RACBLK', Integer),
    Column('RACNHPI', Integer),
    Column('RACSOR', Integer),
    Column('RACWHT', Integer),
    Column('isHISP', Integer),
    Column('RACNUM', Integer),  # number of race groups. This doesn't exist in data right now
                                # need to add as computed column in view definition
    )


'''
Domains and data representations
'''

SEX =  {
    'Male' : 1,
    'Female' : 2
}


