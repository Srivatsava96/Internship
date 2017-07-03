<!DOCTYPE html>

<html>
<body bgcolor= "#E6E6FA">
<head>
	<title>Search Result</title>
</head>

<body>
	<h1 align = "center"><font color = "red">Physician search:</font></h1>
	<table border="1">
	<tr>
		<th>NPI</th>
		<th>First Name</th>
		<th>Middle Name</th>
		<th>Last Name</th>
		<th>Zip code</th>
		<th>Telephone Number</th>
	</tr>
	%for q in rows:
	<tr>
		<td>{{q['NPI']}}</td>
		<td>{{q['Provider_First_Name']}}</td>
		<td>{{q['Provider_Middle_Name']}}</td>
		<td>{{q['Provider_Last_Name']}}</td>
		<td>{{q['Provider_Business_Mailing_Address_Postal_Code']}}</td>
		<td>{{q['Provider_Business_Mailing_Address_Telephone_Number']}}</td>
	</tr>
	%end
</table>
</body>
</html>