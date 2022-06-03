import csv
import uuid
my_data_org_raw = './dev/my-data-org-source-data.csv'

##############################
# Mappings
# Note: Each Function creates triples independently from the source data
##############################


def pds_firstname(person, firstname):
    try:
        if firstname != "":
            firstname_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:designated_by cco:PersonGivenName_{firstname_uuid} . 

            cco:PersonGivenName_{firstname_uuid} a cco:PersonGivenName ;
                obo:RO_0010001 cco:InformationBearingEntity_PersonGivenName_{firstname_uuid} . 
            
            cco:InformationBearingEntity_PersonGivenName_{firstname_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{firstname}".
            """
            return triples
    except Exception as e:
        print("FirstName:" + e)


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
    except Exception as e:
        print("Email:" + e)

        

##############################
# Mapping data      (Order)  
##############################
        
def pds_lastname(person, lastname):
    try:
        if lastname != "":
            lastname_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:designated_by cco:PersonFamilyName_{lastname_uuid} . 

            cco:PersonFamilyName_{lastname_uuid} a cco:PersonFamilyName ;
                obo:RO_0010001 cco:InformationBearingEntity_PersonFamilyName_{lastname_uuid} . 
            
            cco:InformationBearingEntity_PersonFamilyName_{lastname_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{lastname}".
            """
            return triples
    except Exception as e:
        print("Lastname:" + e)        

        
def pds_birthday(person, birthday):
    try:
        if birthday != "":
            birthday_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:is_object_of cco:Birth_{birthday_uuid} . 

            cco:Birth_{birthday_uuid} a cco:Birth ;
                cco:occurs_on cco:Day_{birthday_uuid} . 
                
            cco:Day_{birthday_uuid} a cco:Day ;
                cco:designated_by cco:DateIdentifier_{birthday_uuid} .
                
            cco:DateIdentifier_{birthday_uuid} a cco:DateIdentifier ;
                obo:RO_0010001 cco:InformationBearingEntity_DataIdentifier_{birthday_uuid} .
                
            cco:InformationBearingEntity_DateIdentifier_{birthday_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{birthday}".
            """
            return triples
    except Exception as e:
        print("Birthday:" + e)           
        
        
         
def pds_mailingstreet(person, mailingstreet):
    try:
        if mailingstreet != "":
            mailingstreet_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:agent_in cco:ActOfResiding_{mailingstreet_uuid} . 

            cco:ActOfResiding_{mailingstreet_uuid} a cco:ActOfResiding ;
                obo:RO_0000057 cco:ResidentialFacility_{mailingstreet_uuid} . 
                
            cco:ResidentialFacility_{mailingstreet_uuid} a cco:ResidentialFacility ;
                cco:designated_by cco:StreetAdress_{mailingstreet_uuid} .
                
            cco:StreetAdress_{mailingstreet_uuid} a cco:StreetAdress ;
                obo:RO_0010001 cco:InformationBearingEntity_StreetAdress_{mailingstreet_uuid} .
                
            cco:InformationBearingEntity_StreetAdress_{mailingstreet_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{mailingstreet}".
            """
            return triples
    except Exception as e:
        print("Mailingstreet:" + e)      
        
        
def pds_mailingcity(person, mailingcity):
    try:
        if mailingcity != "":
            mailingcity_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:agent_in cco:ActOfResiding_{mailingcity_uuid} . 

            cco:ActOfResiding_{mailingcity_uuid} a cco:ActOfResiding ;
                obo:RO_0000057 cco:ResidentialFacility_{mailingcity_uuid} . 
                
            cco:ResidentialFacility_{mailingcity_uuid} a cco:ResidentialFacility ;
                obo:RO_0001025 cco:LocalAdministrativeRegion_{mailingcity_uuid} .
                
           cco:LocalAdministrativeRegion_{mailingcity_uuid} a cco:LocalAdministrativeRegion ;
               cco:designated_by cco:DesignativeName_{mailingcity_uuid} .
               
            cco:DesignativeName_{mailingcity_uuid} a cco:DesignativeName ;
                obo:RO_0010001 cco:InformationBearingEntity_DesignativeName_{mailingcity_uuid} .
                
            cco:InformationBearingEntity_DesignativeName_{mailingcity_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{mailingcity}".
            """
            return triples
    except Exception as e:
        print("Mailingcity:" + e)   
        

def pds_mailingstate(person, mailingstate):
    try:
        if mailingstate != "":
            mailingstate_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:agent_in cco:ActOfResiding_{mailingstate_uuid} . 

            cco:ActOfResiding_{mailingstate_uuid} a cco:ActOfResiding ;
                obo:RO_0000057 cco:ResidentialFacility_{mailingstate_uuid} . 
                
            cco:ResidentialFacility_{mailingstate_uuid} a cco:ResidentialFacility ;
                obo:RO_0001025 cco:LocalAdministrativeRegion_{mailingstate_uuid} .
                
            cco:LocalAdministrativeRegion_{mailingstate_uuid} a cco:LocalAdministrativeRegion ;
               obo:BFO_0000050 cco:FirstOrderAdministrativeRegion_{mailingstate_uuid} .
               
            cco:FirstOrderAdministrativeRegion_{mailingstate_uuid} a cco:FirstOrderAdministrativeRegion ;
                cco:designated_by cco:DesignativeName_{mailingstate_uuid} .
                
            cco:DesignativeName_{mailingstate_uuid} a cco:DesignativeName ;
                obo:RO_0010001 cco:InformationBearingEntity_DesignativeName_{mailingstate_uuid} .
                
            cco:InformationBearingEntity_DesignativeName_{mailingstate_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{mailingstate}".
            """
            return triples
    except Exception as e:
        print("Mailingstate:" + e)         
        
        
def pds_mailingpostcode(person, mailingpostcode):
    try:
        if mailingpostcode != "":
            mailingpostcode_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:agent_in cco:ActOfResiding_{mailingpostcode_uuid} . 

            cco:ActOfResiding_{mailingpostcode_uuid} a cco:ActOfResiding ;
                obo:RO_0000057 cco:ResidentialFacility_{mailingpostcode_uuid} . 
                
            cco:ResidentialFacility_{mailingpostcode_uuid} a cco:ResidentialFacility ;
                obo:RO_0001025 cco:PostalZone_{mailingpostcode_uuid} .
                
           cco:PostalZone_{mailingpostcode_uuid} a cco:PostalZone ;
               cco:designated_by cco:PostalCode_{mailingpostcode_uuid} .
               
            cco:PostalCode_{mailingpostcode_uuid} a cco:PostalCode ;
                obo:RO_0010001 cco:InformationBearingEntity_PostalCode_{mailingpostcode_uuid} .
                
            cco:InformationBearingEntity_PostalCode_{mailingpostcode_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{mailingpostcode}".
            """
            return triples
    except Exception as e:
        print("Mailing postal code:" + e)    
        
        
def pds_mailingcountry(person, mailingcountry):
    try:
        if mailingcountry != "":
            mailingcountry_uuid = uuid.uuid4()
            mailingstate_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:agent_in cco:ActOfResiding_{ mailingcountry_uuid} . 

            cco:ActOfResiding_{ mailingcountry_uuid} a cco:ActOfResiding ;
                obo:RO_0000057 cco:ResidentialFacility_{ mailingcountry_uuid} . 
                
            cco:ResidentialFacility_{ mailingcountry_uuid} a cco:ResidentialFacility ;
                obo:RO_0001025 cco:LocalAdministrativeRegion_{ mailingcountry_uuid} .
                
            cco:LocalAdministrativeRegion_{mailingstate_uuid} a cco:LocalAdministrativeRegion ;
               obo:BFO_0000050 cco:FirstOrderAdministrativeRegion_{ mailingcountry_uuid} .
               
            cco:FirstOrderAdministrativeRegion_{mailingstate_uuid} a cco:FirstOrderAdministrativeRegion ;
                obo:BFO_0000050 cco:County_{mailingcountry_uuid} .
                
            cco:Country_{mailingcountry_uuid} a cco:Country ;
               cco:designated_by cco:PostalCodeDesignativeName_{mailingcountry_uuid} .
               
            cco:DesignativeName_{mailingcountry_uuid} a cco:DesignativeName ;
                obo:RO_0010001 cco:InformationBearingEntity_DesignativeName_{mailingcountry_uuid} .
                
            cco:InformationBearingEntity_DesignativeName_{mailingcountry_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{mailingcountry}".
            """
            return triples
    except Exception as e:
        print("Mailingcountry:" + e)     
        
        
def pds_homephonenumber(person, homephonenumber):
    try:
        if homephonenumber != "":
            homephonenumber_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:user cco:LandlineTelephone_{homephonenumber_uuid} . 

            cco:LandlineTelephone_{homephonenumber_uuid} a cco:LandlineTelephone;
                obo:RO_0000056 cco:StasisOfTelecommunicationEndpointAssignment_{homephonenumber_uuid} . 
                
            cco:StasisOfTelecommunicationEndpointAssignment_{homephonenumber_uuid} a  cco:StasisOfTelecommunicationEndpointAssignment;
                obo:RO_0000057 cco:TelecommunicationEndpoint_{homephonenumber_uuid} .
                
            cco:TelecommunicationEndpoint_{homephonenumber_uuid} a cco:TelecommunicationEndpoint ;
               cco:designated_by cco:TelephoneNumber_{homephonenumber_uuid} .
               
            cco:TelephoneNumber_{homephonenumber_uuid} a cco:TelephoneNumber ;
                obo:RO_0010001 cco:InformationBearingEntity_TelephoneNumber_{homephonenumber_uuid} .
                
            cco:InformationBearingEntity_TelephoneNumber_{homephonenumber_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{homephonenumber}".
            """
            return triples
    except Exception as e:
        print("Home phone number:" + e)    
        

def pds_mobilephonenumber(person, mobilephonenumber):
    try:
        if mobilephonenumber != "":
            mobilephonenumber_uuid = uuid.uuid4()
            triples = f"""
            {person} cco:user cco:MobileTelephone_{mobilephonenumber_uuid} . 

            cco:MobileTelephone_{mobilephonenumber_uuid} a cco:MobileTelephone;
                obo:RO_0000056 cco:StasisOfTelecommunicationEndpointAssignment_{mobilephonenumber_uuid} . 
                
            cco:StasisOfTelecommunicationEndpointAssignment_{mobilephonenumber_uuid} a  cco:StasisOfTelecommunicationEndpointAssignment;
                obo:RO_0000057 cco:TelecommunicationEndpoint_{mobilephonenumber_uuid} .
                
            cco:TelecommunicationEndpoint_{mobilephonenumber_uuid} a cco:TelecommunicationEndpoint ;
               cco:designated_by cco:TelephoneNumber_{mobilephonenumber_uuid} .
               
            cco:TelephoneNumber_{mobilephonenumber_uuid} a cco:TelephoneNumber ;
                obo:RO_0010001 cco:InformationBearingEntity_TelephoneNumber_{mobilephonenumber_uuid} .
                
            cco:InformationBearingEntity_TelephoneNumber_{mobilephonenumber_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{mobilephonenumber}".
            """
            return triples
    except Exception as e:
        print("Mobile phone number:" + e)     
        

def pds_employername(person, employername):
    try:
        if employername != "":
            employername_uuid = uuid.uuid4()
            triples = f"""
            {person} obo:RO_0000053 cco:OccupationRole_{employername_uuid} . 

            cco:OccupationRole_{employername_uuid} a cco:OccupationRole;
                cco:has_organization_context cco:Organization_{employername_uuid} . 
                
            cco:Organization_{employername_uuid} a cco:Organization ;
                cco:designated_by cco:DesignativeName_{employername_uuid}
                
            cco:DesignativeName_{employername_uuid} a cco:DesignativeName ;
                obo:RO_0010001 cco:InformationBearingEntity_DesignativeName_{employername_uuid} .
                
            cco:InformationBearingEntity_DesignativeName_{employername_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{employername}".
            """
            return triples
    except Exception as e:
        print("Name of employeer" + e)  
        
        
def pds_employerindustry(organization, employerindustry):
    try:
        if employerindustry != "":
            employerindustry_uuid = uuid.uuid4()
            triples = f"""
            {organization} obo:RO_0000053 cco:Capability_{employerindustry_uuid} . 

            cco:Capability_{employerindustry_uuid} a cco:Capability;
                cco:is_measured_by_nominal cco:DescriptiveMeasurementContentEntity_{employerindustry_uuid}.
                
            cco:DescriptiveMeasurementContentEntity_{employerindustry_uuid} a cco:DescriptiveMeasurementContentEntity ;
                obo:RO_0010001 cco:InformationBearingEntity_DescriptiveMeasurementContentEntity_{employerindustry_uuid} .
                
            cco:InformationBearingEntity_DescriptiveMeasurementContentEntity_{employerindustry_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{employerindustry}".
            """
            return triples
    except Exception as e:
        print("Place of employeer industry" + e)  
    
    
def pds_employerstreet(organization, employerstreet):
    try:
        if employerstreet != "":
            employerstreet_uuid = uuid.uuid4()
            triples = f"""
            {organization} cco:agent_in cco:ActOfInhabitancy_{employerstreet_uuid} . 

            cco:ActOfInhabitancy_{employerstreet_uuid} a cco:ActOfInhabitancy;
                cco:has_object cco:Facility_{employerstreet_uuid}.
                
            cco:Facility_{employerstreet_uuid} a cco:Facility ;
                cco:designed_by cco:StreetAdress_{employerstreet_uuid} .
                
            cco:StreetAdress_{employerstreet_uuid} a cco:StreetAdress ;
                obo:RO_0010001 cco:InformationBearingEntity_StreetAdress_{employerstreet_uuid} .
                
            cco:InformationBearingEntity_StreetAdress_{employerstreet_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{employerstreet}".
            """
            return triples
    except Exception as e:
        print("Employeers address" + e) 
        
        
def pds_employercity(organization, employercity):
    try:
        if employercity != "":
            employercity_uuid = uuid.uuid4()
            triples = f"""
            {organization} cco:agent_in cco:ActOfInhabitancy_{employercity_uuid} . 

            cco:ActOfInhabitancy_{employercity_uuid} a cco:ActOfInhabitancy;
                cco:has_object cco:Facility_{employercity_uuid}.
                
            cco:Facility_{employercity_uuid} a cco:Facility ;
                obo:RO_0001025 cco:LocalAdministrativeRegion_{employercity_uuid} .
                
            cco:LocalAdministrativeRegion_{employercity_uuid} a cco:LocalAdministrativeRegion ;
                cco:designed_by cco:DesignativeName_{employercity_uuid}.
                
            cco:DesignativeName_{employercity_uuid} a cco:DesignativeName ;
                obo:RO_0010001 cco:InformationBearingEntity_DesignativeName_{employercity_uuid} .
                
            cco:InformationBearingEntity_DesignativeName_{employercity_uuid} a cco:InformationBearingEntity;
               cco:has_text_value "{employercity}".
            """
            return triples
    except Exception as e:
        print("Employeers city" + e)   
        
        
def pds_employerstate(organization, employerstate):
    try:
        if employerstate != "":
            employerstate_uuid = uuid.uuid4()
            triples = f"""
            {organization} cco:agent_in cco:ActOFInhabitancy_{employerstate_uuid} . 

             cco:ActOfInhabitancy_{employerstate_uuid} a cco:ActOfInhabitancy;
                cco:has_object cco:Facility_{employerstate_uuid}.
                
             cco:Facility_{employerstate_uuid} a cco:Facility ;
                obo:RO_0001025 cco:LocalAdministrativeRegion_{employerstate_uuid} .
                
             cco:LocalAdministrativeRegion_{employerstate_uuid} a cco:LocalAdministrativeRegion ;
               obo:BFO_0000050 cco:FirstOrderAdministrativeRegion_{employerstate_uuid} .
               
             cco:FirstOrderAdministrativeRegion_{employerstate_uuid} a cco:FirstOrderAdministrativeRegion ;
                cco:designated_by cco:DesignativeName_{employerstate_uuid} .
                
             cco:DesignativeName_{employerstate_uuid} a cco:DesignativeName ;
                obo:RO_0010001 cco:InformationBearingEntity_DesignativeName_{employerstate_uuid} .
                
            cco:InformationBearingEntity_DesignativeName_{employerstate_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{employerstate}".
            """
            return triples
    except Exception as e:
        print("Employeer state" + e)  
        
        
def pds_employerpostcode(organization, employerpostcode):
    try:
        if employerpostcode != "":
            employerpostcode_uuid = uuid.uuid4()
            triples = f"""
            {organization} cco:agent_in cco:ActOFInhabitancy_{employerpostcode_uuid} . 

             cco:ActOfInhabitancy_{employerpostcode_uuid} a cco:ActOfInhabitancy;
                cco:has_object cco:Facility_{employerpostcode_uuid}.
                
             cco:Facility_{employerpostcode_uuid} a cco:Facility ;
                obo:RO_0001025 cco:PostalZone_{employerpostcode_uuid} .
                
             cco:PostalZone_{employerpostcode_uuid} a cco:PostalZone;
               cco:designated_by cco:PostalCode_{employerpostcode_uuid} .
               
             cco:PostalCode_{employerpostcode_uuid} a cco:PostalCode;
                obo:RO_0010001 cco:InformationBearingEntity_PostalCode_{employerpostcode_uuid} .
                
             cco:InformationBearingEntity_PostalCode_{employerpostcode_uuid} a cco:InformationBearingEntity;
               cco:has_text_value "{employerpostcode_uuid}".
            """
            return triples
    except Exception as e:
        print("Employeer post code" + e)         
        
        
def pds_employercountry(organization, employercountry):
    try:
        if employercountry != "":
            employercountry_uuid = uuid.uuid4()
            triples = f"""
            {organization} cco:agent_in cco:ActOfInhabitancy_{employercountry_uuid} . 

            cco:ActOfInhebitancy_{employercountry_uuid} a cco:ActOfInhebitancy ;
                cco:has_object cco:Facility_{employercountry_uuid} . 
                
            cco:Facility_{employercountry_uuid} a cco:Facility ;
                obo:RO_0001025 cco:LocalAdministrativeRegion_{employercountry_uuid} .
                
            cco:LocalAdministrativeRegion_{employercountry_uuid} a cco:LocalAdministrativeRegion ;
               obo:BFO_0000050 cco:FirstOrderAdministrativeRegion_{employercountry_uuid} .
               
            cco:FirstOrderAdministrativeRegion_{employercountry_uuid} a cco:FirstOrderAdministrativeRegion ;
                obo:BFO_0000050 cco:County_{employercountry_uuid} .
                
            cco:Country_{employercountry_uuid} a cco:Country ;
               cco:designated_by cco:DesignativeName_{employercountry_uuid} .
               
            cco:DesignativeName_{employercountry_uuid} a cco:DesignativeName ;
                obo:RO_0010001 cco:InformationBearingEntity_DesignativeName_{employercountry_uuid} .
                
            cco:InformationBearingEntity_DesignativeName_{employercountry_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{employercountry}".
            """
            return triples
    except Exception as e:
        print("Employer country:" + e)
        
        
def pds_employerphone(organization, employerphone):
    try:
        if employerphone != "":
            employerphone_uuid = uuid.uuid4()
            triples = f"""
            {organization} cco:agent_in cco:ActOFOwnership_{employerphone_uuid} . 

             cco:ActOfOwnership_{employerphone_uuid} a cco:ActOfOwnership;
                cco:has_object cco:Telephone_{employerphone_uuid}.
                
            cco:Telephone_{employerphone_uuid} a cco:Telephone ;
                obo:RO_000056 cco:StasisOfTelecommunicayionEndpointAssignment_{employerphone_uuid} .
            
            cco:StasisOfTelecommunicayionEndpointAssignment_{employerphone_uuid} a cco:StasisOfTelecommunicayionEndpointAssignment ;
                obo:RO_0000057 cco:TelecommunicationEndpoint_{employerphone_uuid} .
                
            cco:TelecommunicationEndpoint_{employerphone_uuid} a cco:TelecommunicationEndpoint ;
                cco:designed_by cco:TelephoneNumber_{employerphone_uuid} .
                
            cco:TelephoneNumber_{employerphone_uuid} a cco:TelephoneNumber ;
                obo:RO_0010001 cco:InformationBearingEntity_TelephoneNumber_{employerphone_uuid} .
                
            cco:InformationBearingEntity_TelephoneNumber_{employerphone_uuid} a cco:InformationBearingEntity ; 
                cco:has_text_value "{employerphone}".
            """
            return triples
    except Exception as e:
        print("Employer phone number" + e) 
        
        
def pds_employerfax(organization, employerfax):
    try:
        if employerfax != "":
            employerfax_uuid = uuid.uuid4()
            triples = f"""
            {organization} cco:agent_in cco:ActOFOwnership_{employerfax_uuid} . 

             cco:ActOfOwnership_{employerfax_uuid} a cco:ActOfOwnership;
                cco:has_object cco:FacsimileMachine_{employerfax_uuid}.
                
             cco:FacsimileMachine_{employerfax_uuid} a cco:FacsimileMachine;
                obo:RO_000056 cco:StasisOfTelecommunicayionEndpointAssignment_{employerfax_uuid} .
                
            cco:StasisOfTelecommunicayionEndpointAssignment_{employerfax_uuid} a cco:StasisOfTelecommunicayionEndpointAssignment ;
                obo:RO_0000057 cco:TelecommunicationEndpoint_{employerfax_uuid} .
                
            cco:TelecommunicationEndpoint_{employerfax_uuid} a cco:TelecommunicationEndpoint ;
                cco:designed_by cco:FacsimileMachineNumber_{employerfax_uuid} .
                
            cco:FacsimileMachineNumber_{employerfax_uuid} a cco:FacsimileMachineNumber ;
                obo:RO_0010001 cco:InformationBearingEntity_FacsimileMachineNumber_{employerfax_uuid} .
                
            cco:InformationBearingEntity_FacsimileMachineNumber_{employerfax_uuid} a cco:InformationBearingEntity ; 
                cco:has_text_value "{employerfax}".
            """
            return triples
    except Exception as e:
        print("Employer fax:" + e)
        
        
def pds_employeetitle(person, employeetitle):
    try:
        if employeetitle != "":
            employeetitle_uuid = uuid.uuid4()
            triples = f"""
            {person} obo:RO_0000053 cco:OccupationRole_{employeetitle_uuid} . 

            cco:OccupationRole_{employeetitle_uuid} a cco:OccupationRole;
                cco:described_by cco:NominalMeasurementInformationContentEntity_{employeetitle_uuid} . 
                
            cco:NominalMeasurementInformationContentEntity_{employeetitle_uuid} a cco:NominalMeasurementInformationContentEntity;
                obo:RO_0010001 cco:InformationBearingEntity_NominalMeasurementInformationContentEntity_{employeetitle_uuid} .
                
            cco:InformationBearingEntity_NominalMeasurementInformationContentEntity_{employeetitle_uuid} a cco:InformationBearingEntity ;
               cco:has_text_value "{employeetitle}".
            """
            return triples
    except Exception as e:
        print("Employer role" + e)         
        
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
            organization_uuid = "cco:Organization_" + str(uuid.uuid4())
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
                print(pds_firstname(person_uuid, firstname))
                print(pds_lastname(person_uuid, lastname))
                print(pds_birthday(person_uuid, birthdate))
                print(pds_mailingstreet(person_uuid, mailingstreet))
                print(pds_mailingcity(person_uuid, mailingcity))
                print(pds_mailingstate(person_uuid, mailingstate))
                print(pds_mailingpostcode(person_uuid, mailingpostcode))
                print(pds_mailingcountry(person_uuid, mailingcountry))
                print(pds_homephonenumber(person_uuid, homephonenumber))
                print(pds_mobilephonenumber(person_uuid, mobilephonenumber))
                print(pds_employername(person_uuid, employername))
                print(pds_employeetitle(person_uuid, employeetitle))
                
                print(pds_employerindustry(organization_uuid, employerindustry))
                print(pds_employerstreet(organization_uuid, employerstreet))
                print(pds_employercity(organization_uuid, employercity))
                print(pds_employerstate(organization_uuid, employerstate))
                print(pds_employerpostcode(organization_uuid, employerpostcode))
                print(pds_employercountry(organization_uuid, employercountry))
                print(pds_employerphone(organization_uuid, employerphone))
                print(pds_employerfax(organization_uuid, employerfax))
                

    except Exception as e:
        print("Reading my data" + e)


my_data_org_transformations()
