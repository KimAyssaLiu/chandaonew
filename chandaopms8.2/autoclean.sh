sudo docker stop $(sudo docker ps -aq)

sudo docker rm $(sudo docker ps -aq)

sudo docker rmi $(sudo docker images -q)

sudo docker ps -a

sudo docker ps 

sudo docker images
