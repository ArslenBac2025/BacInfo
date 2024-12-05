<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>results</title>
</head>
<body>
    <?php 

        $cin = $_POST["cin"];
        $np = $_POST["np"];
        $adr = $_POST["adr"];
        $postal = $_POST["postal"];
        $transporteur = $_POST["transporteur"];
        $fragile = isset($_POST["fragile"]) ? 'O' : 'N';

        $conn = mysqli_connect("localhost","root","admin123","ep2023");
        $query = "SELECT * FROM expediteur WHERE cinExp ='$cin'";
        $res = mysqli_query($conn, $query);
        if(mysqli_num_rows($res) == 0){
            die ("couldn't find CIN of this expeditor");
        }
        $date = date("Y-m-d H:i:s");

        $query = "INSERT INTO colis(dateColis, nomDest, adrDest, codePostal, fragile, etat, cinExp, idTrans) 
        VALUES('$date', '$np', '$adr', '$postal', '$fragile', 0, '$cin', '$transporteur')";
        
        echo $query;
    
        mysqli_query($conn, $query) or die("error:" . mysqli_error($conn));


        if(mysqli_affected_rows($conn) > 0){
            echo "success!";
        }
        else{
            die("error inserting data");
        }

        mysqli_close($conn);

    ?>
</body>
</html>