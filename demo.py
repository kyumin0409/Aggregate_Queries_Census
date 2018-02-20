from census_table import CensusTable
from predicate import Predicate
from schema import hh_persons
from sqlalchemy.sql import and_, or_, not_, func, true


'''
Here is an example table from SF1, consisting of 17 queries:

P5.		0	HISPANIC OR LATINO ORIGIN BY RACE [17]
P5.		0	Universe:  Total population
P5.	1	0	Total:
P5.	2	1		Not Hispanic or Latino:
P5.	3	2			White alone
P5.	4	2			Black or African American alone
P5.	5	2			American Indian and Alaska Native alone
P5.	6	2			Asian alone
P5.	7	2			Native Hawaiian and Other Pacific Islander alone
P5.	8	2			Some Other Race alone
P5.	9	2			Two or More Races
P5.	10	1		Hispanic or Latino:
P5.	11	2			White alone
P5.	12	2			Black or African American alone
P5.	13	2			American Indian and Alaska Native alone
P5.	14	2			Asian alone
P5.	15	2			Native Hawaiian and Other Pacific Islander alone
P5.	16	2			Some Other Race alone
P5.	17	2			Two or More Races

'''


if __name__ == '__main__':

    # Note to avoid confusion:
    # a construction like this:  hh_persons.c.isHISP == 1
    # creates an sqlalchemy object defining a boolean expression on a defined schema
    # it is an instance of sqlalchemy.sql.expression.BinaryExpression


    # define the predicates for hispanic, not-hispanic
    hisp = Predicate(name='hisp', pred=hh_persons.c.isHISP == 1)
    not_hisp = Predicate(name='not_hisp', pred=hh_persons.c.isHISP == 0)


    # define the race enumeration used in the table
    # this generates statements like the following:
    #   Predicate('white-alone', and_(hh_persons.c.RACWHT == 1, hh_persons.c.RACNUM ==1))
    race_attributes = ['RACWHT', 'RACBLK', 'RACAIAN', 'RACASN', 'RACNHPI', 'RACSOR']
    race_alone_predicates = []
    for r in race_attributes:
        pred = Predicate(name=r + '-alone', pred=and_(getattr(hh_persons.c, r) == 1, hh_persons.c.RACNUM == 1))
        race_alone_predicates.append(pred)

    # add 'two-or-more-races'
    race_levels = race_alone_predicates + [Predicate('two-or-more-races', pred=(hh_persons.c.RACNUM >= 2))]


    # create the table object, adding levels
    P5 = CensusTable('P5')
    P5.set_root_select('population')
    P5.add_ortho_level([hisp, not_hisp])
    P5.add_ortho_level(race_levels)

    # display the table
    P5.render(sql=False)


