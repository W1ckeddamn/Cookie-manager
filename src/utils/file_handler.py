import os

def create_profile_directory(profile_name):
    profile_dir = f"profiles/{profile_name}"
    os.makedirs(profile_dir, exist_ok=True)
    return profile_dir
