from intuginehelper import intudb


def main():
    db = intudb.get_database()
    collection = db['trips']
    all_trip_ids = collection.find({ }, {
        '_id': 1
    })
    cnt = 0
    for trip in all_trip_ids:
        # print(trips)
        """
        data = collection.aggregate([
            { "$match": { '_id': trip['_id'] } },
            { '$group': { '_id': '$tripId', 'result': { '$push': '$$ROOT' } } }
        ], allowDiskUse=True)
        """
        # res = list()
        try:
            print(trip['_id'])
            data = collection.find({ '_id': trip['_id'] }, { "milestones": 0 })
            for d in data:
                print(d)
                # res.append(d)
        except Exception as e:
            cnt += 1
            # print(e)
            print()
            print(trip['_id'])
            print()
            debug_file.write(str(trip['_id']) + "\n")
        # print(res)
    print("[ERR = ] ", cnt)


if __name__ == '__main__':
    debug_file = open('debug.txt', 'a')
    main()