'''
Output will be:

Total:	true
├── hisp:	hh_persons."isHISP" = 1
│   ├── RACWHT-alone:	hh_persons."RACWHT" = 1 AND hh_persons."RACNUM" = 1
│   ├── RACBLK-alone:	hh_persons."RACBLK" = 1 AND hh_persons."RACNUM" = 1
│   ├── RACAIAN-alone:	hh_persons."RACAIAN" = 1 AND hh_persons."RACNUM" = 1
│   ├── RACASN-alone:	hh_persons."RACASN" = 1 AND hh_persons."RACNUM" = 1
│   ├── RACNHPI-alone:	hh_persons."RACNHPI" = 1 AND hh_persons."RACNUM" = 1
│   ├── RACSOR-alone:	hh_persons."RACSOR" = 1 AND hh_persons."RACNUM" = 1
│   └── two-or-more-races:	hh_persons."RACNUM" >= 2
└── not_hisp:	hh_persons."isHISP" = 0
    ├── RACWHT-alone:	hh_persons."RACWHT" = 1 AND hh_persons."RACNUM" = 1
    ├── RACBLK-alone:	hh_persons."RACBLK" = 1 AND hh_persons."RACNUM" = 1
    ├── RACAIAN-alone:	hh_persons."RACAIAN" = 1 AND hh_persons."RACNUM" = 1
    ├── RACASN-alone:	hh_persons."RACASN" = 1 AND hh_persons."RACNUM" = 1
    ├── RACNHPI-alone:	hh_persons."RACNHPI" = 1 AND hh_persons."RACNUM" = 1
    ├── RACSOR-alone:	hh_persons."RACSOR" = 1 AND hh_persons."RACNUM" = 1
    └── two-or-more-races:	hh_persons."RACNUM" >= 2

calling P5.render(sql=True) will show the sql expressions

Total:	true
.  SELECT count(*) AS cnt
.  FROM hh_persons
.  WHERE true
├── hisp:	hh_persons."isHISP" = 1
│   .  SELECT count(*) AS cnt
│   .  FROM hh_persons
│   .  WHERE hh_persons."isHISP" = 1
│   ├── RACWHT-alone:	hh_persons."RACWHT" = 1 AND hh_persons."RACNUM" = 1
│   │   .  SELECT count(*) AS cnt
│   │   .  FROM hh_persons
│   │   .  WHERE hh_persons."isHISP" = 1 AND hh_persons."RACWHT" = 1 AND hh_persons."RACNUM" = 1
│   ├── RACBLK-alone:	hh_persons."RACBLK" = 1 AND hh_persons."RACNUM" = 1
│   │   .  SELECT count(*) AS cnt
│   │   .  FROM hh_persons
│   │   .  WHERE hh_persons."isHISP" = 1 AND hh_persons."RACBLK" = 1 AND hh_persons."RACNUM" = 1
│   ├── RACAIAN-alone:	hh_persons."RACAIAN" = 1 AND hh_persons."RACNUM" = 1
│   │   .  SELECT count(*) AS cnt
│   │   .  FROM hh_persons
│   │   .  WHERE hh_persons."isHISP" = 1 AND hh_persons."RACAIAN" = 1 AND hh_persons."RACNUM" = 1
│   ├── RACASN-alone:	hh_persons."RACASN" = 1 AND hh_persons."RACNUM" = 1
│   │   .  SELECT count(*) AS cnt
│   │   .  FROM hh_persons
│   │   .  WHERE hh_persons."isHISP" = 1 AND hh_persons."RACASN" = 1 AND hh_persons."RACNUM" = 1
│   ├── RACNHPI-alone:	hh_persons."RACNHPI" = 1 AND hh_persons."RACNUM" = 1
│   │   .  SELECT count(*) AS cnt
│   │   .  FROM hh_persons
│   │   .  WHERE hh_persons."isHISP" = 1 AND hh_persons."RACNHPI" = 1 AND hh_persons."RACNUM" = 1
│   ├── RACSOR-alone:	hh_persons."RACSOR" = 1 AND hh_persons."RACNUM" = 1
│   │   .  SELECT count(*) AS cnt
│   │   .  FROM hh_persons
│   │   .  WHERE hh_persons."isHISP" = 1 AND hh_persons."RACSOR" = 1 AND hh_persons."RACNUM" = 1
│   └── two-or-more-races:	hh_persons."RACNUM" >= 2
│       .  SELECT count(*) AS cnt
│       .  FROM hh_persons
│       .  WHERE hh_persons."isHISP" = 1 AND hh_persons."RACNUM" >= 2
└── not_hisp:	hh_persons."isHISP" = 0
    .  SELECT count(*) AS cnt
    .  FROM hh_persons
    .  WHERE hh_persons."isHISP" = 0
    ├── RACWHT-alone:	hh_persons."RACWHT" = 1 AND hh_persons."RACNUM" = 1
    │   .  SELECT count(*) AS cnt
    │   .  FROM hh_persons
    │   .  WHERE hh_persons."isHISP" = 0 AND hh_persons."RACWHT" = 1 AND hh_persons."RACNUM" = 1
    ├── RACBLK-alone:	hh_persons."RACBLK" = 1 AND hh_persons."RACNUM" = 1
    │   .  SELECT count(*) AS cnt
    │   .  FROM hh_persons
    │   .  WHERE hh_persons."isHISP" = 0 AND hh_persons."RACBLK" = 1 AND hh_persons."RACNUM" = 1
    ├── RACAIAN-alone:	hh_persons."RACAIAN" = 1 AND hh_persons."RACNUM" = 1
    │   .  SELECT count(*) AS cnt
    │   .  FROM hh_persons
    │   .  WHERE hh_persons."isHISP" = 0 AND hh_persons."RACAIAN" = 1 AND hh_persons."RACNUM" = 1
    ├── RACASN-alone:	hh_persons."RACASN" = 1 AND hh_persons."RACNUM" = 1
    │   .  SELECT count(*) AS cnt
    │   .  FROM hh_persons
    │   .  WHERE hh_persons."isHISP" = 0 AND hh_persons."RACASN" = 1 AND hh_persons."RACNUM" = 1
    ├── RACNHPI-alone:	hh_persons."RACNHPI" = 1 AND hh_persons."RACNUM" = 1
    │   .  SELECT count(*) AS cnt
    │   .  FROM hh_persons
    │   .  WHERE hh_persons."isHISP" = 0 AND hh_persons."RACNHPI" = 1 AND hh_persons."RACNUM" = 1
    ├── RACSOR-alone:	hh_persons."RACSOR" = 1 AND hh_persons."RACNUM" = 1
    │   .  SELECT count(*) AS cnt
    │   .  FROM hh_persons
    │   .  WHERE hh_persons."isHISP" = 0 AND hh_persons."RACSOR" = 1 AND hh_persons."RACNUM" = 1
    └── two-or-more-races:	hh_persons."RACNUM" >= 2
        .  SELECT count(*) AS cnt
        .  FROM hh_persons
        .  WHERE hh_persons."isHISP" = 0 AND hh_persons."RACNUM" >= 2


'''
