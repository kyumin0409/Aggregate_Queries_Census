from census_table import CensusTable
from predicate import Predicate
from schema import hh_persons
from sqlalchemy.sql import and_, or_, not_, func, true
from itertools import combinations

if __name__ == '__main__':

    # define the predicates for hispanic, not-hispanic
    hisp = Predicate(name='hisp', pred=hh_persons.c.isHISP == 1)
    not_hisp = Predicate(name='not_hisp', pred=hh_persons.c.isHISP == 0)

    P4 = CensusTable('P4')
    P4.set_root_select('population')
    P4.add_ortho_level([hisp, not_hisp])

    # display the table
    P4.render(sql=False)
