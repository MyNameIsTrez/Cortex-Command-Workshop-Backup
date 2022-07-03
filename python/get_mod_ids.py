import json


with open("209670_subscriptions.vdf") as f:
	data = json.load(f)

	ids = []

	for v in data.values():
		ids.append(int(v["publishedfileid"]))

	print(ids)
	with open("../mod_ids.json", "w") as of:
		of.write(json.dumps(ids))
