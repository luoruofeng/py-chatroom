#!/bin/sh
echo 开始构建...

roomc=`docker ps -a | grep im-room`
httpc=`docker ps -a | grep im-http`
wsc=`docker ps -a | grep im-ws`

if [[ -n $roomc ]];then
  echo 1
  echo $roomc
  docker stop im-room
  docker rm im-room
fi

if [[ -n $wsc ]];then
  echo 2
  echo $wsc
  docker stop im-ws
  docker rm im-ws
fi

if [[ -n $httpc ]];then
  echo 3
  echo $httpc
  docker stop im-http
  docker rm im-http
fi

roomi=`docker image ls | grep im-room`
httpi=`docker image ls | grep im-http`
wsi=`docker image ls | grep im-ws`

if [[ -n $roomi ]];then
  echo 4
  echo $roomi
  docker image rm im-room:v1.0
fi

if [[ -n $wsi ]];then
  echo 5
  echo $wsi
  docker image rm im-ws:v1.0
fi

if [[ -n $httpi ]];then
  echo 6
  echo $httpi
  docker image rm im-http:v1.0
fi

imnet=`docker network ls | grep im-net`
if [[ -n $imnet ]];then
  echo 7
  echo imnet
  docker network rm im-net
  docker network create --driver bridge --subnet 172.22.16.0/24 im-net
fi

docker-compose up -d

#cd ./manage
#docker build -t im-room:v1.0 .
#
#cd ../httpsrv
#docker build -t im-http:v1.0 .
#
#cd ../ws
#docker build -t im-ws:v1.0 .
#
#docker run --network=im-net --name im-room  -d --restart=always im-room:v1.0 &
#docker run --network=im-net --name im-ws -p 5555:5555  -d --restart=always im-ws:v1.0 &
#docker run --network=im-net --name im-http -p 80:80 -d --restart=always im-http:v1.0 &

echo 完成.