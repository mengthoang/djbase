#!/bin/bash
set -ex

RED='\033[0;31m'
NC='\033[0m' # No Color
Yellow='\033[0;33m'

workingdir="$(dirname "$0")"

case $1 in
    init)
        # ${workingdir}/initial.sh
        docker-compose run web python manage.py migrate
        # docker-compose run web python manage.py loaddata */fixtures/*.json
        docker-compose run web python manage.py createsuperuser
        echo -e "${Yellow}Please use the following command ${RED}\"${workingdir}/djbase.sh start\" ${NC}or ${RED}\"docker-compose up\" ${NC}to start developement server.${NC}"
    ;;
    start)
        docker-compose up
    ;;
    migrate)
        docker-compose run web python manage.py migrate
    ;;
    makemigrations)
        docker-compose run web python manage.py makemigration
    ;;
    *)
        echo -e "${RED}***${Yellow}Please use one of the following arguments ${NC}(${RED}${workingdir}/djbase.sh ${RED}init${NC}|${RED}start${NC}|${RED}migrate${NC}|${RED}makemigrations${NC})${RED}***${NC}"
    ;;
esac