import requests

#http://rajapinnat.ymparisto.fi/api/Hydrologiarajapinta/1.1//odata/Vedenkorkeus?$top=20&$filter=year(Aika) eq 2022 and month(Aika) eq 2 and day(Aika) eq 15&$orderby=Paikka_Id&$select=Aika,Arvo,ArvoMax,ArvoMin,Lippu_id,Paikka_Id&$expand=Paikka,Lippu

url_test = 'http://services.odata.org/V3/OData/OData.svc/Products?$format=json'

url_water_depth = 'http://rajapinnat.ymparisto.fi/api/Hydrologiarajapinta/1.1//odata/Vedenkorkeus?$top=20&$filter=year(Aika) eq 2022 and month(Aika) eq 2 and day(Aika) eq 15&$orderby=Paikka_Id&$select=Aika,Arvo,ArvoMax,ArvoMin,Lippu_id,Paikka_Id&$expand=Paikka,Lippu'


r = requests.get(url_water_depth)

r_json = r.json()
for value in r_json['value']:
    #print(value['Paikka_Id'] + " " + str(value['Arvo']) )
    print("{} {}".format(value['Paikka_Id'], str(value['Arvo'])))