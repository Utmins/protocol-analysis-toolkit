
import json

def save_transcript(data,path="transcript.json"):
    with open(path,"w") as f:
        json.dump(data,f,indent=2)
