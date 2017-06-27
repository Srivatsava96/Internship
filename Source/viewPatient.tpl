<!DOCTYPE html>

<html>
<body bgcolor= "#E6E6FA">
<head>
	<title>View Patient</title>
</head>
<body>
<h1>Patient details</h1>
	Gender: {{patient['sex']}}<br>
	Title: {{patient['title']}}<br>
	First name: {{patient['gname']}}<br>
	Middle Initial: {{patient['mi']}}<br>
	Last name: {{patient['surname']}}<br>
	Address: {{patient['add']}}<br>
	City: {{patient['city']}}<br>
	State: {{patient['state']}}<br>
	Zip: {{patient['zip']}}<br>
	Country: {{patient['country']}}<br>
	Email: {{patient['email']}}<br>
	Telephone: {{patient['tel']}}<br>
	Date of Birth: {{patient['dob']}}<br>
	National Id: {{patient['nid']}}<br>
	Blood Group: {{patient['bg']}}<br>
	Weight: {{patient['weight']}}<br>
	Height: {{patient['height']}}<br>
	Telephone Code: {{patient['telcc']}}<br>
	Occupation: {{patient['occ']}}<br>
	Company: {{patient['com']}}<br>
</body>

</html>