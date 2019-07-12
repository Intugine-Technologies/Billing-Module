from pymongo import MongoClient
import datetime
import re
import json
import os

gmt_to_ist = datetime.timedelta(hours=5, minutes=30)


def date_range(start_date, end_date):
    for date in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(date)


def get_database():
    server, port = os.environ['DATABASE_SERVER'].rsplit(':', 1)
    client = MongoClient(server, port=int(port))
    database = client['telenitytracking']
    return database


def get_trips(options):
    startTime = list(map(int, str(options.start).split("/")))
    start = datetime.datetime(startTime[2], startTime[1], startTime[0]) - gmt_to_ist

    endTime = list(map(int, str(options.end).split("/")))
    end = datetime.datetime(endTime[2], endTime[1], endTime[0]) - gmt_to_ist

    database = get_database()
    collection = database['trips']

    if (options.query):
        print("[Options.query]: True")
        query = json.loads(options.query)
        if '$and' not in query.keys():
            query["$and"] = []
        query["$and"] += ({
                              '$or': [{
                                  'startTime': { '$lte': end }
                              }, {
                                  'startTime': { '$lte': end.isoformat() }
                              }]
                          }, {
                              '$or': [{
                                  'endTime': { '$gte': start }
                              }, {
                                  'endTime': { '$gte': start.isoformat() }
                              }, {
                                  'running': True
                              }]
                          })
        print("~~~queryy", query)
        data = collection.find(query)
        res = list()
        for x in data:
            temp = x
            if 'client_client' in x.keys():
                temp['client_client'] = x['client_client']
            elif 'client' in x.keys():
                temp['client_client'] = x['client']
            res.append(temp)
        print("[]]]]]]")
        print(len(res))
        return res

    client = options.client
    query = {
        'user': options.username,
        'tel': {
            '$nin': ['7354670095', '8989868676', '7389898918', '7987464701', '9986888311', '7276190400', '9986663220',
                     '9920541820', '9986644720', '9841942120', '9711325880', '7550238128', '8951369532'] },
        'invoice': { '$nin': [re.compile("test", re.IGNORECASE)] },
        'truck_number': { '$nin': [re.compile("test", re.IGNORECASE)] },
        'vehicle': { '$nin': [re.compile("test", re.IGNORECASE)] },
        '$and': [{
            '$or': [{
                'startTime': { '$lte': end }
            }, {
                'startTime': { '$lte': end.isoformat() }
            }]
        }, {
            '$or': [{
                'endTime': { '$gte': start }
            }, {
                'endTime': { '$gte': start.isoformat() }
            }, {
                'running': True
            }]
        }
        ] }
    if client == '' or client is None:
        data = collection.find(query, { "milestones": 0 })
        res = list()
        for x in data:
            temp = x
            if 'client_client' in x.keys():
                temp['client_client'] = x['client_client']
            elif 'client' in x.keys():
                temp['client_client'] = x['client']
            res.append(temp)
        print("[]]]]]]")
        print(len(res))
        return res
    else:
        query['client_client'] = client
        data = collection.find(query)
        if isinstance(data, list):
            res = list()
            for x in data:
                temp = x
                if 'client_client' in x.keys():
                    temp['client_client'] = x['client_client']
                elif 'client' in x.keys():
                    temp['client_client'] = x['client']
                res.append(temp)
            print(len(res))
            return res
        else:
            res = list()
            for x in data:
                temp = x
                if 'client_client' in x.keys():
                    temp['client_client'] = x['client_client']
                elif 'client' in x.keys():
                    temp['client_client'] = x['client']
                res.append(temp)
            print(len(res))
            return res


def get_pings(trips_list, startTime, endTime):
    start = datetime.datetime(startTime[2], startTime[1], startTime[0]) - gmt_to_ist
    end = datetime.datetime(endTime[2], endTime[1], endTime[0]) - gmt_to_ist + datetime.timedelta(1)
    database = get_database()
    collection = database['status']
    # print("tripsList", trips_list)
    print("start ", start)
    print("end ", end)
    data = collection.aggregate([{
        '$match': { 'tripId': { '$in': trips_list }, 'createdAt': { '$gte': start, '$lte': end } }
    }, {
        '$group': { '_id': '$tripId', 'pings': { '$push': '$$ROOT' } }
    }], allowDiskUse=True)
    print("pings returned")
    res = list()
    for x in data:
        res.append(x)
    return res
