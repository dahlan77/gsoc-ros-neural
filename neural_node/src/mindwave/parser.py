
class Parser(object):
    def __init__(self, headset, stream):
        print headset
        self.headset = headset
        self.stream = stream
        self.buffer = []

    def listen2(self):
        print "do work"

    def listen(self):
        # settings = self.stream.getSettingsDict()   

        # for i in xrange(2):
        #     settings['rtscts'] = not settings['rtscts']
        #     self.stream.applySettingsDict(settings)

        #if self.stream.isOpen():
           #while True:
        print "inside listen"
        byte1 = self.stream.read(1)
        byte2 = self.stream.read(1)                      
        print byte1

        self.buffer.append(byte1)
        self.buffer.append(byte2)
        
        print BytesStatus.CONNECT

        if byte1 == Bytes.SYNC and byte2 == Bytes.SYNC:
            print '0x%s , 0x%s ' % (byte1.encode('hex'), byte2.encode('hex'))
        
            while True:
                plength = self.stream.read() # 0-169
                self.buffer.append(plength)
                plength = ord(plength)
                if plength != 170: 
                    break
            if plength > 169: # return to while
                pass #continue        
            
            payload = self.stream.read(plength)
            checksum = 0
            checksum = sum(ord(b) for b in payload[:-1])
            checksum &= 0xff
            checksum = ~checksum & 0xff

            chksum = ord(self.stream.read())

            if checksum != chksum:
                pass

            #print 'payload ', payload.encode('hex')
            self.parser_payload(payload)

            for b in self.buffer:
                if not b == "":
                    print '0x%s, ' % b.encode('hex'),
            print ""

            self.buffer = []
        else:
            pass        
        #else:
        #    print 'no stream open'

    def parser_payload(self, payload):

        while payload:
            code, payload = payload[0], payload[1:] 
            
        
            if code >= 0x80:
                vlength, payload = payload[0], payload[1:]
                value, payload = payload[:ord(vlength)], payload[ord(vlength):]
                
                self.buffer.append(code)
                self.buffer.append(vlength)
                self.buffer.append(value)
                        
                if code == BytesStatus.RESPONSE_CONNECTED:
                    # headset found
                    # format: 0xaa 0xaa 0x04 0xd0 0x02 0x05 0x05 0x23
                    self.headset.status = Status.CONNECTED
                    self.headset.id = value 
                                            
                elif code == BytesStatus.RESPONSE_NOFOUND:  # it can be 0 or 2 bytes
                    # headset no found
                    # format: 0xaa 0xaa 0x04 0xd1 0x02 0x05 0x05 0xf2

                    self.headset.status = Status.NOFOUND
                    
                    # 0xAA 0xAA 0x02 0xD1 0x00 0xD9
                    
                elif code == BytesStatus.RESPONSE_DISCONNECTED: # dongle send 4 bytes
                    # headset found
                    # format: 0xaa 0xaa 0x04 0xd2 0x02 0x05 0x05 0x21
                    self.headset.status = Status.DISCONNECTED
                
                elif code == BytesStatus.RESPONSE_REQUESTDENIED:
                    # headset found
                    # format: 0xaa 0xaa 0x02 0xd3 0x00 0x2c
                    self.headset.status = Status.DENIED
                
                elif code == BytesStatus.RESPONSE_STANDBY: # waiting for a command the device send a byte 0x00
                    # standby/scanning mode
                    # format: 0xaa 0xaa 0x03 0xd4 0x01 0x00 0x2a
                    self.headset.status = Status.STANDBY
                     
                else:
                    #unknow multibyte
                    pass
            else: 
                # single byte there isn't vlength
                # 0-127
                value, payload = payload[0], payload[1:]
                
                self.buffer.append(value)

                if code == Bytes.POOR_SIGNAL:
                    self.headset.signal = ord(value)
                elif code == Bytes.ATTENTION:
                    self.headset.attention = ord(value)
                elif code == Bytes.MEDITATION:
                    self.headset.meditation = ord(value)
                elif code == Bytes.BLINK:
                    self.headset.blink = ord(value)
                else: 
                    pass

from common import *
