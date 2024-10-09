#Preadvise  - use   collab for getting results
import pandas as pd

scraper = pd.read_html("https://en.wikipedia.org/wiki/Graduate_Aptitude_Test_in_Engineering")
scraper # Run it, you will get all tables of webpage

# for i, table in enumerate(scraper):
#   print("______")
#   print(i)
#   print(table)

scraper[2]# Indexing indicates the required table no. to be print
df = scraper[2]

df.to_csv('GATE_database.csv',index=False)
df_scraped_file = pd.read_csv('premier_league.csv')
df_scraped_file

"""
	* Engineering Sciences (XE) Paper Sections (A and any 2 of B to H)	Code	** Life Sciences (XL) Paper Sections (P and any 2 of Q to U)	Code.1	Humanities and Social Sciences (XH) Paper Sections (B1 and any 1 of C1 to C6)	Code.2
0	Engineering Mathematics (Compulsory)	A	Chemistry (Compulsory)	P	Reasoning and Comprehension (Compulsory)	B1
1	Fluid Mechanics	B	Biochemistry	Q	Economics	C1
2	Materials Science	C	Botany	R	English	C2
3	Solid Mechanics	D	Microbiology	S	Linguistics	C3
4	Thermodynamics	E	Zoology	T	Philosophy	C4
5	Polymer Science and Engineering	F	Food Technology	U	Psychology	C5
6	Food Technology	G	NaN	NaN	Sociology	C6
7	Atmospheric and Oceanic Sciences	H	NaN	NaN	NaN	NaN

"""


