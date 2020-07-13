import json
import hashlib


with open('rank.json', 'r') as f:
    db = json.load(f)

name = 'cergmin'
ip = '0.0.0.0'
score = 300

for i in db:
    if i['name'] == name:
        if i['ip'] == ip:
            if i['score'] < score:
                i['score'] = score
            with open('rank.json', 'a') as f:
	            json.dump(db, f)
            return 'ok'
        return 'wrong_ip'

db.append({
    'name': name,
    'ip': ip,
    'score': score,
    'note': ''
})

with open('rank.json', 'a') as f:
	json.dump(db, f)


hashlib.sha1(b'save_egor' + str(len(db)) + str(name) + str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))).hexdigest()