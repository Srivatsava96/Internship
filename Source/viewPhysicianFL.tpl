<!DOCTYPE html>

<html>
<body bgcolor= "#6BEC1C">
<head>
	<title>Search Result</title>
</head>

<body>
	<h1 align = "center"><font color = "red">Physician search:</font></h1>
	<table border="1" align = "center" bgcolor= "#E6E6FA">
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
		<td>{{q.get('n6') or ""}}</td>
		<td>{{q.get('n7') or ""}}</td>
		<td>{{q.get('n5') or ""}}</td>
		<td>{{q.get('n24') or ""}}</td>
		<td>{{q.get('n26') or ""}}</td>
	</tr>
	%end
</table>
</body>
</html>