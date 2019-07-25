# BillingModule

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
    python3 main.py -d=1/1/2019 -e=1/2/2019 -o=data -t="TRIPDAYS" -u="lplogics"
