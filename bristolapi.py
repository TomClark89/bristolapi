import requests, json

#setup bristol api key
import settings
bristol_api_key = settings.bristol_api_key

url = 'https://bristol.api.urbanthings.io/api/2.0/rti/report?stopID=01000053227'
headers = {'X-Api-Key': bristol_api_key}

r = requests.get(url, headers=headers)

data_list = []

for i in r.json()['data']['rtiReports'][0]['upcomingCalls']:
    if 'expectedArrivalTime' in i:
        # if i['routeInfo']['lineName'] == '903':
        #     dataline = i['expectedArrivalTime'],i['tripInfo']['headsign'],i['routeInfo']['lineName']
        #     data_list.append(data_line_string)
        dataline = i['expectedArrivalTime'],i['tripInfo']['headsign'],i['routeInfo']['lineName']
        data_line_string = " | ".join(dataline)
        data_list.append(data_line_string)

email_body = ("\n".join(data_list))

print(email_body)