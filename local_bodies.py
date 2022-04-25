from datetime import datetime
import json
from MySQLdb import _mysql
db = _mysql.connect("localhost","root","Anonymous@123!@#","election_new")
# Opening JSON file
f = open('local_bodies.json')
data = json.load(f)
 
for provinces in data:
    # print(provinces)
    del data[provinces]['name']
    for districts in data[provinces]:
        # pass
        # print(districts)
        for district in data[provinces][districts]:
            for x in district['locations'][0]:
                x['created_at'] = datetime.now()
                x['updated_at'] = datetime.now()
                print("District ID: %s"%(district["id"]))
                print("name_en : %s"%(x["nepali_name"]))
                print("District Eng Name: %s"%(x["english_name"]))
                print("\n------\n")
                query="""insert into election_new.ys_local_bodies (district_id,name_en,name_np,deleted,created_at,updated_at) values ('%s','%s','%s','%s','%s','%s');""" %(district["id"],x["english_name"],x["nepali_name"],0,x["created_at"],x["updated_at"])
                db.query(query)
            
# Closing file
f.close()