ls -1 | grep -v "^locals" | xargs -n 1 -IHERE cp -rf HERE ../windyeng/
cp -rf ./locals/balieng/* ../windyeng/
cp -rf ../windyeng/settings-server/* ../windyeng/