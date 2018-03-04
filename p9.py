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

    one_race = Predicate(name='one_race', pred=hh_persons.c.RACNUM == 1,parent=not_hisp)
    two_plus_races = Predicate(name='two_or_more_races', pred=hh_persons.c.RACNUM >= 2,parent=not_hisp)
    # define the race enumeration used in the table
    # this generates statements like the following:
    #   Predicate('white-alone', and_(hh_persons.c.RACWHT == 1, hh_persons.c.RACNUM ==1))
    race_attributes = ['RACWHT', 'RACBLK', 'RACAIAN', 'RACASN', 'RACNHPI', 'RACSOR']
    race_alone_predicates = []
    for r in race_attributes:
        pred = Predicate(name=r + '-alone', pred=and_(getattr(hh_persons.c, r) == 1, hh_persons.c.RACNUM == 1),parent=one_race)
        race_alone_predicates.append(pred)


    two_races = Predicate(name='two_races', pred=hh_persons.c.RACNUM==2,parent=two_plus_races)
    three_races = Predicate(name='three_races', pred=hh_persons.c.RACNUM==3,parent=two_plus_races)
    four_races = Predicate(name='four_races', pred=hh_persons.c.RACNUM==4,parent=two_plus_races)
    five_races = Predicate(name='five_races', pred=hh_persons.c.RACNUM==5,parent=two_plus_races)
    six_races = Predicate(name='six_races', pred=hh_persons.c.RACNUM==6,parent=two_plus_races)

    two_races_predicates = list(combinations(race_attributes,2))
    for (r1,r2) in two_races_predicates:
        pred = Predicate(name= r1 + ' and ' + r2, pred=and_(getattr(hh_persons.c, r1) == 1, getattr(hh_persons.c, r2) == 1, hh_persons.c.RACNUM == 2),parent=two_races)

    three_races_predicates = list(combinations(race_attributes, 3))
    for (r1, r2, r3) in three_races_predicates:
        pred = Predicate(name = r1 + ', ' + r2 + ', and ' +r3, pred=and_(getattr(hh_persons.c, r1) == 1, getattr(hh_persons.c, r2) == 1, getattr(hh_persons.c, r3) == 1, hh_persons.c.RACNUM == 3),parent=three_races)

    four_races_predicates = list(combinations(race_attributes, 4))
    for (r1, r2, r3, r4) in four_races_predicates:
        pred = Predicate(name = r1 + ', ' + r2 + ', ' +r3 + ', and '+r4, pred=and_(getattr(hh_persons.c, r1) == 1, getattr(hh_persons.c, r2) == 1, getattr(hh_persons.c, r3) == 1,getattr(hh_persons.c, r4) == 1, hh_persons.c.RACNUM == 4),parent=four_races)

    five_races_predicates = list(combinations(race_attributes, 5))
    for (r1, r2, r3, r4, r5) in five_races_predicates:
        pred = Predicate(name = r1 + ', ' + r2 + ', ' +r3 + ', '+r4+', and '+r5, pred=and_(getattr(hh_persons.c, r1) == 1, getattr(hh_persons.c, r2) == 1, getattr(hh_persons.c, r3) == 1,getattr(hh_persons.c, r4) == 1, getattr(hh_persons.c, r5) == 1, hh_persons.c.RACNUM == 5),parent=five_races)

    six_races_predicates = list(combinations(race_attributes, 6))
    for (r1, r2, r3, r4, r5, r6) in six_races_predicates:
        pred = Predicate(name = r1 + ', ' + r2 + ', ' +r3 + ', '+r4+', '+r5+', and '+r6, pred=and_(getattr(hh_persons.c, r1) == 1, getattr(hh_persons.c, r2) == 1, getattr(hh_persons.c, r3) == 1,getattr(hh_persons.c, r4) == 1, getattr(hh_persons.c, r5) == 1, getattr(hh_persons.c,r6)==1, hh_persons.c.RACNUM == 6),parent=six_races)


    # create the table object, adding levels
    P9 = CensusTable('P9')
    P9.set_root_select('population')
    P9.add_ortho_level([hisp, not_hisp])


    # display the table
    P9.render(sql=False)
