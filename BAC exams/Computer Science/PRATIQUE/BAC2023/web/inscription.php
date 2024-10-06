<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inscription</title>
</head>
<body>
    <?php

        $nom = $_POST["nom"];
        $email = $_POST["email"];
        $date = $_POST["date"];
        $genre = $_POST["genre"];
        $mdp = $_POST["mdp"];

        echo $nom;
        // $conn = mysqli_connect("localhost","root","admin123","mydb");
        // $query = "SELECT * FROM membre WHERE email = '$email'";

        // $res = mysqli_query($conn, $query);
        // if(mysqli_num_rows($res) > 0)
        // {
        //     echo "this email already exists!!";
        // }
        
        // $query = "INSERT INTO membre(nomMem, genre, dateNais, email, mdp)
        // VALUES('$nom','$genre','$date','$email','$mdp')";

        // $res = mysqli_query($conn, $query);

        // if(mysqli_affected_rows($conn) > 0)
        // {
        //     $userid = mysqli_insert_id($conn);
        //     echo $userid;
        //     echo "resussi!";
        // }
    ?>
</body>
</html>