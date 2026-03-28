echo "[+] Starting..." 
pkg install -y python3 || apt install -y python3 ||dnf install -y python3 --skip-broken || yum install -y python3 --skip-broken || pacman -S --noconfirm python3
command -v curl
pkg install -y curl || apt install -y curl || dnf install -y curl --skip-broken || yum install -y curl --skip-broken || pacman -S --noconfirm curl

mkdir -p ~/Sy-PackInst
curl -L -o ~/Sy-PackInst/Sy-PackInst.py https://raw.githubusercontent.com/Syaifanisa/Sy-PackInst/main/Sy-PackInst.py
echo "[+] Making Alias"
if ! grep -q "ALIAS_LINE=" ~/.bashrc; then
    ALIAS_LINE="alias Sy-PackInst='python3 ~/Sy-PackInst/Sy-PackInst.py'"
fi
echo "[+] Done, type 'source ~/.bashrc' and then 'Sy-PackInst' to run it."
rm -- "$0"
