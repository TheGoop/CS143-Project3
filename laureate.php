<?php
$servername = "localhost";
$username = "cs143";
$password = "";
$dbname = "class_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
$id = intval($_GET['id']);
$output = (object) [
    "id" => strval($id),
];
$sql_main = "SELECT l.id, givenName, familyName, gender, birthdate, city, country FROM Laureates l, Person p, Birth b, Place pl WHERE l.id=p.id AND l.id=b.id AND b.pid=pl.id AND l.id=" . $_GET['id'] ;
$result = $conn->query($sql_main);
echo "<p>hi<p>";
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
  	echo "Hello";
    if ($row["givenName"] != "null") {
      $output["givenName"] = ["en" => $row["givenName"]];
    }
    if ($row["familyName"] != "null") {
      $output["familyName"] = ["en" => $row["familyName"]];
    }
    if ($row["gender"] != "null") {
      $output["gender"] = $row["gender"];
    }
    if ($row["birthdate"] != "null") {
      $output["birthdate"] = $row["birthdate"];
    }
    if ($row["city"] != "null") {
      $output["city"] = $row["city"];
    }
    if ($row["country"] != "null") {
      $output["country"] = $row["country"];
    }
  }
}

// get the id parameter from the request


// set the Content-Type header to JSON, 
// so that the client knows that we are returning JSON data
header('Content-Type: application/json');

/*
   Send the following fake JSON as the result
   {  "id": $id,
      "givenName": { "en": "A. Michael" },
      "familyName": { "en": "Spencer" },
      "affiliations": [ "UCLA", "White House" ]
   }
*/

// $output = (object) [
//     "id" => strval($id),
//     "givenName" => (object) [
//         "en" => "A. Michael"
//     ],
//     "familyName" => (object) [
//         "en" => "Spencer"
//     ],
//     "affliations" => array(
//         "UCLA",
//         "White House"
//     )
// ];
echo json_encode($output);

?>
