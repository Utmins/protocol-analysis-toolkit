
import socket
import json

def run_protocol_audit(args):
    if args.replay:
        replay_transcript(args.replay)
        return

    s = socket.socket()
    s.connect((args.host, args.port))

    with open(args.script) as f:
        script = f.read().splitlines()

    transcript = []

    for line in script:
        if line.startswith("send"):
            payload = line.split("send",1)[1].strip()
            s.sendall(payload.encode()+b"\n")
            data = s.recv(4096).decode()
            transcript.append({"send":payload,"recv":data})
            print(data)

    save_transcript(transcript)

def save_transcript(t):
    with open("transcript.json","w") as f:
        json.dump(t,f,indent=2)

def replay_transcript(path):
    with open(path) as f:
        t=json.load(f)
    for step in t:
        print("SEND:",step["send"])
        print("RECV:",step["recv"])
