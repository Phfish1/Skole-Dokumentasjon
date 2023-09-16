import paramiko
import ssh_handler
import pty

def do_command(client, command, command_type):

    if command_type == "password":
        print("Hello")
        stdin, stdout, stderr = client.exec_command('python -c "import pty; pty.spawn("/bin/sh")"')
    else:
        print(command_type)
        stdin, stdout, stderr = client.exec_command(command)

    if stdout.channel.recv_exit_status() == 0:
        output = stdout.read().decode("utf8")
    else:
        output = stderr.read().decode("utf8")

    stdin.close()
    stdout.close()
    stderr.close()

    return output



client = ssh_handler.server_start_ssh("egne_prosjekter/scripts/server_startup_conf/server.json")
#do_command(client, "hostname")

commands = {
    "timezone": "timedatectl set-timezone Europe/Oslo",
    "repo_update": "apt update && apt upgrade -y",
    "useradd": "useradd -mG sudo -s /bin/bash phfish",
    "password": "passwd phfish",
}

for command in commands:
    output = do_command(client, commands[command], command)


