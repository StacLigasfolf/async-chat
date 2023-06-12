from ipaddress import ip_address
from host_ping import host_ping


def host_range_ping():
    while True:
        start_ip = input('Введите адрес: ')
        try:
            last = int(start_ip.split('.')[3])
            break
        except Exception as e:
            print(e)
    while True:
        end_ip = input('Сколько адресов проверить?: ')
        if not end_ip.isnumeric():
            print('Введите количество: ')
        else:
            if (last + int(end_ip)) > 254:
                print(f"максимальное число хостов для проверки: {254 - last}")
            else:
                break
    host_list = []
    [host_list.append(str(ip_address(start_ip) + x)) for x in range(int(end_ip))]
    return host_ping(host_list)


if __name__ == "__main__":
    host_range_ping()
