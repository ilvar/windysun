cd ..
rm *.pyc
rm settings.py
rm urls.py
rm -rf setitngs*
git add .
git commit -m 'quick deploy commit'
git push
../../../windy-deploy.sh