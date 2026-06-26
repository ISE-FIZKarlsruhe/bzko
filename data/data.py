import csv

# this is the list of columns in the CSV from the parquet file
"""
0 split_row
1 CompensationOffice1
2 BZKNr
3 Layout class
4 ApplicantFirstName
5 ApplicantLastName
6 ApplicantAltFirstName
7 ApplicantBirthName
8 ApplicantAltLastName
9 ApplicantBirthDate
# ApplicantBirthPlace
# ApplicantCurrentAddress
10 VictimFirstName
11 VictimLastName
12 VictimAltFirstName
13 VictimBirthName
14 VictimAltLastName
15 VictimBirthDate
# VictimBirthPlace
16 VictimDeathDate
# VictimDeathPlace
"""

offices={}  # we need that to map different occurences of the same offices // exact string matching

split_row_cases={} # a mapping between split_row and case IRI // needed for second pass (addresses)

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
@prefix organization: <http://purl.obolibrary.org/obo/OBI_0000245> . #
@prefix site: <http://purl.obolibrary.org/obo/BFO_0000029> . 

@prefix address: <http://purl.obolibrary.org/obo/IAO_0000422> . # postal address
@prefix last_residential_address: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010006> .
@prefix organization_name: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010005> . # compensation office name
@prefix bzk_process: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010000> . 
@prefix given_name: <http://purl.obolibrary.org/obo/IAO_0020016> .
@prefix last_name: <http://purl.obolibrary.org/obo/IAO_0020017> .
@prefix alt_first_name: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010007> .
@prefix alt_last_name: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000007> .
@prefix birth_name: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000006> .
@prefix unit_number: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000016> .
@prefix street_name: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000014> .
@prefix house_number: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000015> . 
@prefix postal_code: <https://nfdi.fiz-karlsruhe.de/ontology/NFDI_0001041> . 
@prefix neighborhood: <https://bzk.fiz-karlsruhe.de/ontology/BZK_X010020> .
@prefix city: <https://nfdi.fiz-karlsruhe.de/ontology/NFDI_0000106> .
@prefix district: <https://bzk.fiz-karlsruhe.de/ontology/BZK_X010021> .
@prefix place: <https://nfdi.fiz-karlsruhe.de/ontology/NFDI_0000005> .
@prefix region: <https://bzk.fiz-karlsruhe.de/ontology/BZK_X010022> .
@prefix state: <https://nfdi.fiz-karlsruhe.de/ontology/NFDI_0000134> .
@prefix country: <https://nfdi.fiz-karlsruhe.de/ontology/NFDI_0000119> .
@prefix bzk_nummer: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000003> . # the bzk nummer
#@prefix has_time: <http://www.w3.org/2006/time#inXSDDate> .
@prefix has_time: <http://www.w3.org/2000/01/rdf-schema#label> . # currently not formatted properly
@prefix has_label: <http://www.w3.org/2000/01/rdf-schema#label> . 
@prefix office_role: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010001> .
@prefix applicant_role: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010003> .
@prefix persecutee_role: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010002> . # persecutee role
@prefix card: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0000002> .  # bfo object
@prefix digitized_card: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010011> . #i.c.e
@prefix death_process_boundary: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010009> .
@prefix birth_process_boundary: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010008> .
@prefix last_residential_address: <https://bzk.fiz-karlsruhe.de/ontology/BZK_0010006> .
@prefix denotes: <http://purl.obolibrary.org/obo/IAO_0000219> .

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
@prefix causally_influenced_by: <http://purl.obolibrary.org/obo/RO_0000087> .
@prefix occurs_in: <http://purl.obolibrary.org/obo/BFO_0000066> .
@prefix has_part: <http://purl.obolibrary.org/obo/BFO_0000051> . 
@prefix causally_influences: <http://purl.obolibrary.org/obo/RO_0002566> .
@prefix located_in: <http://purl.obolibrary.org/obo/RO_0001025> .

