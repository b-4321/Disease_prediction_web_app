<?php
$usname = $_POST["usname"];
$pass = $_POST["pass"];

//database connection
$conn = new mysqli("localhost","root","","project");

//check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
$sql = "SELECT * FROM registration
        WHERE username='$usname' AND pass='$pass'";

$result = mysqli_query($conn,$sql);
$count = mysqli_num_rows($result);
if($count>0){
    echo "Login Sucessful";
}
else{
    echo "Login error!";
}
  $conn->close();

?>