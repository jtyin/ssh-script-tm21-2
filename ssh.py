import paramiko

def ssh_command(host, port, username, password, command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port, username, password)
        print(f"terhubung ke {host}")
    
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        print(f"hasil perintah: \n{output}")
    
        client.close()
    except Exception as e:
        print(f"terjadi kesalahan: {e}")

ssh_command("ip",22,"user","pwd","command")
