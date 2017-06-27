<!DOCTYPE html>

<html>
<body bgcolor= "#E6E6FA">
<head>
	<title>Patient Detail Edit Success</title>
</head>
<body>
	<h1>Patient Data Successfully changed</h1>
	<table>
	<tr>
		<td>{{patient['sex']}}</td>
		<td>{{patient['title']}}</td>
		<td>{{patient['gname']}}</td>
		<td>{{patient['mi']}}</td>
		<td>{{patient['surname']}}</td>
		<td>{{patient['add']}}</td>
		<td>{{patient['city']}}</td>
		<td>{{patient['state']}}</td>
		<td>{{patient['zip']}}</td>
		<td>{{patient['country']}}</td>
		<td>{{patient['email']}}</td>
		<td>{{patient['tel']}}</td>
		<td>{{patient['dob']}}</td>
		<td><a href="http://localhost:8082/patients/edit/{{patient['nid']}}">{{patient['nid']}}</a></td>
		<td>{{patient['bg']}}</td>
		<td>{{patient['weight']}}</td>
		<td>{{patient['height']}}</td>
		<td>{{patient['telcc']}}</td>
		<td>{{patient['occ']}}</td>
		<td>{{patient['com']}}</td>
	</tr>
	</table>
</body>

</html>