from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(list_ip_addresses, timeout=500, requests=1):
    result = {'Доступные узлы': '', 'Недоступные узлы': ''}
    for address in list_ip_addresses:
        try:
            address = ip_address(address)
        except ValueError:
            pass
        proc = Popen(f"ping {address} -w {timeout} -n {requests}", shell=False, stdout=PIPE)
        proc.wait()

        if proc.returncode == 0:
            result['Доступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел доступен'
        else:
            result['Недоступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел недоступен'
        print(res_string)
    return result


if __name__ == "__main__":
    ip_addresses = ['github.com', '127.0.0.1:7777', '1.1.1.1', '192.168.0.100 ']
    host_ping(ip_addresses)
