echo "[+] Starting..." 
pkg install -y python3 || apt install -y python3 ||dnf install -y python3 --skip-broken || yum install -y python3 --skip-broken || pacman -S --noconfirm python3
command -v curl
pkg install -y curl || apt install -y curl || dnf install -y curl --skip-broken || yum install -y curl --skip-broken || pacman -S --noconfirm curl

mkdir -p ~/Sy-PackInst
curl -o ~/Sy-PackInst/Sy-PackInst.py \
https://raw.githubusercontent.com/Syaifanisa/Sy-PackInst/main/Sy-PackInst.py
echo "[+] Making Alias"
echo "alias Sy-PackInst=' cd ~/Sy-PackInst && python3 Sy-PackInst.py && cd -'" >> ~/.bashrc
echo "[+] Running back shell"
source ~/.bashrc
echo "[+] Done, type 'Sy-PackInst' to run it." 
rm -- "$0"
