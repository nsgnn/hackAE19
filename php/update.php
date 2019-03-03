<?php
//load data
$dbhost = 'localhost';
$dbuser = 'barberca_dank';
$dbpass = 'dankdankdank';
$dbname = 'barberca_dankdata';
$conn = mysqli_connect($dbhost, $dbuser, $dbpass,$dbname);

if(! $conn ) {
    die('Could not connect: ' . mysqli_error("ds"));
}


$type = $_POST["type"];
$plant_id = $_POST["plant_id"];
$value = $_POST["value"];

$e_time = $_POST["time"];
$time = new DateTime();
$time->setTimestamp($e_time);
$time = $time->format('Y-m-d H:i:s');



$sql = "INSERT INTO sensor_data (`time`, `plant_id`, `type`, `value`) VALUES ('$time', '$plant_id', '$type', '$value')";
$result = mysqli_query($conn, $sql);

echo $sql;

mysqli_close($conn);
?>