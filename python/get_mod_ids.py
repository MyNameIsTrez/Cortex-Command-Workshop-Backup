import vdf


def get_mod_ids(settings):
	mod_ids = []

	with open(settings["vdf_path"]) as f:
		data = vdf.parse(f)["subscribedfiles"]

		for v in data.values():
			if isinstance(v, dict):
				mod_ids.append(int(v["publishedfileid"]))

	return mod_ids