## we need these assertions, otherwise Protege/Owlapi inferring them as annotation properties
has_role: a owl:ObjectProperty .
denoted_by: a owl:ObjectProperty .
realized_in: a owl:ObjectProperty .
participates_in: a owl:ObjectProperty .
has_participant: a owl:ObjectProperty .
is_about: a owl:ObjectProperty .
concretizes:  a owl:ObjectProperty .
occupies_temporal_region: a owl:ObjectProperty .
denotes: a owl:ObjectProperty .
realizes: a owl:ObjectProperty .
environs: a owl:ObjectProperty .
causally_influenced_by: a owl:ObjectProperty .
causally_influences: a owl:ObjectProperty .
occurs_in: a owl:ObjectProperty .
has_part: a owl:ObjectProperty .

has_value: a owl:DatatypeProperty .
"""

print (prefix)


office_tmplt="""
<OFFICEIRI> a organization: .
<OFFICEIRI> has_role: <OFFICEIRI_role> .
<OFFICEIRI_role> a office_role: .
<OFFICEIRI> denoted_by: <OFFICEIRI_name> . 
<OFFICEIRI_name> a organization_name: .
<OFFICEIRI_name> has_label: "NAME" .
"""

office_process="""
<OFFICEIRI_role> realized_in: <CASEIRI> .
<OFFICEIRI> participates_in: <CASEIRI> .
"""

bzk_card_tmplt="""
<BZKIRI_card> a card: . 
<BZKIRI_card> participates_in: <CASEIRI> .
<BZKIRI_digicard> a digitized_card: . 
<BZKIRI_digicard> is_about: <BZKIRI_card> .
<CASEIRI> concretizes: <BZKIRI_digicard> .
"""

bzk_num_tmplt="""
<BZKIRI> a bzk_nummer: .
<BZKIRI> has_label: "BZKLABEL" .
<BZKIRI> denotes: <BZKIRI_card> . 

"""

def getNameTmplt(nametype):
	return """
