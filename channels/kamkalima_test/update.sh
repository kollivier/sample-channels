#!/usr/bin/env bash
set -e

cd content

if [ -f two_friends_in_desert.zip ]; then
  rm two_friends_in_desert.zip
fi

cd two_friends_in_desert
echo "Creatin HTML5Zip file two_friends_in_desert.zip"
zip -r ../two_friends_in_desert.zip *

