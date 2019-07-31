# BillingModule

## Environment variables

|`Environ Variables`|`Values`|
|---|---|
|`DATABASE_SERVER`|`mongodb+srv://username:pass@example.mongodb.net:27017`|
|`DATABASE_CLIENT`|`Main DB Client`|

## Setup

    git clone https://github.com/Intugine-Technologies/Billing-Module.git
    cd Billing-Module
    pip3 install -r requirements.txt
    mkdir data

## Input Params

|short Param|Long Param|Help|
|---|---|---|
|`-s`| `--start`|`Start date of generating the report in (DD/MM/YYYY)`|
|`-e`| `--end`|`End date of generating the report in DD/MM/YYYY`|
|`-t`| `--type`|`Billing type TRIPDAYS / TRIPPINGS`|
|`-o`| `--output`|`Output File Name`|
|`-u`| `--username`|`User Name`|
|`-c`| `--client`|`Client Name`|
|`-d`| `--dir`|`Output Directory`|
|`-q`| `--query`|`Query`|

### Example Input
    python3 main.py -s="1/1/2019" -e="1/2/2019" -d="data" -t="TRIPDAYS" -u="lplogics"

### For all users

    python3 main.pyt -s="1/1/2019" -e="1/2/2019" -d="data"
