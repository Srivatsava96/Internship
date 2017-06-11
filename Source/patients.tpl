<!DOCTYPE html>

<html>
<head>
	<title>Patient Collection</title>
</head>
<body>
<h1>Patient data</h1>
<table border="1">
<tr>
	<th>Gender</th>
	<th>Title</th>
	<th>Given Name</th>
	<th>Middle name</th>
	<th>Surname</th>
	<th>Street Addr</th>
	<th>City</th>
	<th>State</th>
	<th>ZipCode</th>
	<th>Country</th>
	<th>Email</th>
	<th>Telephone</th>
	<th>Birthday</th>
	<th>National-id</th>
	<th>Bloodtype</th>
	<th>Weight</th>
	<th>Height</th>
	<th>Telcode</th>
	<th>Occupation</th>
	<th>Company</th>
</tr>
%for q in rows:
	<tr>
		<td>{{q['sex']}}</td>
		<td>{{q['title']}}</td>
		<td>{{q['gname']}}</td>
		<td>{{q['mi']}}</td>
		<td>{{q['surname']}}</td>
		<td>{{q['add']}}</td>
		<td>{{q['city']}}</td>
		<td>{{q['state']}}</td>
		<td>{{q['zip']}}</td>
		<td>{{q['country']}}</td>
		<td>{{q['email']}}</td>
		<td>{{q['tel']}}</td>
		<td>{{q['dob']}}</td>
		<td><a href="http://localhost:8082/patients/view/{{q['nid']}}">{{q['nid']}}</a></td>
		<td>{{q['bg']}}</td>
		<td>{{q['weight']}}</td>
		<td>{{q['height']}}</td>
		<td>{{q['telcc']}}</td>
		<td>{{q['occ']}}</td>
		<td>{{q['com']}}</td>
		<td><a href="http://localhost:8082/patients/edit/{{q['nid']}}">Edit</a></td>
	</tr>
%end
</table>