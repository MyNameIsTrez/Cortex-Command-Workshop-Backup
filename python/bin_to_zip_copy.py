import os, shutil, zipfile

from pathlib import Path

from python import get_project_path


def bin_to_zip_copy(settings):
	for mod_bin_parent_dir_name in os.listdir(settings["game_mods_path"]):
		mod_bin_parent_dir_path = Path(settings["game_mods_path"]) / mod_bin_parent_dir_name

		# There's always a single .bin in mod_bin_parent_dir_name
		mod_bin_file_name = os.listdir(mod_bin_parent_dir_path)[0]

		mod_bin_path = mod_bin_parent_dir_path / mod_bin_file_name
		mod_zip_path = (get_project_path.get_project_path() / "output_zips" / mod_bin_file_name).with_suffix(".zip")

		shutil.copyfile(mod_bin_path, mod_zip_path)

		give_zip_proper_name(mod_zip_path)


def give_zip_proper_name(mod_zip_path):
	with zipfile.ZipFile(mod_zip_path) as zip:
		# There's always a single mod with a proper name in mod_zip_path
		real_mod_name = list(zipfile.Path(zip).iterdir())[0]

	try:
		mod_zip_path.rename(Path(mod_zip_path.parent, f"{real_mod_name.name}.zip"))
	except FileExistsError: # Renaming can fail when two mods have the same name
		pass
