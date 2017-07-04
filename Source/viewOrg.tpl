<!DOCTYPE html>

<html>
<body bgcolor= "#E6E6FA">
<head>
	<title>View by Npi</title>
</head>

<body>
	<h1 align ="center"><font color = "navy">NPI Number Lookup</font></h1>
	<h2 align ="center"><font color = "red">This is an organization.</font></h2>
	<br>
	<center>
	<table border = 1>
	<tr>
	<td>Name:</td> <td>{{phy['n4']}}</td><br>
	</tr>
	<tr>
	<td>ZIP:</td><td>{{phy['n24']}}</td><br>
	</tr>
	<tr>
	<td>State Code:</td><td>{{phy['n23']}}</td><br>
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