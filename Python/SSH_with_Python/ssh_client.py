import paramiko
import psutil


def connect_to_ssh_client(ssh_client, linux_ip, user, password):
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(f"{linux_ip}", username=f'{user}', password=f'{password}')
        print("Success")
        return True
    except Exception as e:
        print(e)
    return False


def execute_command_on_linux(ssh_client, command):
    try:
        stdin, stdout, stderror = ssh_client.exec_command(f"{command}", get_pty=True)
        process_pid = int(stdout.readline())
        print(process_pid)
        if stdout.channel.recv_exit_status() != 0:
            print("Not executed")
            return False
    except Exception as error:
        print(f"{error}")
    return True


def check_pid_exists_on_machine(ssh_client, platform, machine, pid, user, password):
    if platform == "Windows":
        return psutil.pid_exists(pid)
    elif platform == "Linux":
        if ssh_client.get_transport() is not None:
            if ssh_client.get_transport().is_active():
                return check_process_pid_exists_on_linux(machine, pid, ssh_client)
            else:
                conn_success = connect_to_ssh_client(ssh_client,
                                                     machine, user, password)
                if conn_success:
                    return check_process_pid_exists_on_linux(machine, pid, ssh_client)
                else:
                    return False
        return False
    return False


def check_process_pid_exists_on_linux(machine, pid, ssh_client):
    try:
        stdin, stdout, stderr = ssh_client.exec_command(f"ps -p {pid}")
        if len(stdout.readlines()) < 2:
            return False
        else:
            return True
    except OSError as e:
        print(f"Failed to get process pid {pid} on linux machine {machine}. Reason: {e}")
        return False

