import requests, json, sendgrid, time

#importing settings file with variables etc.
import settings
bristol_api_key = settings.bristol_api_key
sendgrid_api_key = settings.sendgrid_api_key
email_to = settings.email_to

url = 'https://bristol.api.urbanthings.io/api/2.0/rti/report?stopID=01000053227'
headers = {'X-Api-Key': bristol_api_key}

r = requests.get(url, headers=headers)

data_list = []

for i in r.json()['data']['rtiReports'][0]['upcomingCalls']:
    if 'expectedArrivalTime' in i:
        # if i['routeInfo']['lineName'] == '903':
        #     dataline = i['expectedArrivalTime'],i['tripInfo']['headsign'],i['routeInfo']['lineName']
        #     data_list.append(data_line_string)
        time_string = i['expectedArrivalTime']
        tuple_time = time.strptime(time_string[0:19], "%Y-%m-%dT%H:%M:%S")
        time_string_new = (str(tuple_time[3]) +':'+ str(tuple_time[4]).zfill(2))
        print (time_string_new)
        headsign_text_justified = i['tripInfo']['headsign'].ljust(20)
        dataline = time_string_new,headsign_text_justified,i['routeInfo']['lineName']
        data_line_string = " | ".join(dataline)
        data_list.append(data_line_string)

email_body = '<ul><li>' + ('<li>'.join(data_list)) + '</ul>'


sg = sendgrid.SendGridClient(sendgrid_api_key)
message = sendgrid.Mail()
message.add_to(email_to)
message.set_subject('Bus timetables')
message.set_html(email_body)
#message.set_text(email_body)
message.set_from('tom@tcdj.site')
status, msg = sg.send(message)
print(status, msg)

print (email_body)