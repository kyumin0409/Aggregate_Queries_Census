from census_table import CensusTable
from predicate import Predicate
from schema import hh_persons
from sqlalchemy.sql import and_, or_, not_, func, true
from itertools import combinations

if __name__ == '__main__':

    male = Predicate(name='male', pred=hh_persons.c.SEX == 1)
    female = Predicate(name = 'female', pred=hh_persons.c.SEX == 2)

    under_5 = Predicate(name = 'Under 5 years', pred=hh_persons.c.AGEP < 5)
    five_to_nine = Predicate(name = '5 to 9 years', pred =and_(hh_persons.c.AGEP>=5, hh_persons.c.AGEP<=9))
    ten_to_fourteen = Predicate(name = '10 to 14 years', pred =and_(hh_persons.c.AGEP>=10, hh_persons.c.AGEP<=14))
    fifteen_to_seventeen = Predicate(name = '15 to 17 years', pred =and_(hh_persons.c.AGEP>=15, hh_persons.c.AGEP<=17))
    eighteen_and_nineteen = Predicate(name = '18 and 19 years', pred =or_(hh_persons.c.AGEP==18, hh_persons.c.AGEP==19))
    twenty = Predicate(name = '20 years', pred =(hh_persons.c.AGEP==20))
    twentyone = Predicate(name = '21 years', pred =(hh_persons.c.AGEP==21))
    twentytwo_to_twentyfour = Predicate(name = '22 to 24 years', pred =and_(hh_persons.c.AGEP>=22, hh_persons.c.AGEP<=24))
    twentyfive_to_twentynine = Predicate(name = '25 to 29 years', pred =and_(hh_persons.c.AGEP>=25, hh_persons.c.AGEP<=29))
    thirty_to_thirtyfour = Predicate(name = '30 to 34 years', pred =and_(hh_persons.c.AGEP>=30, hh_persons.c.AGEP<=34))
    thirtyfive_to_thirtynine = Predicate(name = '35 to 39 years', pred =and_(hh_persons.c.AGEP>=35, hh_persons.c.AGEP<=39))
    forty_to_fortyfour = Predicate(name = '40 to 44 years', pred =and_(hh_persons.c.AGEP>=40, hh_persons.c.AGEP<=44))
    fortyfive_to_fortynine = Predicate(name = '45 to 49 years', pred =and_(hh_persons.c.AGEP>=45, hh_persons.c.AGEP<=49))
    fifty_to_fiftyfour = Predicate(name = '50 to 54 years', pred =and_(hh_persons.c.AGEP>=50, hh_persons.c.AGEP<=54))
    fiftyfive_to_fiftynine = Predicate(name = '55 to 59 years', pred =and_(hh_persons.c.AGEP>=55, hh_persons.c.AGEP<=59))
    sixty_and_sixtyone = Predicate(name = '60 and 61 years', pred =or_(hh_persons.c.AGEP==60, hh_persons.c.AGEP==61))
    sixtytwo_to_sixtyfour = Predicate(name = '62 to 64 years', pred =and_(hh_persons.c.AGEP>=62,hh_persons.c.AGEP<=64))
    sixtyfive_and_sixtysix = Predicate(name = '65 and 66 years', pred =or_(hh_persons.c.AGEP==65, hh_persons.c.AGEP==66))
    sixtyseven_to_sixtynine = Predicate(name = '67 to 69 years', pred =and_(hh_persons.c.AGEP>=67, hh_persons.c.AGEP<=69))
    seventy_to_seventyfour = Predicate(name = '70 to 74 years', pred =and_(hh_persons.c.AGEP>=70, hh_persons.c.AGEP<=74))
    seventyfive_to_seventynine = Predicate(name = '75 to 79 years', pred =and_(hh_persons.c.AGEP>=75, hh_persons.c.AGEP<=79))
    eighty_to_eightyfour = Predicate(name = '80 to 84 years', pred =and_(hh_persons.c.AGEP>=80, hh_persons.c.AGEP<=84))
    eightyfive_and_over = Predicate(name = '85 years and over', pred =(hh_persons.c.AGEP>=85))

    age_groups = [under_5, five_to_nine, ten_to_fourteen, fifteen_to_seventeen, eighteen_and_nineteen, twenty, twentyone,
                twentytwo_to_twentyfour, twentyfive_to_twentynine, thirty_to_thirtyfour, thirtyfive_to_thirtynine,
                forty_to_fortyfour, fortyfive_to_fortynine, fifty_to_fiftyfour, fiftyfive_to_fiftynine,sixty_and_sixtyone,
                sixtytwo_to_sixtyfour, sixtyfive_and_sixtysix,sixtyseven_to_sixtynine,seventy_to_seventyfour,seventyfive_to_seventynine,
                eighty_to_eightyfour,eightyfive_and_over]

    P12 = CensusTable('P12')
    P12.set_root_select('population')
    P12.add_ortho_level([male,female])
    P12.add_ortho_level(age_groups)

    P12.render(sql=True)
