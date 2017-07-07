<!DOCTYPE html>
<html>
<body bgcolor= "#6BEC1C">
<head>
<style>
body {font-family: "Lato", sans-serif;}
/* Style the tab */
div.tab {
    overflow: hidden;
    border: 1px solid #ccc;
    background-color: #E6E6FA;
}

/* Style the buttons inside the tab */
div.tab button {
    background-color: inherit;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    transition: 0.3s;
    font-size: 17px;
}

/* Change background color of buttons on hover */
div.tab button:hover {
    background-color: #ddd;
}

/* Create an active/current tablink class */
div.tab button.active {
    background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
    display: none;
    padding: 6px 12px;
    border: 1px solid #ccc;
    border-top: none;
    background-color: #ccc;
    -webkit-animation: fadeEffect 1s;
    animation: fadeEffect 1s;
}

.topright {
    float: right;
    cursor: pointer;
    font-size: 20px;
}

.topright:hover {color: red;}

@-webkit-keyframes fadeEffect {
    from {opacity: 0;}
    to {opacity: 1;}
}

@keyframes fadeEffect {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
</head>
<body>
<h1 align = "center"><font color = "red"><b>Physician Lookup for Patients and Organisations</b></font></h1>
<p>Select whether a patient or a hospital looking for the physician:</p>

<div class="tab">
  <button class="tablinks" onclick="openCity(event, 'Patient')">Patient</button>
  <button class="tablinks" onclick="openCity(event, 'Organization/Hospital')">Organization/Hospital</button>
</div>

<div id="Patient" class="tabcontent">
  <span onclick="this.parentElement.style.display='none'" class="topright">x</span>
  <h3>Patient</h3>
  <h1 align ="center"><font color = "navy">Physician Lookup</font></h1>
  <p align = "center">Enter any of the following physician details:</p>
  <form action = "/physician_lookup_pat" method = "POST">
		<center>
		Speciality:<br>
		 <input type = "text" name="speciality", id="ajax", list="json-datalist", placeholder="Grouping">
		 <input type = "text" name="speciality2", id="ajax2", list="json-datalist2", placeholder="Classification"><br>
		<datalist id="json-datalist"></datalist>
		<datalist id="json-datalist2"></datalist>
		<br>
		First Name: <input type = "text" name ="first_name"><br>
		<br>
		Last Name : <input type = "text" name = "lne"><br>
		<br>
		ZIP code: <input type = "text" name = "zip"><br>
		<br>
		State: <input type = "text" name = "state"><br>
		<br>
		Organization: <input type = "text" name = "org"><br>
		<br>
		<input type="submit" value="Search">
		<input type="reset">
		</center>
	</form>
</div>

<div id="Organization/Hospital" class="tabcontent">
  <span onclick="this.parentElement.style.display='none'" class="topright">x</span>
  <h3>Organization/Hospital</h3>
  <h1 align ="center"><font color = "navy">Physician Lookup</font></h1>
	<h2 align ="center"><font color = "red">Select the type of search and enter details:-</font></h2>
	<br>
	<form action = "/physician_lookup_org" method = "POST">
		<center>
		<input type="radio" name="type" value="NPI" checked><font color = "navy">NPI Number Lookup</font><br>
		NPI number: <input type = "text" name = "npi"><br>
		<br>
		<input type="radio" name="type" value="name"><font color = "navy"> First/Last name:-</font><br>
		Last Name : <input type = "text" name = "lne"><br>
		First Name : <input type = "text" name ="first_name"><br>
		<br>
		<input type="submit" value="Search">
		<input type="reset">
		</center>
	</form>
</div>

<script>
function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
}
</script>
<script>
var lookup = {};
var lookup2 = {};
var resultg = [];
var dataList = document.getElementById('json-datalist');
var dataList2 = document.getElementById('json-datalist2');
var input = document.getElementById('ajax');
var request = new XMLHttpRequest();
request.onreadystatechange = function() {
	console.log("Hello");
  if (request.readyState === 4) {
    if (request.status === 200) {
      // Parse the JSON
      var jsonOptions = JSON.parse(request.responseText);
  
      // Loop over the JSON array.
      jsonOptions.forEach(function(item) {
        // Create a new <option> element.
  		var grouping = item.grouping;
		var classification = item.classification
  		if (!(grouping in lookup)) {
    		lookup[grouping] = 1;
    		var option = document.createElement('option');
    		option.value = grouping;
    		dataList.appendChild(option);
		  }
		if (!(classification in lookup2)) {
			lookup2[classification] =1;
			var option2 = document.createElement('option');
    		option2.value = classification;
    		dataList2.appendChild(option2);
    	}
        // Set the value using the item in the JSON array.
        
        // Add the <option> element to the <datalist>.
      });
      
      // Update the placeholder text.
      input.placeholder = "Grouping";
    } else {
      // An error occured :(
      input.placeholder = "Couldn't load datalist options :(";
    }
  }
};

// Update the placeholder text.
input.placeholder = "Loading options...";

// Set up and make the request.
request.open('POST', '/ajax', true);
request.send();
</script>
     
</body>
</html> 
