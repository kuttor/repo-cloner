# Name: Clone All Yer Repos
# Purpose: Access your github and clones all repos < 100
# Version: 1.0.00
# Date: 9/11/2016

USER=$1

PAGE=1

curl "https://api.github.com/users/$USER/repos?page=$PAGE&per_page=100" | grep -e 'git_url*' | cut -d \" -f 4 | xargs -L1 git clone
