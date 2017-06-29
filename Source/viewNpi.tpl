<!DOCTYPE html>

<html>
<body bgcolor= "#E6E6FA">
<head>
	<title>View by Npi</title>
</head>

<body>
	<h1 align ="center"><font color = "navy">NPI Number Lookup</font></h1>
	<h2 align ="center"><font color = "red">Search Result</font></h2>
	<br>
	<center>
	<table border = 1>
	<tr>
	<td>Name:</td> <td>{{phy['Provider_Name_Prefix_Text']}} {{phy['Provider_First_Name']}} {{phy['Provider_Middle_Name']}} {{phy['Provider_Last_Name']}} {{phy['Provider_Credential_Text']}}</td><br>
	</tr>
	<tr>
	<td>ZIP:</td><td>{{phy['Provider_Business_Mailing_Address_Postal_Code']}}</td><br>
	</tr>
	<tr>
	<td>State Code:</td><td>{{phy['Provider_Business_Mailing_Address_State_Name']}}</td><br>
	</tr>
	<tr>
	<td>Speciality:</td><td>{{phy['Healthcare_Provider']}}</td><br>
	</tr>
	<tr>
	<td>Organization:</td><br>
	</tr>
	<tr> 
	<td>NPI :</td> <td>{{phy['NPI']}}</td><br>
	</tr>
	<br>
	</center>
</body>

</html>