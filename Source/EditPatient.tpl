<!DOCTYPE html>

<html>
<body bgcolor= "#E6E6FA">
<head>
	<title>Edit Patient</title>
	<link rel="stylesheet" href="style.css">
</head>
<body>
<h1> Edit Patient Details </h1>
<form action="/edit_patient.php" method="post">
	Gender:<input type="text" name="sex" value={{patient['sex']}}><br>
	Title:<input type="text" name="title" value={{patient['title']}}><br>
	First name:<input type="text" name="firstname" value={{patient['gname']}}><br>
	Middle Initial:<input type="text" name="midinitial" value={{patient['mi']}}><br>
	Last name:<input type="text" name="lastname" value={{patient['surname']}}><br>
	Address:<input type="text" name="address" value={{patient['add']}}><br>
	City:<input type="text" name="city" value={{patient['city']}}><br>
	State:<input type="text" name="state" value={{patient['state']}}><br>
	Zip:<input type="text" name="zip" value={{patient['zip']}}><br>
	Country:<input type="text" name="country" value={{patient['country']}}><br>
	Email:<input type="text" name="email" value={{patient['email']}}><br>
	Telephone:<input type="text" name="tel" value={{patient['tel']}}><br>
	Date of Birth:<input type="text" name="dob" value={{patient['dob']}}><br>
	National Id:<input type="text" name="nid" value={{patient['nid']}}><br>
	Blood Group:<input type="text" name="bg" value={{patient['bg']}}><br>
	Weight:<input type="text" name="weight" value={{patient['weight']}}><br>
	Height:<input type="text" name="height" value={{patient['height']}}><br>
	Telephone Code:<input type="text" name="telcc" value={{patient['telcc']}}><br>
	Occupation:<input type="text" name="occupation" value={{patient['occ']}}><br>
	Company:<input type="text" name="company" value={{patient['com']}}><br><br>
	<input type="submit" value="Submit">
	<input type="reset">
 
</form>
</body>
</html>