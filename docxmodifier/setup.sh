#!/bin/bash

# Ubuntu packagespackages=("python2.7" "python-dev" "libpq-dev" "python-pip")

# install Ubuntu packages
step=1
echo -e "Step" $step "- Installing Ubuntu packages\n"
for i in "${packages[@]}"; do   # The quotes are necessary here
    echo "$i"
    apt-get install -y $i
done

# install Python packages
step=$((step+1))
echo -e "\nStep" $step "- Installing Python Packages\n"
pip install -r requirements.txt


# migrate database
step=$((step+1))
echo -e "\nStep" $step "- Migrating Database\n"
python manage.py migrate

