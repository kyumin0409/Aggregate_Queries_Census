from census_table import CensusTable
from predicate import Predicate
from schema import hh_persons
from sqlalchemy.sql import and_, or_, not_, func, true
from itertools import combinations

if __name__ == '__main__':

    # Note to avoid confusion:
    # a construction like this:  hh_persons.c.isHISP == 1
    # creates an sqlalchemy object defining a boolean expression on a defined schema
    # it is an instance of sqlalchemy.sql.expression.BinaryExpression

    hisp = Predicate(name='hisp', pred=hh_persons.c.isHISP == 1)
    not_hisp = Predicate(name='not_hisp', pred=hh_persons.c.isHISP == 0)


    one_race = Predicate(name='one_race', pred=hh_persons.c.RACNUM == 1)
    # define the race enumeration used in the table
    # this generates statements like the following:
    #   Predicate('white-alone', and_(hh_persons.c.RACWHT == 1, hh_persons.c.RACNUM ==1))
    race_attributes = ['RACWHT', 'RACBLK', 'RACAIAN', 'RACASN', 'RACNHPI', 'RACSOR']
    race_alone_predicates = []
    for r in race_attributes:
        pred = Predicate(name=r + '-alone', pred=and_(getattr(hh_persons.c, r) == 1, hh_persons.c.RACNUM == 1),parent=hisp)
        race_alone_predicates.append(pred)

    for r in race_attributes:
        pred = Predicate(name=r + '-alone', pred=and_(getattr(hh_persons.c, r) == 1, hh_persons.c.RACNUM == 1),parent=not_hisp)
        race_alone_predicates.append(pred)

     # add 'two-or-more-races'
    race_levels = race_alone_predicates + [Predicate('two-or-more-races', pred=(hh_persons.c.RACNUM >= 2), parent=hisp)]

    # add 'two-or-more-races'
    race_levels = race_alone_predicates + [Predicate('two-or-more-races', pred=(hh_persons.c.RACNUM >= 2), parent=not_hisp)]


    # create the table object, adding levels
    P5 = CensusTable('P5')
    P5.set_root_select('population')
    P5.add_ortho_level([hisp, not_hisp])
    #P5.add_ortho_level([one_race])

    # display the table
    P5.render(sql=True)
