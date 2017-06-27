<!DOCTYPE html>

<html>
<head>
	<title>Organisations Collection</title>
</head>
<body>
<table border="1">
<tr>
	<th>Name</th>
	<th>NPI</th>
	
	<th>City</th>
	<th>State</th>
	<th>Zip Code</th>
	<th>Telephone Number</th>
	<th>Fax</th>
</tr>
%for q in rows:
	<tr>
		<td>{{q['name']}}</td>
		<td>{{q['npi']}}</td>
		
		<td>{{q['city']}}</td>
		<td>{{q['state']}}</td>
		<td>{{q['zip']}}</td>
		<td>{{q['tel']}}</td>
		<td>{{q['fax']}}</td>
	</tr>
%end
</table>