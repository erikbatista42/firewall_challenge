from firewall import Firewall, Packet
import unittest

class FirewallTest(unittest.TestCase):

    def test_tcp(self):
        path = "rules.csv"
        firewall = Firewall(path)
        assert firewall.accept_packet("inbound", "tcp", 80, "192.168.1.2") == True
        assert firewall.accept_packet("outbound", "tcp", 10234, "192.168.10.11") == True
        assert firewall.accept_packet("inbound", "tcp", 81, "192.168.1.2") == False
        assert firewall.accept_packet("outbound", "tcp", 20000, "192.168.10.11") == True
        assert firewall.accept_packet("inbound", "tcp", 800, "192.168.1.2") == False
        
    def test_udp(self):
        path = "rules.csv"
        firewall = Firewall(path)
        assert firewall.accept_packet("inbound", "udp", 53, "192.168.2.1") == True
        assert firewall.accept_packet("inbound", "udp", 24, "52.12.48.92") == False
        assert firewall.accept_packet("inbound", "udp", 57, "192.168.1.1") == False
        assert firewall.accept_packet("outbound", "udp", 1000, "52.12.48.92") == True
        assert firewall.accept_packet("outbound", "udp", 1500, "52.12.48.93") == False

if __name__ == '__main__':
    unittest.main()
