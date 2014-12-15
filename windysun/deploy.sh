cd /var/www/windymain
git pull 
./scripts/windy.sh
./scripts/windysun.sh
./scripts/windyeng.sh
/etc/init.d/apache2 restart