rm ~/.ssh/known_hosts
docker rm bweb
docker run --name bweb -it -p 8008:80 -p 2222:22 bweb
