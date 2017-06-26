<!DOCTYPE html>

<html>
<body bgcolor= "#E6E6FA">
<head>
	<title>NPI lookup</title>
</head>

<body>
	<h1 align ="center"><font color = "navy">NPI Number Lookup</font></h1>
	<h2 align ="center"><font color = "red">National NPI registry</font></h2>
	<br>
	<form action = "/npi_lookup" method = "POST">
		<center>
		Last Name : <input type = "text" name = "lne"><br>
		First Name : <input type = "text" name ="first_name"><br>
		<br>
		or Search by NPI number: <input type = "text" name = "npi"><br>
		<br>
		<input type="submit" value="Submit">
		<input type="reset">
		</center>
	</form>
</body>
</html>