import pandas as pd
import json
  
# Opening JSON fie
f = open('demoq.txt')

objectsList = []
print("Started Reading JSON file which contains multiple JSON document")
with open('demoq.txt') as f:
    for jsonObj in f:
        objectDict = json.loads(jsonObj)
        if(objectDict["category"]=="tracker"):
            objectsList.append(objectDict)

temp = pd.DataFrame()


print("Adding each JSON Decoded Object in Dataframe")
for object in objectsList:
    obj=object["values"]['frame']
    dict={
    
    'timestamp':[obj['timestamp']],

    'is_fix':obj['fix'],
    
    'gaze_smooth_x':obj['avg']['x'],
    'gaze_smooth_y':obj['avg']['y'],
    'gaze_raw_x':obj['raw']['x'],
    'gaze_raw_y':obj['raw']['y'],

    'lefteye_smooth_x':obj['lefteye']['avg']['x'],
    'lefteye_smooth_y':obj['lefteye']['avg']['y'],
    'lefteye_raw_x':obj['lefteye']['raw']['x'],
    'lefteye_raw_y':obj['lefteye']['raw']['y'],
    'lefteye_psize':obj['lefteye']['psize'],
    'lefteye_p_x':obj['lefteye']['pcenter']['x'],
    'lefteye_p_y':obj['lefteye']['pcenter']['y'],

    'righteye_smooth_x':obj['righteye']['avg']['x'],
    'righteye_smooth_y':obj['righteye']['avg']['y'],
    'righteye_raw_x':obj['righteye']['raw']['x'],
    'righteye_raw_y':obj['righteye']['raw']['y'],
    'righteye_psize':obj['righteye']['psize'],
    'righteye_p_x':obj['righteye']['pcenter']['x'],
    'righteye_p_y':obj['righteye']['pcenter']['y'],

    }
    df = pd.DataFrame(dict)
    temp=pd.concat([temp,df],ignore_index=True)
    
temp.to_csv('file.csv')
