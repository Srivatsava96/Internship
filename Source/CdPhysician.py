from mongoengine import *

class HealthcareProvider(EmbeddedDocument):
	Healthcare_Provider_Taxonomy_Code = StringField()
	Provider_License_Number = StringField()
	Provider_License_Number_State_Code = StringField()
	Healthcare_Provider_Primary_Taxonomy_Switch = StringField()
	def UpdateHealthcare(self,l):
		self.Healthcare_Provider_Taxonomy_Code = l[0]
		self.Provider_License_Number = l[1]
		self.Provider_License_Number_State_Code = l[2]
		self.Healthcare_Provider_Primary_Taxonomy_Switch = l[3]	
	
class OtherProviderIdentifier(EmbeddedDocument):
	Other_Provider_Identifier = StringField()
	Other_Provider_Identifier_Type_Code = StringField()
	Other_Provider_Identifier_State = StringField()
	Other_Provider_Identifier_Issuer = StringField()
	def UpdateOtherprovider(self,l):
		self.Other_Provider_Identifier = l[0]
		self.Other_Provider_Identifier_Type_Code = l[1]
		self.Other_Provider_Identifier_State = l[2]
		self.Other_Provider_Identifier_Issuer = l[3]
	
class Physician(Document):
	NPI = StringField(unique=True)
	Entity_Type_Code = StringField()
	Replacement_NPI = StringField()
	Employer_Identification_Number = StringField()
	Provider_Organization_Name = StringField()
	Provider_Last_Name = StringField()
	Provider_First_Name = StringField()
	Provider_Middle_Name = StringField()
	Provider_Name_Prefix_Text = StringField()
	Provider_Name_Suffix_Text = StringField()
	Provider_Credential_Text = StringField()
	Provider_Other_Organization_Name = StringField()
	Provider_Other_Organization_Name_Type_Code = StringField()
	Provider_Other_Last_Name = StringField()
	Provider_Other_First_Name = StringField()
	Provider_Other_Middle_Name = StringField()
	Provider_Other_Name_Prefix_Text = StringField()
	Provider_Other_Name_Suffix_Text = StringField()
	Provider_Other_Credential_Text = StringField()
	Provider_Other_Last_Name_Type_Code = StringField()
	Provider_First_Line_Business_Mailing_Address = StringField()
	Provider_Second_Line_Business_Mailing_Address = StringField()
	Provider_Business_Mailing_Address_City_Name = StringField()
	Provider_Business_Mailing_Address_State_Name = StringField()
	Provider_Business_Mailing_Address_Postal_Code = StringField()
	Provider_Business_Mailing_Address_Country_Code = StringField()
	Provider_Business_Mailing_Address_Telephone_Number = StringField()
	Provider_Business_Mailing_Address_Fax_Number = StringField()
	Provider_First_Line_Business_Practice_Location_Address = StringField()
	Provider_Second_Line_Business_Practice_Location_Address = StringField()
	Provider_Business_Practice_Location_Address_City_Name = StringField()
	Provider_Business_Practice_Location_Address_State_Name = StringField()
	Provider_Business_Practice_Location_Address_Postal_Code = StringField()
	Provider_Business_Practice_Location_Address_Country_Code = StringField()
	Provider_Business_Practice_Location_Address_Telephone_Number = StringField()
	Provider_Business_Practice_Location_Address_Fax_Number = StringField()
	Provider_Enumeration_Date = StringField()
	Last_Update_Date = StringField()
	NPI_Deactivation_Reason_Code = StringField()
	NPI_Deactivation_Date = StringField()
	NPI_Reactivation_Date = StringField()
	Provider_Gender_Code = StringField()
	Authorized_Official_Last_Name = StringField()
	Authorized_Official_First_Name = StringField()
	Authorized_Official_Middle_Name = StringField()
	Authorized_Official_Title_or_Position = StringField()
	Authorized_Official_Telephone_Number = StringField()
	Healthcare_Provider = ListField(EmbeddedDocumentField(HealthcareProvider))
	Other_Provider_Identifier = ListField(EmbeddedDocumentField(OtherProviderIdentifier))
	Is_Sole_Proprietor = StringField()
	Is_Organization_Subpart = StringField()
	Parent_Organization_LBN = StringField()
	Parent_Organization_TIN = StringField()
	Authorized_Official_Name_Prefix_Text = StringField()
	Authorized_Official_Name_Suffix_Text = StringField()
	Authorized_Official_Credential_Text = StringField()
	Healthcare_Provider_Taxonomy_Group = ListField(StringField())

	def UpdateUsingDict(self,Phydict):
		self.NPI                                                          = Phydict[0]     
		self.Entity_Type_Code                                             = Phydict[1]
		self.Replacement_NPI                                              = Phydict[2]
		self.Employer_Identification_Number                               = Phydict[3]
		self.Provider_Organization_Name                                   = Phydict[4]
		self.Provider_Last_Name                                           = Phydict[5]
		self.Provider_First_Name                                          = Phydict[6]
		self.Provider_Middle_Name                                         = Phydict[7]
		self.Provider_Name_Prefix_Text                                    = Phydict[8]
		self.Provider_Name_Suffix_Text                                    = Phydict[9]
		self.Provider_Credential_Text                                     = Phydict[10]
		self.Provider_Other_Organization_Name                             = Phydict[11]
		self.Provider_Other_Organization_Name_Type_Code                   = Phydict[12]
		self.Provider_Other_Last_Name                                     = Phydict[13]
		self.Provider_Other_First_Name                                    = Phydict[14]
		self.Provider_Other_Middle_Name                                   = Phydict[15]
		self.Provider_Other_Name_Prefix_Text                              = Phydict[16]
		self.Provider_Other_Name_Suffix_Text                              = Phydict[17]
		self.Provider_Other_Credential_Text                               = Phydict[18]
		self.Provider_Other_Last_Name_Type_Code                           = Phydict[19]
		self.Provider_First_Line_Business_Mailing_Address                 = Phydict[20]
		self.Provider_Second_Line_Business_Mailing_Address                = Phydict[21]
		self.Provider_Business_Mailing_Address_City_Name                  = Phydict[22]
		self.Provider_Business_Mailing_Address_State_Name                 = Phydict[23]
		self.Provider_Business_Mailing_Address_Postal_Code                = Phydict[24]
		self.Provider_Business_Mailing_Address_Country_Code               = Phydict[25]
		self.Provider_Business_Mailing_Address_Telephone_Number           = Phydict[26]
		self.Provider_Business_Mailing_Address_Fax_Number                 = Phydict[27]
		self.Provider_First_Line_Business_Practice_Location_Address       = Phydict[28]
		self.Provider_Second_Line_Business_Practice_Location_Address      = Phydict[29]
		self.Provider_Business_Practice_Location_Address_City_Name        = Phydict[30]
		self.Provider_Business_Practice_Location_Address_State_Name       = Phydict[31]
		self.Provider_Business_Practice_Location_Address_Postal_Code      = Phydict[32]
		self.Provider_Business_Practice_Location_Address_Country_Code     = Phydict[33]
		self.Provider_Business_Practice_Location_Address_Telephone_Number = Phydict[34]
		self.Provider_Business_Practice_Location_Address_Fax_Number       = Phydict[35]
		self.Provider_Enumeration_Date                                    = Phydict[36]
		self.Last_Update_Date                                             = Phydict[37]
		self.NPI_Deactivation_Reason_Code                                 = Phydict[38]
		self.NPI_Deactivation_Date                                        = Phydict[39]
		self.NPI_Reactivation_Date                                        = Phydict[40]
		self.Provider_Gender_Code                                         = Phydict[41]
		self.Authorized_Official_Last_Name                                = Phydict[42]
		self.Authorized_Official_First_Name                               = Phydict[43]
		self.Authorized_Official_Middle_Name                              = Phydict[44]
		self.Authorized_Official_Title_or_Position                        = Phydict[45]
		self.Authorized_Official_Telephone_Number                         = Phydict[46]
		for i in range(47,107,4):
			healthcare = HealthcareProvider()
			l=[Phydict[i],Phydict[i+1],Phydict[i+2],Phydict[i+3]]
			healthcare.UpdateHealthcare(l)
			self.Healthcare_Provider.append(healthcare)
		for i in range(107,307,4):
			other_provider = OtherProviderIdentifier()
			l=[Phydict[i],Phydict[i+1],Phydict[i+2],Phydict[i+3]]
			other_provider.UpdateOtherprovider(l)
			self.Other_Provider_Identifier.append(other_provider)
		self.Is_Sole_Proprietor                                           = Phydict[307]
		self.Is_Organization_Subpart                                      = Phydict[308]
		self.Parent_Organization_LBN                                      = Phydict[309]
		self.Parent_Organization_TIN                                      = Phydict[310]
		self.Authorized_Official_Name_Prefix_Text                         = Phydict[311]
		self.Authorized_Official_Name_Suffix_Text                         = Phydict[312]
		self.Authorized_Official_Credential_Text                          = Phydict[313]
		for i in range(314,329):
			self.Healthcare_Provider_Taxonomy_Group.append(Phydict[i])