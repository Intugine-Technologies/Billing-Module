#!/usr/bin/env bash
declare -a clients=(
    "cosma"
    "merino"
    "mahindra_net"
    "powerol"
    "rajasthan"
    "siemens"
    "spicer"
    "mahindraauto"
    "mahindra_tractor_inbound"
    "mahindra_tractor_outbound"
    "belden"
    "spares"
    "bulk"
    )

declare -a tdays=(
    "pando"
    "lplogics"
    "ezyhaul"
    "goex"
    "bridgestone"
    "contractlogics"
    "goldplus"
    "3scsaksham"
    "philips"
    "jusda"
    "piind"
    "boltcargo"
    "arc_trans"
)

declare -a tpings=(
    "ravi"
    "elasticrun"
)

mkdir data
mkdir all_users

for i in "${clients[@]}"
do
    echo "$i"
#    python3 main.py 1 5 2019 31 5 2019 data TRIPDAYS mahindra "$i"
#    python3 main.py 1 6 2019 30 6 2019 data TRIPDAYS mahindra "$i"
done


for i in "${tdays[@]}"
do
    echo "$i"
#    python3 main.py 1 6 2019 30 6 2019 data TRIPDAYS "$i"
done


for i in "${tpings[@]}"
do
    echo "$i"
#    python3 main.py 1 6 2019 30 6 2019 data TRIPPINGS "$i"
done


#python3 main.py 1 4 2019 30 6 2019 data TRIPDAYS "kwe"
#python3 main.py 1 1 2019 31 5 2019 data TRIPDAYS  "pando"

#python3 main.py 1 6 2019 30 6 2019 data TRIPDAYS "bridgestone"

#python3 main.py 1 4 2019 30 4 2019 data TRIPDAYS "kwe"
#python3 main.py 1 5 2019 31 5 2019 data TRIPDAYS "kwe"
#python3 main.py 1 3 2019 31 3 2019 data TRIPDAYS "kwe"

#python3 main.py -s="1/5/2019" -e="1/7/2019" -o="mahindra_swaraj_all" --dir="data" -u="mahindra" -c="swaraj"

python3 main.py -s="1/6/2019" -e="1/7/2019" -o="mahindra" --dir="data" -u="mahindra"
#python3 main.py -s="1/6/2019" -e="1/7/2019" -o="bridgestone" --dir="data" -u="bridgestone"


#python3 main.py -s="1/1/2019" -e="1/7/2019" -o="mayank" -t="TRIPDAYS" --dir="data" -q='{
#  "$and": [
#    {
#      "started_by": {
#        "$in": ["mahindratest", "mahindraprod"]
#      }
#    }
#  ]
#}'


#python3 main.py 1 5 2019 31 5 2019 data TRIPDAYS mahindra "mahindra_tractor_inbound"
#python3 main.py 1 5 2019 31 5 2019 data TRIPDAYS mahindra "mahindra_tractor_outbound"

#boltcargo
#elastricrun