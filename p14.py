from census_table import CensusTable
from predicate import Predicate
from schema import hh_persons
from sqlalchemy.sql import and_, or_, not_, func, true
from itertools import combinations

if __name__ == '__main__':

    male = Predicate(name='male', pred=hh_persons.c.SEX == 1)
    female = Predicate(name = 'female', pred=hh_persons.c.SEX == 2)

    under_1 = Predicate(name='under 1 year', pred=hh_persons.c.AGEP<1)
    one = Predicate(name='1 year', pred=hh_persons.c.AGEP==1)
    two = Predicate(name='2 years', pred=hh_persons.c.AGEP==2)
    three = Predicate(name='3 years', pred=hh_persons.c.AGEP==3)
    four = Predicate(name='4 years', pred=hh_persons.c.AGEP==4)
    five = Predicate(name='5 years', pred=hh_persons.c.AGEP==5)
    six = Predicate(name='6 years', pred=hh_persons.c.AGEP==6)
    seven = Predicate(name='7 years', pred=hh_persons.c.AGEP==7)
    eight = Predicate(name='8 years', pred=hh_persons.c.AGEP==8)
    nine = Predicate(name='9 years', pred=hh_persons.c.AGEP==9)
    ten = Predicate(name='10 years', pred=hh_persons.c.AGEP==10)
    eleven = Predicate(name='11 years', pred=hh_persons.c.AGEP==11)
    twelve = Predicate(name='12 years', pred=hh_persons.c.AGEP==12)
    thirteen = Predicate(name='13 years', pred=hh_persons.c.AGEP==13)
    fourteen = Predicate(name='14 years', pred=hh_persons.c.AGEP==14)
    fifteen = Predicate(name='15 years', pred=hh_persons.c.AGEP==15)
    sixteen = Predicate(name='16 years', pred=hh_persons.c.AGEP==16)
    seventeen = Predicate(name='17 years', pred=hh_persons.c.AGEP==17)
    eighteen = Predicate(name='18 years', pred=hh_persons.c.AGEP==18)
    nineteen = Predicate(name='19 years', pred=hh_persons.c.AGEP==19)

    age = [under_1, one, two, three, four, five, six, seven, eight, nine, ten, eleven,
            twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen]

    P14 = CensusTable('P14')
    P14.set_root_select('under_20')
    P14.add_ortho_level([male,female])
    P14.add_ortho_level(age)

    P14.render(sql=True)
