mkdir ../windy
ls -1 | grep -v "^locals" | xargs -n 1 -IHERE cp -rf HERE ../windy/
cp -rf ./locals/bali/* ../windy/
cp -rf ../windy/settings-server/* ../windy/