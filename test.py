#coding:utf-8
#

from wxbot import *
import socket
import time

HOST = 'hayoou.com'
PORT = 9999

if 0:
            socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket2.connect((HOST, PORT))
            socket2.send(('Ê¾Ýà'))
            data = socket2.recv(1024)
            print(data)
            socket2.close()

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        #print(msg)
        data = ''
        if (msg['msg_type_id'] == 3 or msg['msg_type_id'] == 4 or  msg['msg_type_id'] == 5 ) and msg['content']['type'] == 0:
            socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket2.connect((HOST, PORT))
            #cmd = raw_input("Please input msg:")
            #print(msg['content'])
            if  msg['msg_type_id'] == 5 :
              time.sleep(0.2)
            inputt = msg['content']['data'].replace(' ','').encode('utf-8')[0:48]
            socket2.send(inputt)
            data = socket2.recv(1024).replace(' ','')
            socket2.close()
            #print(msg['user']['id'])
            #print(1)
            if data=='' :
               data = ".."
            if msg['msg_type_id'] == 5 and len(msg['content']['data'].encode('utf-8'))==121:
               print('wait xiaobin')

               return
            #print(len(msg['content']['data'].encode('utf-8')))
            self.send_msg_by_uid(data  , msg['user']['id'])
            if  msg['msg_type_id'] == 5 :# and msg['user']['id']=='@c39318acb413215e3ef6acb7ce33bbcf' :
              with open('test.txt','a+') as f:
               f.write("\n<br>----------\n<br>Q:")
               f.write(msg['content']['data'].encode('utf-8'))
               f.write("\n<br>A:")
               f.write(data)
               
            #self.send_img_msg_by_uid("img/1.png", msg['user']['id'])
            #self.send_file_msg_by_uid("img/1.png", msg['user']['id'])

        #photo and voice
        if msg['content']['type'] == 3 or msg['content']['type'] == 4:
           data='不懂'
           self.send_msg_by_uid(data , msg['user']['id'])
        
        return data


'''
    def schedule(self):
        self.send_msg(u'å äI', u'æKèU')
        time.sleep(1)
'''


def main():
    bot = MyWXBot()
#    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()