<NAMEIRI> a """ + nametype + """ .
<NAMEIRI> denotes: <PERSONIRI> . 
<NAMEIRI> has_label: "NAMELABEL" .
	"""

case_has_applicant="""
<APPLICANT> participates_in: <CASEIRI> .
<APPLICANT> a person: .
<APPLICANT> has_role: <APPLICANT_appl_role> .
<CASEIRI> realizes: <APPLICANT_appl_role> .
<APPLICANT_appl_role> a applicant_role: .
"""

case_has_victim="""
<VICTIM> participates_in: <CASEIRI> .
<VICTIM> a person: .
<VICTIM> has_role: <VICTIM_per_role> .
<CASEIRI> realizes: <VICTIM_per_role> .
<VICTIM_per_role> a persecutee_role: .
"""


birth_tmplt="""
<BIRTH> a birth_process_boundary: . 
<BIRTH> has_participant: <PERSON> .
"""

birth_date_tmplt="""
<BIRTH> occupies_temporal_region: <BIRTH_instant> .
<BIRTH_instant> a temporal_instant: .
<BIRTH_instant> has_time: "TIME" .
"""




death_tmplt="""
<DEATH> a death_process_boundary: . 
<DEATH> has_participant: <PERSON> .
"""

death_date_tmplt="""
<DEATH> occupies_temporal_region: <DEATH_instant> .
<DEATH_instant> a temporal_instant: .
<DEATH_instant> has_time: "TIME" .
"""





with open('bzkopen-2026-04-17/bzkopen_raw_validation.csv', newline='') as csvfile:
	reader = csv.reader(csvfile)
	next(reader, None) # skip header row

	for row in reader:
		if len(row)>0:  
			print ("#", row)

			# the IRI of the compensation case (the row)
			caseIRI=niri()
			print (f"<{caseIRI}> a bzk_process: .")
			split_row = row[0]
			split_row_cases[split_row]={"case": caseIRI}

			office = row[1]
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

			bzknum = row[2]
			bzknumiri = niri()
			split_row_cases[split_row]["bzkcardiri"]=bzknumiri+"_card"

			#  we always have a bzk card; also if there is no bzk number (probably the number was not readable)
			print (bzk_card_tmplt.replace("BZKIRI", bzknumiri).replace("CASEIRI", caseIRI))

			if bzknum:
				bzkRDF=bzk_num_tmplt.replace("BZKIRI", bzknumiri).replace("BZKLABEL", bzknum)
				print (bzkRDF)
				

			
			applicantIRI=niri()

			split_row_cases[split_row]["applicant"]=applicantIRI

			applicantFirstName=row[4]
			if applicantFirstName:
				iri = applicantIRI+"_firstname"
				applicantFirstNameRDF = getNameTmplt("given_name:").replace("NAMEIRI", iri).replace("NAMELABEL", applicantFirstName).replace("PERSONIRI", applicantIRI)
				print (applicantFirstNameRDF)

			applicantLastName=row[5]
			if applicantLastName:
				iri = applicantIRI+"_lastname"
				applicantLastNameRDF = getNameTmplt("last_name:").replace("NAMEIRI", iri).replace("NAMELABEL", applicantLastName).replace("PERSONIRI", applicantIRI)
				print (applicantLastNameRDF)
		
			applicantAltFirstName=row[6]
			if applicantAltFirstName:
				iri = applicantIRI+"_altfirstname"
				applicantAltFirstNameRDF = getNameTmplt("alt_first_name:").replace("NAMEIRI", iri).replace("NAMELABEL", applicantAltFirstName).replace("PERSONIRI", applicantIRI)
				print (applicantAltFirstNameRDF)

			applicantBirthName=row[7]
			if applicantBirthName:
				iri = applicantIRI+"_birthname"
				applicantBirthNameRDF = getNameTmplt("birth_name:").replace("NAMEIRI", iri).replace("NAMELABEL", applicantBirthName).replace("PERSONIRI", applicantIRI)
				print (applicantBirthNameRDF)

			applicantAltLastName=row[8]
			if applicantAltLastName:
				iri = applicantIRI+"_altlastname"
				applicantAltLastNameRDF = getNameTmplt("alt_last_name:").replace("NAMEIRI", iri).replace("NAMELABEL", applicantAltLastName).replace("PERSONIRI", applicantIRI)
				print (applicantAltLastNameRDF)

			if applicantFirstName or applicantLastName or applicantAltFirstName or applicantBirthName or applicantAltLastName:
				print (case_has_applicant.replace("CASEIRI", caseIRI).replace("APPLICANT", applicantIRI))
			


			birthIRI=applicantIRI+"_birth"
			birthRDF=birth_tmplt.replace("BIRTH", birthIRI).replace("PERSON", applicantIRI)

			applicantBirthDate=row[9]
			if applicantBirthDate:
				birthDateRDF=birth_date_tmplt.replace("BIRTH", birthIRI).replace("TIME", applicantBirthDate)
				print (birthRDF)
				print (birthDateRDF)

			split_row_cases[split_row]["applicant"]=applicantIRI
			split_row_cases[split_row]["applicant_birth"]=birthIRI
			split_row_cases[split_row]["applicant_birth_rdf"]=birthRDF ## we will print it again for the place, if existing


			victimIRI=niri()
			split_row_cases[split_row]["victim"]=victimIRI

			victimFirstName=row[10]
			if victimFirstName:
				iri = victimIRI+"_firstname"
				victimFirstNameRDF = getNameTmplt("given_name:").replace("NAMEIRI", iri).replace("NAMELABEL", victimFirstName).replace("PERSONIRI", victimIRI)
				print (victimFirstNameRDF)

			victimLastName=row[11]
			if victimLastName:
				iri = victimIRI+"_lastname"
				victimLastNameRDF = getNameTmplt("last_name:").replace("NAMEIRI", iri).replace("NAMELABEL", victimLastName).replace("PERSONIRI", victimIRI)
				print (victimLastNameRDF)
		
			victimAltFirstName=row[12]
			if victimAltFirstName:
				iri = victimIRI+"_altfirstname"
				victimAltFirstNameRDF = getNameTmplt("alt_first_name:").replace("NAMEIRI", iri).replace("NAMELABEL", victimAltFirstName).replace("PERSONIRI", victimIRI)
				print (victimAltFirstNameRDF)

			victimBirthName=row[13]
			if victimBirthName:
				iri = victimIRI+"_birthname"
				victimBirthNameRDF = getNameTmplt("birth_name:").replace("NAMEIRI", iri).replace("NAMELABEL", victimBirthName).replace("PERSONIRI", victimIRI)
				print (victimBirthNameRDF)

			victimAltLastName=row[14]
			if victimAltLastName:
				iri = victimIRI+"_altlastname"
				victimAltLastNameRDF = getNameTmplt("alt_last_name:").replace("NAMEIRI", iri).replace("NAMELABEL", victimAltLastName).replace("PERSONIRI", victimIRI)
				print (victimAltLastNameRDF)

			if victimFirstName or victimLastName or victimAltFirstName or victimBirthName or victimAltLastName:
				print (case_has_victim.replace("CASEIRI", caseIRI).replace("VICTIM", victimIRI))


			birthIRI=victimIRI+"_birth"
			birthRDF=birth_tmplt.replace("BIRTH", birthIRI).replace("PERSON", victimIRI)

			split_row_cases[split_row]["persecutee"]=victimIRI
			split_row_cases[split_row]["persecutee_birth"]=birthIRI
			split_row_cases[split_row]["persecutee_birth_rdf"]=birthRDF

			victimBirthDate=row[15]
			if victimBirthDate:
				birthDateRDF=birth_date_tmplt.replace("BIRTH", birthIRI).replace("TIME", victimBirthDate)
				print (birthRDF)
				print (birthDateRDF)


			deathIRI=victimIRI+"_death"
			deathRDF=death_tmplt.replace("DEATH", deathIRI).replace("PERSON", victimIRI)
			split_row_cases[split_row]["persecutee_death"]=deathIRI
			split_row_cases[split_row]["persecutee_death_rdf"]=deathRDF

			victimDeathDate=row[16]
			if victimDeathDate:
				deathDateRDF=death_date_tmplt.replace("DEATH", deathIRI).replace("TIME", victimDeathDate)
				print (deathRDF)
				print (deathDateRDF)




address_tmplt="""
<ADDRESS> a address: .
<ADDRESS> has_label: "ADDRLABEL" .
#<ADDRESS> is_about: <PLACE> .
<PLACE> a place: . 
<PLACE> has_label: "ADDRLABEL" .
"""

unit_tmplt="""
#<UNIT> a unit_number: .
#<UNIT> has_value: "NUMBER" .
#<ADDRESS> has_part: <UNIT> .
"""

house_tmplt="""
#<HOUSE> a house_number: .
#<HOUSE> has_value: "NUMBER" .
#<ADDRESS> has_part: <HOUSE> .
"""

street_tmplt="""
#<STREET> a street_name: .
#<STREET> has_value: "VALUE" .
#<ADDRESS> has_part: <STREET> .
"""

postalcode_tmplt="""
#<CODE> a postal_code: .
#<CODE> has_value: "VALUE" .
#<ADDRESS> has_part: <CODE> .
"""

places_tmplt="""
<IRI> a TEMPLATE: .
<IRI> has_label: "VALUE" .
<ADDRESS> is_about: <IRI> .
"""


'''
0 split_row	
1 bzk_field	
2 full_address	
3 UnitNumber	
4 HouseNumber	
5 StreetName	
6 Neighborhood	
7 City	
8 District	
8 Region	
9 State	
10 Country	
11 PostalCode
'''

'''
ApplicantBirthPlace
ApplicantCurrentAddress
VictimBirthPlace
VictimCurrentAddress
VictimDeathPlace
'''

with open('bzkopen-2026-04-17/bzkopen_addresses_validation.csv', newline='') as csvfile:
	reader = csv.reader(csvfile)
	next(reader, None) # skip header row

	for row in reader:
		if len(row)>0:  
			print ("#", row)

			# lets first collect all the info about the place 
			# (each row in the spreadsheed represents one place)
			placeIRI = niri()+"_place"

			# a place (which will be typed later to e.g. birthplace or deathplace) has an address
			address = row[2] # should not be empty
			addressIri = None
			if address:
				iri = placeIRI + "_address"
				cardiri = split_row_cases[split_row]["bzkcardiri"]
				addressRDF = address_tmplt.replace("ADDRESS", iri).replace("ADDRLABEL", address).replace("PLACE", placeIRI).replace("CARD", cardiri)
				addressIri = iri
				print (addressRDF)
				
			unit=row[3]
			if unit:
				unitIRI=addressIri+"_unit"
				unitRDF = unit_tmplt.replace("UNIT", unitIRI).replace("ADDRESS", addressIri).replace("NUMBER",unit)
				print (unitRDF)

			house=row[4]
			if house:
				houseIRI=addressIri+"_house"
				houseRDF = house_tmplt.replace("HOUSE", houseIRI).replace("ADDRESS", addressIri).replace("NUMBER",house)
				print (houseRDF)

			street=row[5]
			if street:
				streetIRI=addressIri+"_street"
				streetRDF = street_tmplt.replace("STREET", streetIRI).replace("ADDRESS", addressIri).replace("VALUE",street)
				print (streetRDF)

			postalcode=row[12]
			if postalcode:
				codeIRI=addressIri+"_code"
				codeRDF = postalcode_tmplt.replace("CODE", codeIRI).replace("ADDRESS", addressIri).replace("VALUE",postalcode)
				print (codeRDF)

			for t in "neighborhood_6 city_7	district_8 region_9	state_10 country_11".split():
				label=t.split("_")[0]
				key=int(t.split("_")[1])

				iri=addressIri+"_"+label
				value=row[key]
				if value:
					rdf=places_tmplt.replace("TEMPLATE", label).replace("IRI", iri).replace("ADDRESS", addressIri).replace("VALUE", value)
					print (rdf)

			split_row = row[0]
			caseIRI=split_row_cases[split_row]

			# this field tells us the kind of place, and to whom it relates
			field=row[1]

			if field=="ApplicantBirthPlace":
				applicantIRI=split_row_cases[split_row]["applicant"]
				birth=split_row_cases[split_row]["applicant_birth"]
				birthRDF=split_row_cases[split_row]["applicant_birth_rdf"]
				if birth:
					print(birthRDF)
					print(f"<{birth}> occurs_in: <{placeIRI}> . ")
					print(f"<{applicantIRI}> located_in: <{placeIRI}> .")
					
			if field=="ApplicantCurrentAddress":
				person=split_row_cases[split_row]["applicant"]
				if person:
					print(f"<{addressIri}> is_about: <{person}> .")

			if field=="VictimBirthPlace":
				if "persecutee_birth" in split_row_cases[split_row].keys():
					victimIRI=split_row_cases[split_row]["persecutee"]
					birth=split_row_cases[split_row]["persecutee_birth"]
					birthRDF=split_row_cases[split_row]["persecutee_birth_rdf"]
					if birth:
						print(birthRDF)
						print(f"<{birth}> occurs_in: <{placeIRI}> .")
						print(f"<{victimIRI}> located_in: <{placeIRI}> .")
					
			if field=="VictimCurrentAddress":
				person=split_row_cases[split_row]["persecutee"]
				if person:
					print(f"<{addressIri}> is_about: <{person}> .")
					print(f"<{addressIri}> a last_residential_address: .")
					

			if field=="VictimDeathPlace":
				if "persecutee_death" in split_row_cases[split_row].keys():
					victimIRI=split_row_cases[split_row]["persecutee"]
					death=split_row_cases[split_row]["persecutee_death"]
					deathRDF=split_row_cases[split_row]["persecutee_death_rdf"]
					if death:
						print(deathRDF)
						print(f"<{death}> occurs_in: <{placeIRI}> .")
						print(f"<{victimIRI}> located_in: <{placeIRI}> .")
					

















