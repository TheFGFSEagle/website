<?php
        $NAME = $_GET['a'];
        header("Content-Type: text/xml");
        echo "<?xml version=\"1.0\"?>\n";
        echo "<PropertyList>\n";
        echo "<params>" . htmlspecialchars($NAME) . "</params>\n";
        echo "</PropertyList>\n";
?>