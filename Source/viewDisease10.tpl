<!DOCTYPE html>

<html>
<body bgcolor= "#E6E6FA">
<head>
	<title>ICD lookup</title>
</head>

<body>
	<h1 align ="center"><font color = "navy">ICD-10 Lookup</font></h1>
	<br>
	<table border="1" align ="center">
	<tr>
		<th>ICD-10 code</th>
		<th>Disease description</th>
	</tr>
	%for q in icd:
		<tr>
			<td>{{q['code']}}</td>
			<td>{{q['disease']}}</td>
		</tr>
	%end
	</table>
	<br>
	<a href="http://localhost:8082/">Back to search for more codes</a><br>
	<br>
</body>
</html>