# Table of contents / Table de matières :
1. [ Description (English). ](#en)
    - Robot Behavior
    - Makefile
2. [ Description (Français). ](#fr)
    - Comportement du Robot
    - Makefile


<a name="en"></a>
# Description [English]
This project aims to design and program algorithms that allow a robot to pick up K tennis balls scattered arbitrarily. The positions of the robot and the balls are represented by integer coordinates. The main objective is to enable the robot to return to its starting point after collecting all the balls.

# Robot Behavior

The characteristics of the robot's behavior are as follows:

- The robot has a constant movement speed, equivalent to one unit per step.
- The process of picking up a tennis ball is considered instantaneous and does not take any additional time.
- To pick up a ball, the robot must be positioned directly on top of it.
- When it wants to change its direction of movement, the robot must stop, turn around, and then proceed in the new direction. The time required to make this change in direction is determined by a real parameter C, multiplied by the angle in radians α between the new displacement vector and the old displacement vector.
- The robot has the ability to turn in both directions.
At the start of the project, the robot is initially oriented upwards. Unless otherwise specified, it is positioned at coordinates (N/2, N/2), where N represents a parameter defining the width of the grid.

To successfully complete this project, it will be necessary to develop efficient algorithmic strategies for collecting the tennis balls while optimizing movement times and direction changes.

# Makefile

python3 project.py "csv file name" "world size" "movement speed" "rotation speed"



<a name="fr"></a>
# Description [Français]

Ce projet vise à concevoir et programmer des algorithmes permettant à un robot de ramasser K balles de tennis réparties de manière arbitraire. Les positions du robot et des balles sont représentées par des coordonnées entières. L'objectif principal est de permettre au robot de retourner à son point de départ après avoir collecté toutes les balles.

# Comportement du Robot

Les caractéristiques du comportement du robot sont les suivantes :

- Le robot possède une vitesse de déplacement constante, équivalente à une unité par pas.
- Le processus de ramassage d'une balle de tennis est considéré comme instantané et ne prend aucun temps supplémentaire.
- Pour ramasser une balle, le robot doit être positionné directement dessus.
- Lorsqu'il souhaite changer de direction de déplacement, le robot doit s'arrêter, tourner sur lui-même, puis repartir dans la nouvelle direction. Le temps nécessaire pour effectuer ce changement de direction est déterminé par un paramètre réel C, multiplié par l'angle en radian α entre le nouveau vecteur de déplacement et l'ancien vecteur de déplacement.
- Le robot a la capacité de tourner dans les deux sens.

Au démarrage du projet, le robot est initialement orienté vers le haut. À moins d'indications particulières, il est positionné aux coordonnées (N/2, N/2), où N représente un paramètre définissant la largeur de la grille.

Pour mener à bien ce projet, il sera nécessaire de développer des stratégies d'algorithme efficaces pour la collecte des balles de tennis, tout en optimisant les temps de déplacement et les changements de direction.

# Makefile

python3 project.py "nom fichier cvs" "taille du monde" "vitesse de deplacement" "vitesse de rotation"

La commande ```make fig``` permet d'exécuter les deux algorithmes dans des situations différentes et d'afficher les chemins trouvés.

La commande ```make time``` permet de calculer le temps d'exécution des algorithmes dans des mondes avec un nombre de balles variables (peut prendre un certain temps)

Le rapport ```report.pdf``` est disponible dans le dossier ```report```. Il peut être recompilé en se plaçant dans le dossier ```report``` et en effectuant la commande ```make```.
