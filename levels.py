from workload.predicate import Predicate
from workload.schema import hh_persons
from sqlalchemy.sql import and_, or_, not_, func, true
import itertools as it

'''
This file contains common predicates used to define SF1 tables.
The are often re-used across tables.


'''


# define the predicates for hispanic, not-hispanic
hisp = Predicate(name='hisp', pred=hh_persons.c.isHISP == 1)
not_hisp = Predicate(name='not_hisp', pred=hh_persons.c.isHISP == 0)


# define race enumeration
race_attributes = ['RACWHT', 'RACBLK', 'RACAIAN', 'RACASN', 'RACNHPI', 'RACSOR']
race_alone_predicates = []
for r in race_attributes:
    pred = Predicate(name=r + '-alone', pred=and_(getattr(hh_persons.c, r) == 1, hh_persons.c.RACNUM == 1))
    race_alone_predicates.append(pred)

# add 'two-or-more-races'
races_two_plus = [Predicate('two-or-more-races', pred=(hh_persons.c.RACNUM >= 2))]
race_levels = race_alone_predicates + races_two_plus

races_exactly_i = [ Predicate('%i-races'%i, pred=(hh_persons.c.RACNUM == i)) for i in [1,2,3,4,5,6]]



def race_pred_from_tup_of_races(races):
    expr = [ getattr(hh_persons.c,r) == 1 for r in races ]
    count_expr = hh_persons.c.RACNUM == len(races)
    name = str(races).replace(',', '&')
    return Predicate(name, pred=and_(*expr, count_expr))


if __name__ == '__main__':

    # for x in races_exactly_i:
    #     print(x)


    for y in it.combinations(race_attributes, 3):
        print(y)