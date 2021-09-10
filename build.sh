docker network rm im-net
docker network create --driver bridge --subnet 172.22.16.0/24 im-net

roomc=docker ps -a | grep im-room
httpc=docker ps -a | grep im-http
wsc=docker ps -a | grep im-ws

if [ ! -z $roomc ];then
  docker stop im-room | docker rm im-room
fi

if [ ! -z $wsc ];then
  docker stop im-ws | docker rm im-ws
fi

if [ ! -z $httpc ];then
  docker stop im-http | docker rm im-http
fi

roomi=`docker image ls | grep im-room`
httpi=`docker image ls | grep im-http`
wsi=`docker image ls | grep im-ws`

if [ ! -z $roomi ];then
  docker image rm im-room:v1.0
fi

if [ ! -z $wsi ];then
  docker image rm im-ws:v1.0
fi

if [ ! -z $httpi ];then
  docker image rm im-http:v1.0
fi

#cd ./manage
#docker build -t im-room:v1.0 .
#
#cd ../http
#docker build -t im-http:v1.0 .
#
#cd ../ws
#docker build -t im-ws:v1.0 .
#
#docker run --network=im-net --name im-room  -d --restart=always im-room:v1.0 &
#docker run --network=im-net --name im-ws  -d --restart=always im-ws:v1.0 &
#docker run --network=im-net --name im-http -p 80:80 -d --restart=always im-http:v1.0 &