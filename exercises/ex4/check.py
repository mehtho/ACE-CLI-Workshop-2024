import os

expected = {'all4me.sh': '0o700', 'pubkey.pub': '0o644', 'private.key': '0o600'}

def check_permissions(filename):
    try:
        permissions = oct(os.stat(filename).st_mode & 0o777)
        if permissions == expected[filename]:
            print('Permissions for', filename, 'ok:', permissions)
        else:
            print('Permissions for', filename, 'not ok:', permissions)
    except FileNotFoundError:
        return f"{filename} not found."

for file in expected:
    check_permissions(file)
