<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: *");

header("Content-type: text/tsv");
header("Content-Disposition: attachment; filename=file.tsv");
header("Pragma: no-cache");
header("Expires: 0");



//load data
$dbhost = 'localhost';
$dbuser = 'barberca_dank';
$dbpass = 'dankdankdank';
$dbname = 'barberca_dankdata';
$conn = mysqli_connect($dbhost, $dbuser, $dbpass,$dbname);

if(! $conn ) {
    die('Could not connect: ' . mysqli_error("ds"));
}


$sql = "SELECT * FROM sensor_data WHERE 1 = 1";

if(isset($_GET["start"])){
	$start_time = $_GET["start"];
	$start_dt = new DateTime("@$start_time");
	$start_dt = $start_dt->format('Y-m-d H:i:s');
	$sql = $sql . " AND time >= '$start_dt'";
}

if(isset($_GET["end"])){
	$end_time = $_GET["end"];
	$end_dt = new DateTime("@$end_time");
	$end_dt = $end_dt->format('Y-m-d H:i:s');
	$sql = $sql . " AND time <= '$end_dt'";
}

if(isset($_GET["type"])){
	$sql = $sql . " AND type = '" . $_GET["type"] . "'";
}


$result = mysqli_query($conn, $sql);

echo "time\tplant_id\ttype\tvalue\n";

if (mysqli_num_rows($result) > 0) {
    while($row = mysqli_fetch_assoc($result)) {
    echo $row["time"]. "\t" . $row["plant_id"] . "\t" . $row["type"] . "\t" . $row["value"] . "\n";

    }
    } else {
    echo "0 results";
}
mysqli_close($conn);
?>