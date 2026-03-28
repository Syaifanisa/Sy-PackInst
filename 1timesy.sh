echo "[+] Starting..." 
pkg install -y python3 >/dev/null 2>&1 || \
apt install -y python3 >/dev/null 2>&1 || \
dnf install -y python3 --skip-broken >/dev/null 2>&1 || \
yum install -y python3 --skip-broken >/dev/null 2>&1 || \
pacman -S --noconfirm python3 >/dev/null 2>&1
command -v curl >/dev/null 2>&1 || \
pkg install -y curl >/dev/null 2>&1 || \
apt install -y curl >/dev/null 2>&1 || \
dnf install -y curl --skip-broken >/dev/null 2>&1 || \
yum install -y curl --skip-broken >/dev/null 2>&1 || \
pacman -S --noconfirm curl >/dev/null 2>&1

mkdir -p ~/Sy-PackInst
curl -o ~/Sy-PackInst/Sy-PackInst.py \
https://raw.githubusercontent.com/Syaifanisa/Sy-PackInst/main/Sy-PackInst.py
echo "alias Sy-PackInst='python3 ~/Sy-PackInst/Sy-PackInst.py'" >> ~/.bashrc
source ~/.bashrc
echo "[+] Done, type 'Sy-PackInst' to run it." 
rm -- "$0" 