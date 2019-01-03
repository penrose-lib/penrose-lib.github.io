BASEURL=https://circle-artifacts.com/gh/penrose-lib/penrose-lib.github.com/$CIRCLE_BUILD_NUM/artifacts/0/home/ubuntu/penrose-lib.github.io/_site
sed -i "14 s,.*,destination: ./_site,g" "config.yml"
sed -i "11 s,.*,baseurl: $BASEURL,g" "config.yml"
