# -----------------------------------------------------------------------------
# Description: Data model for NPI physician data
# Author: Srivatsava
# Date: 25-06-2017
#------------------------------------------------------------------------------

from mongoengine import *


class HealthcareProvider(EmbeddedDocument):
	Healthcare_Provider_Taxonomy_Code = StringField(db_field = 'n47_1', default=None)
	Provider_License_Number = StringField(db_field = 'n47_2', default=None)
	Provider_License_Number_State_Code = StringField(db_field = 'n47_3', default=None)
	Healthcare_Provider_Primary_Taxonomy_Switch = StringField(db_field = 'n47_4', default=None)
	
	def UpdateHealthcare(self,l):
		if l[0]:
			self.Healthcare_Provider_Taxonomy_Code = l[0] or None
			self.Provider_License_Number = l[1] or None
			self.Provider_License_Number_State_Code = l[2] or None
			self.Healthcare_Provider_Primary_Taxonomy_Switch = l[3] or None
#------------------------------------------------------------------------------
	
class OtherProviderIdentifier(EmbeddedDocument):
	Other_Provider_Identifier = StringField(db_field = 'n48_1', default=None)
	Other_Provider_Identifier_Type_Code = StringField(db_field = 'n48_2', default=None)
	Other_Provider_Identifier_State = StringField(db_field = 'n48_3', default=None)
	Other_Provider_Identifier_Issuer = StringField(db_field = 'n48_4', default=None)
	
	def UpdateOtherprovider(self,l):
		self.Other_Provider_Identifier = l[0] or None
		self.Other_Provider_Identifier_Type_Code = l[1] or None
		self.Other_Provider_Identifier_State = l[2] or None
		self.Other_Provider_Identifier_Issuer = l[3] or None
#------------------------------------------------------------------------------
	
