import os, shutil

from pathlib import Path

from python import get_project_path


def bin_to_zip_copy(settings):
	for mod_bin_parent_dir_name in os.listdir(settings["game_mods_path"]):
		mod_bin_parent_dir_path = Path(settings["game_mods_path"]) / mod_bin_parent_dir_name

		# There's always a single .bin in mod_bin_parent_dir_name, but the name will be unknown
		for mod_bin_file_name in os.listdir(mod_bin_parent_dir_path):
			mod_bin_path = mod_bin_parent_dir_path / mod_bin_file_name
			mod_zip_path = (get_project_path.get_project_path() / "output_zips" / mod_bin_file_name).with_suffix(".zip")

			shutil.copyfile(mod_bin_path, mod_zip_path)
