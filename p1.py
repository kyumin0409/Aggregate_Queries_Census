from census_table import CensusTable
from predicate import Predicate
from schema import hh_persons
from sqlalchemy.sql import and_, or_, not_, func, true
from itertools import combinations

if __name__ == '__main__':

    P1 = CensusTable('P1')
    P1.set_root_select('population')

    # display the table
    P1.render(sql=True)
