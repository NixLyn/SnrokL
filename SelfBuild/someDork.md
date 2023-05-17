# Reverse Scan #

## Get IP-Geo ##


### The Request ###

```
    curl http://ip-api.com/json/<ip-addr>
```



### The Expexted OutPut Type ###

```
{
    "status":"success",
    "country":"United States",
    "countryCode":"US",
    "region":"NY",
    "regionName":"New York",
    "city":"New York",
    "zip":"10014",
    "lat":40.729,
    "lon":-74.0055,
    "timezone":"America/New_York",
    "isp":"Squarespace, Inc.",
    "org":"Squarespace, Inc.",
    "as":"AS53831 Squarespace, Inc.",
    "query":"198.49.23.144"
}  
```


### More Opts ###

```
http://ip-api.com/json/{query}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query
```

or simply:

```
http://ip-api.com/json/{query}?fields=66846719
```



### MAC-LookUp ###

```
mac_addr = "82:4B:F5:41:42:83"
```

so... 

```
mac_query = mac_addr.replace(":", "%3A")
```

Hence
```
cmd = f"curl https://udger.com/resources/mac-address-vendor-lookup?macaddress={mac_qeury}"

```

then.. 

```
query_ret = subprocess.getoutput(cmd)
```

