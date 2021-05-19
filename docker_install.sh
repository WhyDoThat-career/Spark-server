#docker 설치
curl -fsSL https://get.docker.com/ | sudo sh
sudo usermod -aG docker $USER
docker version

#docker-compose 설치
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version