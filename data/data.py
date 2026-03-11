import csv

# this is the list of columns in the CSV from the parquet file
"""
#bytes
#path
0 CompensationOffice1
1 BZKNr
2 Layout class
3 ApplicantFirstName
4 ApplicantLastName
5 ApplicantAltFirstName
6 ApplicantBirthName
7 ApplicantAltLastName
8 ApplicantBirthDate
9 ApplicantBirthPlace
10 ApplicantCurrentAddress
11 VictimFirstName
12 VictimLastName
13 VictimAltFirstName
14 VictimBirthName
15 VictimAltLastName
16 VictimBirthDate
17 VictimBirthPlace
18 VictimDeathDate
19 VictimDeathPlace
"""

offices={}  # we need that to map different occurences of the same offices

# gets increased for each new IRI
IRIcount=0

'''
creates new IRI
'''
def niri():
	global IRIcount
	IRIcount = IRIcount + 1
	return "http://bzk.fiz-karlsruhe.de/data/" + str(IRIcount)


prefix = """

@prefix owl: <http://www.w3.org/2002/07/owl#> .

# reused classes
@prefix organization: <http://purl.obolibrary.org/obo/OBI_0000245> .
@prefix site: <http://purl.obolibrary.org/obo/BFO_0000029> .
@prefix address: <http://purl.obolibrary.org/obo/IAO_0000422> . # postal addresss
@prefix organization_name: <http://purl.obolibrary.org/obo/IAO_0000303> . # institutional identification
@prefix process: <http://purl.obolibrary.org/obo/BFO_0000015> . 
@prefix given_name: <http://purl.obolibrary.org/obo/IAO_0020016> .
@prefix last_name: <http://purl.obolibrary.org/obo/IAO_0020017> .

@prefix has_role: <http://purl.obolibrary.org/obo/RO_0000087> .
@prefix denoted_by: <http://purl.obolibrary.org/obo/IAO_0000235> .
@prefix has_value: <https://nfdi.fiz-karlsruhe.de/ontology/NFDI_0001007> .
@prefix realized_in: <http://purl.obolibrary.org/obo/BFO_0000054> .
@prefix participates_in: <http://purl.obolibrary.org/obo/RO_0000056> .
@prefix has_participant: <http://purl.obolibrary.org/obo/RO_0000057> .
@prefix is_about: <http://purl.obolibrary.org/obo/IAO_0000136> .
@prefix concretizes:  <http://purl.obolibrary.org/obo/RO_0000059> .
@prefix occupies_temporal_region: <http://purl.obolibrary.org/obo/BFO_0000199> .
@prefix denotes: <http://purl.obolibrary.org/obo/IAO_0000219> .
@prefix realizes: <http://purl.obolibrary.org/obo/BFO_0000055> .
@prefix environs: <http://purl.obolibrary.org/obo/BFO_0000183> .
@prefix temporal_instant: <http://purl.obolibrary.org/obo/BFO_0000203> .
@prefix person: <https://nfdi.fiz-karlsruhe.de/ontology/NFDI_0000004> .

# new required BZK classes

@prefix alt_first_name: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000005> .
@prefix alt_last_name: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000007> .
@prefix birth_name: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000006> .
@prefix identifier: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000003> .
@prefix has_time: <http://www.w3.org/2006/time#inXSDDate> .
@prefix office_role: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000004> .
@prefix applicant_role: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000001> .
@prefix victim_role: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000000> .
@prefix card: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000002> .  # bfo object
@prefix death_place_role: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000008> .
@prefix birth_place_role: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000009> .

[ a owl:Ontology ;
   owl:imports <https://nfdi.fiz-karlsruhe.de/ontology/3.0.4>
 ] .

"""

print (prefix)


office_tmplt="""
<OFFICEIRI> a organization: .
<OFFICEIRI> has_role: <OFFICEIRI_role> .
<OFFICEIRI_role> a office_role: .
<OFFICEIRI> denoted_by: <OFFICEIRI_name> . 
<OFFICEIRI_name> a organization_name: .
<OFFICEIRI_name> has_value: "NAME" .
"""

office_process="""
<OFFICEIRI_role> realized_in: <CASEIRI> .
<OFFICEIRI> participates_in: <CASEIRI> .
"""

bzk_num_tmplt="""
<BZKIRI> a identifier: .
<BZKIRI> has_value: "BZKLABEL" .
<BZKIRI> is_about: <BZKIRI_card> . 
<BZKIRI_card> a card: . 
<BZKIRI_card> participates_in: <CASEIRI> .
<CASEIRI> concretizes: <BZKIRI> .
<CASEIRI> a process: .
"""

