import os
import json
import pandas as pd

def read_all_json_files(JSON_ROOT):
    df = pd.DataFrame()
    for filename in os.listdir(JSON_ROOT):
        with open(os.path.join(JSON_ROOT, filename), 'r') as file:
            json_data = json.load(file)
            df_2 = pd.json_normalize(json_data['results'])
            df_2['source'] = str(filename)
            df = pd.concat([df,df_2])
    return df