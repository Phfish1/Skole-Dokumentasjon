import paramiko
import json

def server_start_ssh(server_file_path):
    server_file = open(server_file_path)
    server_json = json.load(server_file)

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(server_json["ipv4_address"], username=server_json["username"], password=server_json["password"])

    return client

