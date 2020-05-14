import csv
import ipaddress as ip_lib


class Packet():
    
    def __init__(self, direction_csv: str=None, protocol_csv: str=None, port_csv: int=None, ip_adress_csv: str=None): 
        self.direction_csv = direction_csv
        self.protocol_csv = protocol_csv
        self.port_csv = port_csv
        self.ip_adress_csv = ip_adress_csv

    def is_direction_valid(self, direction):
        if direction == self.direction_csv: 
            return True
        return False # blocked

    def is_protocol_valid(self, protocol):
        if protocol == self.protocol_csv:
            return True
        return False # blocked

    def is_port_valid(self, port):
        if str(port) == self.port_csv:
            return True
        elif "-" in self.port_csv:
            # make port range into two port items in a list
            port_split = self.port_csv.split("-")
            # using the two items in a list, we create a range and
            # add +1 because we want the range to be inclusive
            port_range = range(int(port_split[0]), int(port_split[1])+1)
            # check if port is in range with the rule
            if int(port) in port_range:
                return True
        return False # blocked

    def is_ip_adress_valid(self, ip_adress):
        # quick check if the given ip is the same as the rule
        if ip_adress == self.ip_adress_csv:
            return True
        elif "-" in self.ip_adress_csv:
            # split ip range string into two ip items 
            ip_split = self.ip_adress_csv.split("-")
            start_ip = ip_lib.IPv4Address(ip_split[0])
            end_ip = ip_lib.IPv4Address(ip_split[1])
            # iterate through all ips within the range. If a match is found, return
            # so no need to traverse the rest
            for ip in range(int(start_ip), int(end_ip)+1):
                if ip_adress == str(ip_lib.IPv4Address(ip)):
                    return True
        return False # blocked

class Firewall():

    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path

    def accept_packet(self, direction: str, protocol: str, port: str, ip_adress: str) -> bool:
        # parse csv 
        packet = Packet()
        with open(self.csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for rule in csv_reader:
                packet.__init__(direction_csv=rule[0], protocol_csv=rule[1], port_csv=rule[2], ip_adress_csv=rule[3]) # reset packet instance for reading multiple packets
                if packet.is_direction_valid(direction) is packet.is_protocol_valid(protocol) is packet.is_port_valid(port) is packet.is_ip_adress_valid(ip_adress) is True:
                    return True
            return False # packet doesn't match any rules...blocked!
