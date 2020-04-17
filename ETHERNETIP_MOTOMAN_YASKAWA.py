from cpppo.server.enip.get_attribute import proxy_simple

via = proxy_simple('192.168.255.1')
if via is True:
    result, = via.read([('@0x78/2701/1/0x10=(USINT)0','@0x78/2701/1/0x10')],1)
    print(result)
print(via)