def getNameTmplt(nametype):
	return """
<NAMEIRI> a """ + nametype + """ .
<NAMEIRI> denotes: <PERSONIRI> . 
<NAMEIRI> has_value: "NAMELABEL" .
	"""

case_has_applicant="""
<APPLICANT> participates_in: <CASEIRI> .
<APPLICANT> a person: .
<APPLICANT> has_role: applicant_role: .
<CASEIRI> realizes: applicant_role: .
"""

case_has_victim="""
<VICTIM> participates_in: <CASEIRI> .
<VICTIM> a person: .
<VICTIM> has_role: victim_role: .
<CASEIRI> realizes: victim_role: .
"""


birth_tmplt="""
<BIRTH> a process: . 
<BIRTH> has_participant: <PERSON> .
"""

birth_date_tmplt="""
<BIRTH> occupies_temporal_region: <BIRTH_instant> .
<BIRTH_instant> a temporal_instant: .
<BIRTH_instant> has_time: "TIME" .
"""

birth_place_tmplt="""
<BIRTH_place> environs: <BIRTH> .
<BIRTH_place> a site: .
<BIRTH_place> has_role: birth_place_role: .
<BIRTH_place> has_value: "PLACELABEL" .
"""

address="""
<ADDRESS> a address: .
<ADDRESS> has_value: "ADDRLABEL" .
<ADDRESS> is_about: <AGENT> .
"""

death_tmplt="""
<DEATH> a process: . 
<DEATH> has_participant: <PERSON> .
"""

death_date_tmplt="""
<DEATH> occupies_temporal_region: <DEATH_instant> .
<DEATH_instant> a temporal_instant: .
<DEATH_instant> has_time: "TIME" .
"""

death_place_tmplt="""
<DEATH_place> environs: <DEATH> .
<DEATH_place> a site: .
<DEATH_place> has_role: death_place_role: .
<DEATH_place> has_value: "PLACELABEL" .
"""


