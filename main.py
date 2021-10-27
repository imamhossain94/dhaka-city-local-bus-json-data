from requests import get, post, Session
from bs4 import BeautifulSoup
import json


def get_bus_data(url):
    final_data = {'data': list()}
    try:
        html = get(url).text
        tables = BeautifulSoup(str(html), 'html.parser').find_all('table')[0:]
        global_data = []
        for table in tables:
            rows = BeautifulSoup(str(table), 'html.parser').find_all('tr')[0:]
            for row in rows[0:]:
                cols = row.find_all('td')
                local_data = {}
                if len(cols) != 0:
                    bus_name_english = cols[0].text.split('(')[0].replace(' Bus Route', '').strip()
                    bus_name_bangle = cols[0].text.split('(')[1].replace(')', '').strip()
                    routes = cols[1].text.replace('See Full Route Map', '').split(' ⇄ ')
                    time = cols[2].text
                    service_type = cols[3].text
                    local_data = {
                        "english": bus_name_english,
                        "bangle": bus_name_bangle,
                        "routes": routes,
                        "time": time,
                        "service_type": service_type
                    }
                if local_data != {}:
                    global_data.append(local_data)

        final_data['data'] = global_data
        print(json.dumps(final_data))
    except Exception as ex:
        final_data = {'status': 'failed', 'reason': str(ex)}
        print(json.dumps(final_data))
    return final_data


get_bus_data("https://busroutebd.com/dhaka-local-bus-routes/")
