# VPS Security Checklist

## Priminimas
Uždėti security hardeningą Hostinger VPS šią savaitę.

## Žingsniai (root reikalingas):

```bash
# 1. Firewall
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow 8080  # OpenClaw port
ufw enable

# 2. SSH hardening
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
systemctl restart sshd

# 3. Auto updates
apt install unattended-upgrades -y

# 4. Fail2ban
apt install fail2ban -y
```

## Sukurta
2026-02-10

## Statusas
⏳ Laukiama vartotojo