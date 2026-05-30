# 2026-05-30 21:21:07 by RouterOS 7.20.8
# software id = G353-EXPG
#
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no
/ip address
add address=172.16.21.2/26 interface=ether1 network=172.16.21.0
/ip route
add gateway=172.16.21.1