with open('test.csv', newline='') as csvfile:
	reader = csv.reader(csvfile)
	next(reader, None) # skip header row

	for row in reader:
		if len(row)>0:  
			print ("#", row)

			# the IRI of the compensation case (the row)
			caseIRI=niri()

			

			office = row[0]
			if office:
				# compensation office gets disambiguated by exact string match
				if not office in offices.keys():

					officeIRI=niri()
					offices[office]=officeIRI
					officeRDF=office_tmplt.replace("OFFICEIRI", officeIRI).replace("CASEIRI", caseIRI).replace("NAME", office)
					print (officeRDF) 

				officeIRI=offices[office]
				officeCaseRDF = office_process.replace("OFFICEIRI", officeIRI).replace("CASEIRI", caseIRI)
				print (officeCaseRDF) 

			bzknum = row[1]
			if bzknum:
				bzknumiri = niri()
				bzkRDF=bzk_num_tmplt.replace("BZKIRI", bzknumiri).replace("BZKLABEL", bzknum).replace("CASEIRI", caseIRI)
				print (bzkRDF)

			
			applicantIRI=niri()

			applicantFirstName=row[3]
			if applicantFirstName:
				iri = applicantIRI+"_firstname"
				applicantFirstNameRDF = getNameTmplt("given_name:").replace("NAMEIRI", iri).replace("NAMELABEL", applicantFirstName).replace("PERSONIRI", applicantIRI)
				print (applicantFirstNameRDF)

			applicantLastName=row[4]
			if applicantLastName:
				iri = applicantIRI+"_lastname"
				applicantLastNameRDF = getNameTmplt("last_name:").replace("NAMEIRI", iri).replace("NAMELABEL", applicantLastName).replace("PERSONIRI", applicantIRI)
				print (applicantLastNameRDF)
		
			applicantAltFirstName=row[5]
			if applicantAltFirstName:
				iri = applicantIRI+"_altfirstname"
				applicantAltFirstNameRDF = getNameTmplt("alt_first_name:").replace("NAMEIRI", iri).replace("NAMELABEL", applicantAltFirstName).replace("PERSONIRI", applicantIRI)
				print (applicantAltFirstNameRDF)

			applicantBirthName=row[6]
			if applicantBirthName:
				iri = applicantIRI+"_birthname"
				applicantBirthNameRDF = getNameTmplt("birth_name:").replace("NAMEIRI", iri).replace("NAMELABEL", applicantBirthName).replace("PERSONIRI", applicantIRI)
				print (applicantBirthNameRDF)

			applicantAltLastName=row[7]
			if applicantAltLastName:
				iri = applicantIRI+"_altlastname"
				applicantAltLastNameRDF = getNameTmplt("alt_last_name:").replace("NAMEIRI", iri).replace("NAMELABEL", applicantAltLastName).replace("PERSONIRI", applicantIRI)
				print (applicantAltLastNameRDF)

			if applicantFirstName or applicantLastName or applicantAltFirstName or applicantBirthName or applicantAltLastName:
				print (case_has_applicant.replace("CASEIRI", caseIRI).replace("APPLICANT", applicantIRI))
			


			birthIRI=applicantIRI+"_birth"
			birthRDF=birth_tmplt.replace("BIRTH", birthIRI).replace("PERSON", applicantIRI)

			applicantBirthDate=row[8]
			if applicantBirthDate:
				birthDateRDF=birth_date_tmplt.replace("BIRTH", birthIRI).replace("TIME", applicantBirthDate)
				print (birthDateRDF)

			applicantBirthPlace=row[9]
			if applicantBirthPlace:
				birthPlaceRDF=birth_place_tmplt.replace("BIRTH", birthIRI).replace("PLACELABEL", applicantBirthPlace)
				print (birthPlaceRDF)

			if applicantBirthPlace or applicantBirthDate:
				print (birthRDF)

			applicantCurrentAddress=row[10]
			if applicantCurrentAddress:
				adressRDF=address.replace("ADDRESS", applicantIRI+"_address").replace("ADDRLABEL", applicantCurrentAddress).replace("AGENT", applicantIRI)
				print (adressRDF)



			victimIRI=niri()

			victimFirstName=row[11]
			if victimFirstName:
				iri = victimIRI+"_firstname"
				victimFirstNameRDF = getNameTmplt("given_name:").replace("NAMEIRI", iri).replace("NAMELABEL", victimFirstName).replace("PERSONIRI", victimIRI)
				print (victimFirstNameRDF)

			victimLastName=row[12]
			if victimLastName:
				iri = victimIRI+"_lastname"
				victimLastNameRDF = getNameTmplt("last_name:").replace("NAMEIRI", iri).replace("NAMELABEL", victimLastName).replace("PERSONIRI", victimIRI)
				print (victimLastNameRDF)
		
			victimAltFirstName=row[13]
			if victimAltFirstName:
				iri = victimIRI+"_altfirstname"
				victimAltFirstNameRDF = getNameTmplt("alt_first_name:").replace("NAMEIRI", iri).replace("NAMELABEL", victimAltFirstName).replace("PERSONIRI", victimIRI)
				print (victimAltFirstNameRDF)

			victimBirthName=row[14]
			if victimBirthName:
				iri = victimIRI+"_birthname"
				victimBirthNameRDF = getNameTmplt("birth_name:").replace("NAMEIRI", iri).replace("NAMELABEL", victimBirthName).replace("PERSONIRI", victimIRI)
				print (victimBirthNameRDF)

			victimAltLastName=row[15]
			if victimAltLastName:
				iri = victimIRI+"_altlastname"
				victimAltLastNameRDF = getNameTmplt("alt_last_name:").replace("NAMEIRI", iri).replace("NAMELABEL", victimAltLastName).replace("PERSONIRI", victimIRI)
				print (victimAltLastNameRDF)

			if victimFirstName or victimLastName or victimAltFirstName or victimBirthName or victimAltLastName:
				print (case_has_victim.replace("CASEIRI", caseIRI).replace("VICTIM", victimIRI))


			birthIRI=victimIRI+"_birth"
			birthRDF=birth_tmplt.replace("BIRTH", birthIRI).replace("PERSON", victimIRI)

			victimBirthDate=row[16]
			if victimBirthDate:
				birthDateRDF=birth_date_tmplt.replace("BIRTH", birthIRI).replace("TIME", victimBirthDate)
				print (birthDateRDF)

			victimBirthPlace=row[17]
			if victimBirthPlace:
				birthPlaceRDF=birth_place_tmplt.replace("BIRTH", birthIRI).replace("PLACELABEL", victimBirthPlace)
				print (birthPlaceRDF)

			if victimBirthPlace or victimBirthDate:
				print (birthRDF)

			deathIRI=victimIRI+"_death"
			deathRDF=death_tmplt.replace("DEATH", deathIRI).replace("PERSON", victimIRI)

			victimDeathDate=row[16]
			if victimDeathDate:
				deathDateRDF=death_date_tmplt.replace("DEATH", deathIRI).replace("TIME", victimDeathDate)
				print (deathDateRDF)

			victimDeathPlace=row[17]
			if victimDeathPlace:
				deathPlaceRDF=death_place_tmplt.replace("DEATH", deathIRI).replace("PLACELABEL", victimDeathPlace)
				print (deathPlaceRDF)

			if victimDeathPlace or victimDeathDate:
				print (deathRDF)




