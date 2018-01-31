from workload.census_table import CensusTable
from workload.predicate import Predicate
from workload.schema import hh_persons
from sqlalchemy.sql import and_, or_, not_, func, true

import workload.levels as lvl

sf1 = {}


'''
P1.		0	TOTAL POPULATION [1]				
P1.		0	Universe:  Total population				
P1.	1	0	Total				
'''
sf1['P1'] = CensusTable('P1')
sf1['P1'].set_root_select('population')

'''
# SELECT count(*) AS cnt 
# FROM hh_persons
Total:	true
'''

#TODO: P2: URBAN AND RURAL [6]

'''
P3.		0	RACE [8]				
P3.		0	Universe:  Total population				
P3.	1	0	Total:				
P3.	2	1		White alone			
P3.	3	1		Black or African American alone			
P3.	4	1		American Indian and Alaska Native alone			
P3.	5	1		Asian alone			
P3.	6	1		Native Hawaiian and Other Pacific Islander alone			
P3.	7	1		Some Other Race alone			
P3.	8	1		Two or More Races			
'''

sf1['P3'] = CensusTable('P3')
sf1['P3'].set_root_select('population')
sf1['P3'].add_ortho_level(lvl.race_levels)

'''
# SELECT count(*) AS cnt 
# FROM hh_persons
Total:	true
├── RACWHT-alone:	hh_persons."RACWHT" = 1 AND hh_persons."RACNUM" = 1
├── RACBLK-alone:	hh_persons."RACBLK" = 1 AND hh_persons."RACNUM" = 1
├── RACAIAN-alone:	hh_persons."RACAIAN" = 1 AND hh_persons."RACNUM" = 1
├── RACASN-alone:	hh_persons."RACASN" = 1 AND hh_persons."RACNUM" = 1
├── RACNHPI-alone:	hh_persons."RACNHPI" = 1 AND hh_persons."RACNUM" = 1
├── RACSOR-alone:	hh_persons."RACSOR" = 1 AND hh_persons."RACNUM" = 1
└── two-or-more-races:	hh_persons."RACNUM" >= 2
'''

'''
P4.		0	HISPANIC OR LATINO ORIGIN [3]				
P4.		0	Universe:  Total population				
P4.	1	0	Total:				
P4.	2	1		Not Hispanic or Latino			
P4.	3	1		Hispanic or Latino			
'''

sf1['P4'] = CensusTable('P4')
sf1['P4'].set_root_select('population')
sf1['P4'].add_ortho_level([lvl.hisp, lvl.not_hisp])

'''
# SELECT count(*) AS cnt 
# FROM hh_persons
Total:	true
├── hisp:	hh_persons."isHISP" = 1
└── not_hisp:	hh_persons."isHISP" = 0
'''

'''
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

sf1['P5'] = CensusTable('P5')
sf1['P5'].set_root_select('population')
sf1['P5'].add_ortho_level([lvl.hisp, lvl.not_hisp])
sf1['P5'].add_ortho_level(lvl.race_levels)

'''
# SELECT count(*) AS cnt 
# FROM hh_persons
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
'''


#TODO: P6: RACE (TOTAL RACES TALLIED) [7]
#TODO: P7: HISPANIC OR LATINO ORIGIN BY RACE (TOTAL RACES TALLIED) [15]


'''
P8.		0	RACE [71]				
P8.		0	Universe: Total population				
P8.	1	0	Total:				
P8.	2	1		Population of one race:			
P8.	3	2			White alone		
P8.	4	2			Black or African American alone		
P8.	5	2			American Indian and Alaska Native alone		
P8.	6	2			Asian alone		
P8.	7	2			Native Hawaiian and Other Pacific Islander alone		
P8.	8	2			Some Other Race alone		
P8.	9	1		Two or More Races:    			
P8.	10	2			Population of two races:		
P8.	11	3				White; Black or African American	
P8.	12	3				White; American Indian and Alaska Native 	
P8.	13	3				White; Asian	
P8.	14	3				White; Native Hawaiian and Other Pacific Islander	
P8.	15	3				White; Some Other Race	
P8.	16	3				Black or African American; American Indian and Alaska Native 	
P8.	17	3				Black or African American; Asian	
P8.	18	3				Black or African American; Native Hawaiian and Other Pacific Islander	
P8.	19	3				Black or African American; Some Other Race	
P8.	20	3				American Indian and Alaska Native; Asian	
P8.	21	3				American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander	
P8.	22	3				American Indian and Alaska Native; Some Other Race	
P8.	23	3				Asian; Native Hawaiian and Other Pacific Islander	
P8.	24	3				Asian; Some Other Race	
P8.	25	3				Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	26	2			Population of three races:		
P8.	27	3				White; Black or African American; American Indian and Alaska Native 	
P8.	28	3				White; Black or African American; Asian	
P8.	29	3				White; Black or African American; Native Hawaiian and Other Pacific Islander	
P8.	30	3				White; Black or African American; Some Other Race	
P8.	31	3				White; American Indian and Alaska Native; Asian	
P8.	32	3				White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander	
P8.	33	3				White; American Indian and Alaska Native; Some Other Race	
P8.	34	3				White; Asian; Native Hawaiian and Other Pacific Islander	
P8.	35	3				White; Asian; Some Other Race	
P8.	36	3				White; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	37	3				Black or African American; American Indian and Alaska Native; Asian	
P8.	38	3				Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander	
P8.	39	3				Black or African American; American Indian and Alaska Native; Some Other Race	
P8.	40	3				Black or African American; Asian; Native Hawaiian and Other Pacific Islander	
P8.	41	3				Black or African American; Asian; Some Other Race	
P8.	42	3				Black or African American; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	43	3				American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander 	
P8.	44	3				American Indian and Alaska Native; Asian; Some Other Race	
P8.	45	3				American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	46	3				Asian; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	47	2			Population of four races:		
P8.	48	3				White; Black or African American; American Indian and Alaska Native; Asian	
P8.	49	3				White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander	
P8.	50	3				White; Black or African American; American Indian and Alaska Native; Some Other Race	
P8.	51	3				White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander	
P8.	52	3				White; Black or African American; Asian; Some Other Race	
P8.	53	3				White; Black or African American; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	54	3				White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander	
P8.	55	3				White; American Indian and Alaska Native; Asian; Some Other Race	
P8.	56	3				White; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	57	3				White; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	58	3				Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander	
P8.	59	3				Black or African American; American Indian and Alaska Native; Asian; Some Other Race	
P8.	60	3				Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	61	3				Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	62	3				American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	63	2			Population of five races:		
P8.	64	3				White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander	
P8.	65	3				White; Black or African American; American Indian and Alaska Native; Asian; Some Other Race	
P8.	66	3				White; Black or African American; American Indian and Alaska Native; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	67	3				White; Black or African American; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	68	3				White; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	69	3				Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race	
P8.	70	2			Population of six races:		
P8.	71	3				White; Black or African American; American Indian and Alaska Native; Asian; Native Hawaiian and Other Pacific Islander; Some Other Race	
'''











if __name__ == '__main__':

    # display the table
    sf1['P4'].render(sql=False)


