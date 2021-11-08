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
if ($result->num_rows > 0) {
  // output data of each row
  //$output->birth = ["place" => []];
  //  $output->birth->place = [];
  while($row = $result->fetch_assoc()) {
    if ($row["givenName"] != "null") {
      $output->givenName = ["en" => $row["givenName"]];
    }
    if ($row["familyName"] != "null") {
      $output->familyName = ["en" => $row["familyName"]];
    }
    if ($row["gender"] != "null") {
      $output->gender = $row["gender"];
    }
    if ($row["birthdate"] != "null") {
      $output->birth->date = $row["birthdate"];
    }
    if ($row["city"] != "null") {
      $output->birth->place->city = ["en" => $row["city"]];
    }
    if ($row["country"] != "null") {
      $output->birth->place->country = ["en" => $row["country"]];
    }
  }
}
$sql_main = "SELECT l.id, orgName, birthdate, city, country FROM Laureates l, Organization o, Birth b, Place pl WHERE l.id=o.id AND l.id=b.id AND b.pid=pl.id AND l.id=" . $_GET['id'] ;
$result = $conn->query($sql_main);
if ($result->num_rows > 0) {
  // output data of each row

  while($row = $result->fetch_assoc()) {
    if ($row["orgName"] != "null") {
      $output->orgName = ["en" => $row["orgName"]];
    }
    if ($row["birthdate"] != "null") {
      $output->founded->date = $row["birthdate"];
    }
    if ($row["city"] != "null") {
      $output->founded->place->city = ["en" => $row["city"]];
    }
    if ($row["country"] != "null") {
      $output->founded->place->country = ["en" => $row["country"]];
    }
  }
}

$sql_main = "SELECT l.id, aid, year, category, sortOrder FROM Laureates l, Prize p WHERE l.nid=p.id AND l.id=" . $_GET['id'] ;
$result = $conn->query($sql_main);
if ($result->num_rows > 0) {
  // output data of each row
  $output->nobelPrizes = array();
  while($row = $result->fetch_assoc()) {
    $temp_prize_arr = (object) [];
    if ($row["year"] != "null") {
      $temp_prize_arr->awardYear = $row["year"];
    }
    if ($row["category"] != "null") {
      $temp_prize_arr->category = ["en" => $row["category"]];
    }
    if ($row["sortOrder"] != "null") {
      $temp_prize_arr->sortOrder = $row["sortOrder"];
    }
    
    $sql_assoc = "SELECT affiliationName, city, country FROM Affiliations a, Place p WHERE a.pid=p.id AND a.id=" . $row["aid"];
    $result_assoc = $conn->query($sql_assoc);
    if ($result_assoc->num_rows > 0) {
      // output data of each row
      $temp_prize_arr->affiliations = array();
      while($row_assoc = $result_assoc->fetch_assoc()) {
        $temp_arr = (object) [];
	if ($row_assoc["affiliationName"] != "null") {
	  $temp_arr->name = ["en" => $row_assoc["affiliationName"]];
	}
	if ($row_assoc["city"] != "null") {
	  $temp_arr->city = ["en" => $row_assoc["city"]];
	}
	if ($row_assoc["country"] != "null") {
	  $temp_arr->country = ["en" => $row_assoc["country"]];
	}
	//	echo $temp_arr->city;
	$temp_prize_arr->affiliations[] = $temp_arr;
      }
    }
    $output->nobelPrizes[] = $temp_prize_arr;
  }
}


// // get the id parameter from the request


// set the Content-Type header to JSON, 
// so that the client knows that we are returning JSON data
header('Content-Type: application/json');
echo json_encode($output, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);

?>
