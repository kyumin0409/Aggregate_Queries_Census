from census_table import CensusTable
from predicate import Predicate
from schema import hh_persons
from sqlalchemy.sql import and_, or_, not_, func, true
from itertools import combinations

if __name__ == '__main__':

    race_attributes = ['RACWHT', 'RACBLK', 'RACAIAN', 'RACASN', 'RACNHPI', 'RACSOR']
    race_alone_predicates = []
    for r in race_attributes:
        pred = Predicate(name=r + '-alone', pred=and_(getattr(hh_persons.c, r) == 1, hh_persons.c.RACNUM == 1))
        race_alone_predicates.append(pred)

    # add 'two-or-more-races'
    race_levels = race_alone_predicates + [Predicate('two-or-more-races', pred=(hh_persons.c.RACNUM >= 2))]


    # create the table object, adding levels
    P3 = CensusTable('P3')
    P3.set_root_select('population')
    P3.add_ortho_level(race_levels)

    # display the table
    P3.render(sql=False)
