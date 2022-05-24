import csv
import uuid
my_data_org_raw = './dev/my-data-org-source-data.csv'

##############################
# Mappings
##############################


def pds_email(person, email):
    try:
        if email != "":
            email_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:uses cco:EmailBox_{email_uuid} .

            cco:EmailBox_{email_uuid} a cco:EmailBox ; 
                obo:RO_0000056 cco:StasisOfTelecommunicationEndpointAssignment_{email_uuid} .
            
            cco:StasisOfTelecommunicationEndpointAssignment_{email_uuid} a cco:StasisOfTelecommunicationEndpointAssignment ;
                obo:RO_0000057 cco:TelecommunicationEndpoint_{email_uuid} . 

            cco:TelecommunicationEndpoint_{email_uuid} a cco:TelecommunicationEndpoint;
                cco:designated_by cco:EmailAddress_{email_uuid} . 

            cco:EmailAddress_{email_uuid} a cco:EmailAddress ;
                obo:RO_0010001 cco:InformationBearingEntity_EmailAddress_{email_uuid} . 
            
            cco:InformationBearingEntity_EmailAddress_{email_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{email}".
        
            """
            return triples
    except:
        print("Unable to Mapping Email")


##############################
# Ingress Data
##############################

def my_data_org_transformations():
    try:
        with open(my_data_org_raw, newline='') as csvfile:
            pds_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            header = next(pds_reader)
            # Creates a unique ID for a Person
            person_uuid = "cco:Person_" + str(uuid.uuid4())
            for row in pds_reader:
                firstname = row[0]
                lastname = row[1]
                birthdate = row[2]
                mailingstreet = row[3]
                mailingcity = row[4]
                mailingstate = row[5]
                mailingcountry = row[6]
                mailingpostcode = row[7]
                email = row[8]
                mobilephonenumber = row[8]
                homephonenumber = row[9]
                employeetitle = row[10]
                employername = row[11]
                employerindustry = row[12]
                employerstreet = row[13]
                employercity = row[14]
                employerstate = row[15]
                employerpostcode = row[16]
                employercountry = row[17]
                employeremail = row[18]
                employerphone = row[19]
                employerfax = row[20]

                print(pds_email(person_uuid, email))

    except Exception as e:
        print(e)


my_data_org_transformations()
