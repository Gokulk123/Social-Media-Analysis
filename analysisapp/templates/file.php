<?php 
include('session.php');
 $conn = new PDO('mysql:host=localhost;dbname=socialdb', 'root', ''); 
 $rows = array();
 $query = $conn->query("select * from post LEFT JOIN members on members.member_id = post.member_id WHERE members.member_id ='".$_SESSION['id']."' order by post_id DESC");
while($row = $query->fetch())
{
    $rows[] = $row;
}

json_encode($rows);
?>