class Physician(Document):
	NPI = StringField(unique=True, required = True)
	Entity_Type_Code = StringField(db_field = 'n1', default=None)
	Replacement_NPI = StringField(db_field = 'n2', default=None)
	Employer_Identification_Number = StringField(db_field = 'n3', default=None)
	Provider_Organization_Name = StringField(db_field = 'n4', default=None)
	Provider_Last_Name = StringField(db_field = 'n5', default=None)
	Provider_First_Name = StringField(db_field = 'n6', default=None)
	Provider_Middle_Name = StringField(db_field = 'n7', default=None)
	Provider_Name_Prefix_Text = StringField(db_field = 'n8', default=None)
	Provider_Name_Suffix_Text = StringField(db_field = 'n9', default=None)
	Provider_Credential_Text = StringField(db_field = 'n10', default=None)
	Provider_Other_Organization_Name = StringField(db_field = 'n11', default=None)
	Provider_Other_Organization_Name_Type_Code = StringField(db_field = 'n12', default=None)
	Provider_Other_Last_Name = StringField(db_field = 'n13', default=None)
	Provider_Other_First_Name = StringField(db_field = 'n14', default=None)
	Provider_Other_Middle_Name = StringField(db_field = 'n15', default=None)
	Provider_Other_Name_Prefix_Text = StringField(db_field = 'n16', default=None)
	Provider_Other_Name_Suffix_Text = StringField(db_field = 'n17', default=None)
	Provider_Other_Credential_Text = StringField(db_field = 'n18', default=None)
	Provider_Other_Last_Name_Type_Code = StringField(db_field = 'n19', default=None)
	Provider_First_Line_Business_Mailing_Address = StringField(db_field = 'n20', default=None)
	Provider_Second_Line_Business_Mailing_Address = StringField(db_field = 'n21', default=None)
	Provider_Business_Mailing_Address_City_Name = StringField(db_field = 'n22', default=None)
	Provider_Business_Mailing_Address_State_Name = StringField(db_field = 'n23', default=None)
	Provider_Business_Mailing_Address_Postal_Code = StringField(db_field = 'n24', default=None)
	Provider_Business_Mailing_Address_Country_Code = StringField(db_field = 'n25', default=None)
	Provider_Business_Mailing_Address_Telephone_Number = StringField(db_field = 'n26', default=None)
	Provider_Business_Mailing_Address_Fax_Number = StringField(db_field = 'n27', default=None)
	Provider_First_Line_Business_Practice_Location_Address = StringField(db_field = 'n28', default=None)
	Provider_Second_Line_Business_Practice_Location_Address = StringField(db_field = 'n29', default=None)
	Provider_Business_Practice_Location_Address_City_Name = StringField(db_field = 'n30', default=None)
	Provider_Business_Practice_Location_Address_State_Name = StringField(db_field = 'n31', default=None)
	Provider_Business_Practice_Location_Address_Postal_Code = StringField(db_field = 'n32', default=None)
	Provider_Business_Practice_Location_Address_Country_Code = StringField(db_field = 'n33', default=None)
	Provider_Business_Practice_Location_Address_Telephone_Number = StringField(db_field = 'n34', default=None)
	Provider_Business_Practice_Location_Address_Fax_Number = StringField(db_field = 'n35', default=None)
	Provider_Enumeration_Date = StringField(db_field = 'n36', default=None)
	Last_Update_Date = StringField(db_field = 'n37', default=None)
	NPI_Deactivation_Reason_Code = StringField(db_field = 'n38', default=None)
	NPI_Deactivation_Date = StringField(db_field = 'n39', default=None)
	NPI_Reactivation_Date = StringField(db_field = 'n40', default=None)
	Provider_Gender_Code = StringField(db_field = 'n41', default=None)
	Authorized_Official_Last_Name = StringField(db_field = 'n42', default=None)
	Authorized_Official_First_Name = StringField(db_field = 'n43', default=None)
	Authorized_Official_Middle_Name = StringField(db_field = 'n44', default=None)
	Authorized_Official_Title_or_Position = StringField(db_field = 'n45', default=None)
	Authorized_Official_Telephone_Number = StringField(db_field = 'n46', default=None)
	Healthcare_Provider = ListField(EmbeddedDocumentField(HealthcareProvider))
	Other_Provider_Identifier = ListField(EmbeddedDocumentField(OtherProviderIdentifier))
	Is_Sole_Proprietor = StringField(db_field = 'n49', default=None)
	Is_Organization_Subpart = StringField(db_field = 'n50', default=None)
	Parent_Organization_LBN = StringField(db_field = 'n51', default=None)
	Parent_Organization_TIN = StringField(db_field = 'n52', default=None)
	Authorized_Official_Name_Prefix_Text = StringField(db_field = 'n53', default=None)
	Authorized_Official_Name_Suffix_Text = StringField(db_field = 'n54', default=None)
	Authorized_Official_Credential_Text = StringField(db_field = 'n55', default=None)
	Healthcare_Provider_Taxonomy_Group = ListField(StringField(db_field = 'n56'), default=None)
	meta = {
			'collection': 'physician',
			'indexes': ['Entity_Type_Code', 'Provider_Last_Name', 'Provider_Business_Mailing_Address_Postal_Code']}

	def UpdateUsingDict(self,Phydict):
		self.NPI = Phydict[0]     
		self.Entity_Type_Code = Phydict[1] or None
		self.Replacement_NPI = Phydict[2] or None
		self.Employer_Identification_Number = Phydict[3] or None 
		self.Provider_Organization_Name = Phydict[4] or None
		self.Provider_Last_Name = Phydict[5] or None
		self.Provider_First_Name = Phydict[6] or None
		self.Provider_Middle_Name = Phydict[7] or None
		self.Provider_Name_Prefix_Text = Phydict[8] or None
		self.Provider_Name_Suffix_Text = Phydict[9] or None
		self.Provider_Credential_Text = Phydict[10] or None
		self.Provider_Other_Organization_Name = Phydict[11] or None
		self.Provider_Other_Organization_Name_Type_Code = Phydict[12] or None
		self.Provider_Other_Last_Name = Phydict[13] or None
		self.Provider_Other_First_Name = Phydict[14] or None
		self.Provider_Other_Middle_Name = Phydict[15] or None
		self.Provider_Other_Name_Prefix_Text = Phydict[16] or None
		self.Provider_Other_Name_Suffix_Text = Phydict[17] or None
		self.Provider_Other_Credential_Text = Phydict[18] or None
		self.Provider_Other_Last_Name_Type_Code = Phydict[19] or None
		self.Provider_First_Line_Business_Mailing_Address = Phydict[20] or None
		self.Provider_Second_Line_Business_Mailing_Address = Phydict[21] or None
		self.Provider_Business_Mailing_Address_City_Name = Phydict[22] or None
		self.Provider_Business_Mailing_Address_State_Name = Phydict[23] or None
		self.Provider_Business_Mailing_Address_Postal_Code = Phydict[24] or None
		self.Provider_Business_Mailing_Address_Country_Code = Phydict[25] or None
		self.Provider_Business_Mailing_Address_Telephone_Number = Phydict[26] or None
		self.Provider_Business_Mailing_Address_Fax_Number = Phydict[27] or None
		self.Provider_First_Line_Business_Practice_Location_Address = Phydict[28] or None
		self.Provider_Second_Line_Business_Practice_Location_Address = Phydict[29] or None
		self.Provider_Business_Practice_Location_Address_City_Name = Phydict[30] or None
		self.Provider_Business_Practice_Location_Address_State_Name = Phydict[31] or None
		self.Provider_Business_Practice_Location_Address_Postal_Code = Phydict[32] or None
		self.Provider_Business_Practice_Location_Address_Country_Code = Phydict[33] or None
		self.Provider_Business_Practice_Location_Address_Telephone_Number = Phydict[34] or None
		self.Provider_Business_Practice_Location_Address_Fax_Number = Phydict[35] or None
		self.Provider_Enumeration_Date = Phydict[36] or None
		self.Last_Update_Date = Phydict[37] or None
		self.NPI_Deactivation_Reason_Code = Phydict[38] or None
		self.NPI_Deactivation_Date = Phydict[39] or None
		self.NPI_Reactivation_Date = Phydict[40] or None
		self.Provider_Gender_Code = Phydict[41] or None
		self.Authorized_Official_Last_Name = Phydict[42] or None
		self.Authorized_Official_First_Name = Phydict[43] or None
		self.Authorized_Official_Middle_Name = Phydict[44] or None
		self.Authorized_Official_Title_or_Position = Phydict[45] or None
		self.Authorized_Official_Telephone_Number = Phydict[46] or None
		for i in range(47,107,4):
			if Phydict[i]:
				healthcare = HealthcareProvider()
				l=[Phydict[i],Phydict[i+1],Phydict[i+2],Phydict[i+3]]
				healthcare.UpdateHealthcare(l)
				self.Healthcare_Provider.append(healthcare)
		for i in range(107,307,4):
			if Phydict[i]:
				other_provider = OtherProviderIdentifier()
				l=[Phydict[i],Phydict[i+1],Phydict[i+2],Phydict[i+3]]
				other_provider.UpdateOtherprovider(l)
				self.Other_Provider_Identifier.append(other_provider)
		self.Is_Sole_Proprietor = Phydict[307] or None
		self.Is_Organization_Subpart = Phydict[308] or None
		self.Parent_Organization_LBN = Phydict[309] or None
		self.Parent_Organization_TIN = Phydict[310] or None
		self.Authorized_Official_Name_Prefix_Text = Phydict[311] or None
		self.Authorized_Official_Name_Suffix_Text = Phydict[312] or None
		self.Authorized_Official_Credential_Text = Phydict[313] or None
		for i in range(314,329):
			if Phydict[i]:
				if self.Healthcare_Provider_Taxonomy_Group == None:
					self.Healthcare_Provider_Taxonomy_Group = []
					
				self.Healthcare_Provider_Taxonomy_Group.append(Phydict[i])
#------------------------------------------------------------------------------