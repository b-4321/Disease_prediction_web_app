<?php
$usname = $_POST["usname"];
$email = $_POST["email"];
$pass = $_POST["pass"];
 //database connection
 $conn = new mysqli("localhost","root","","project");
 //check connection
 if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
 }

    $sql = "INSERT INTO registration(username,email,pass)
    VALUES ('$usname', '$email', '$pass')";
    if($conn->query($sql)=== TRUE){
      echo "Registration sucessfull.";
    }
    else{
      echo "Error:". $sql . "<br>". $conn->error;
    }
    $conn->close();
?>