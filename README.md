# my_psa

pip install "fastapi[standard]"

pip install uvicorn

sudo apt-get update
sudo apt-get upgrade

# Setup Router

- Setup Static IP for Server
- Forward SSH Port 22
- Forward HTTP Port 80
- Forward HTTPS Port 443

# Install OpenSSH server and Configure to listen on all interfaces

sudo apt install openssh-server

sudo nano /etc/ssh/sshd_config

**Changed**: enable SSH access from all interfaces

- Port 22
- ListenAddress 0.0.0.0

sudo systemctl enable ssh
sudo systemctl start ssh

> sudo systemctl restart ssh

# Configure systemd-logind to ignore lid switch events

sudo nano /etc/systemd/logind.conf

**Changed**: make sure labtop does not suspend or hibernate when lid is closed

- HandleLidSwitch=ignore
- HandleLidSwitchExternalPower=ignore
- HandleLidSwitchDocked=ignore

sudo systemctl restart systemd-logind

# Connect to the server via SSH

ssh muysengly@192.168.18.201

# Install FastAPI and Uvicorn

pip install fastapi

git clone https://github.com/muysengly-itc/my_psa.git

cd my_psa

> To update the repository, run:

git pull origin main

# Create a virtual environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# remove

rm -rf venv

sudo su

uvicorn app:app --host 127.0.0.1 --port 8000 --reload
uvicorn app:app --host 0.0.0.0 --port 8000 --reload

203.176.137.36:8000
