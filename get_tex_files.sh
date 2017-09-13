#!/bin/bash


wget -qO- https://stacks.math.columbia.edu/browse  | grep -Po "href=\'[^\']+?\.tex\'" | grep -Po "[^']+\.tex"  | sed -r 's_/blob/_/raw/_'  > tex_urls.txt


while read -r url
do
wget -P tex_files  "$url"
done < tex_urls.txt
