import json
from numpy import source
import pandas as pd


df=pd.read_csv('mvf_user.csv')

mvf_user=df.groupby(['user_id','email_id']).apply(lambda x:x.to_json(orient='records')).reset_index().rename(columns={0:'status'})
mvf_json = json.loads(mvf_user.to_json(orient ='records'))


with open("mvf_user.json" , "w") as f:
    count=0
    f.write("{")
    f.write('"data":[')
    #f.write("{")
    for obj in mvf_json:
        obj["status"] = json.loads(obj["status"])
        json.dump(obj, f, indent=4)
        count=count+1
        print(count)
        if count<=42:
           f.write(",")

    
    f.write("]")
    f.write("}")














                    
