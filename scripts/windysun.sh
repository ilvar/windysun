ls -1 | grep -v "^locals" | xargs -n 1 -IHERE cp -rf HERE ../windysun/
cp -rf ./locals/vietnam/* ../windysun/
cp ../windysun/settings-server/* ../windysun/