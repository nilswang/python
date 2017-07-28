'''
Created on Jul 14, 2017

@author: nilswang
'''
import socket
import sys
import select
import time
import wx
 


    
class Chatroom(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Client1", size = (400,600))
        self.panel =wx.Panel(self)
        self.text =wx.TextCtrl(self.panel, wx.ID_ANY, size = (400,300), style = wx.TE_LEFT |wx.TE_MULTILINE |wx.TE_READONLY)
        self.text2 =wx.TextCtrl(self.panel, wx.ID_ANY, pos = (0,340), size = (400,150), style = wx.TE_LEFT |wx.TE_MULTILINE)
        self.button =wx.Button(self.panel, -1, "Send", pos = (300,500), size = (40,20))
        self.button2 = wx.Button(self.panel, -1, "Close", pos =(360,500), size =(40,20))
        self.button.Bind(wx.EVT_BUTTON, self.Send)
        self.button2.Bind(wx.EVT_BUTTON, self.Close)
        self.button3 =wx.Button(self.panel, -1, "Connect", pos =(240,500), size =(40,20))
        self.button3.Bind(wx.EVT_BUTTON, self.Connect)
        self.button4 =wx.Button(self.panel, -1, "receive", pos =(180,500), size =(40,20))
        self.button4.Bind(wx.EVT_BUTTON, self.Receive)

    #try to connect server
    def Connect(self, event):
        host = "localhost"
        port = 5000
     
        s.settimeout(2)
     
        # connect to remote host
        try :
            s.connect((host, port))
        except :
            self.text.AppendText("unable to connect")
            sys.exit()
     
        self.text.AppendText('Connected to remote host. Start sending messages')

    #receive the message from other client   
    def Receive(self, event):
        data =s.recv(1024)
        self.text.AppendText(data)

    #send message to anther
    def Send(self, event):
        data =self.text2.GetValue()
        #user entered a message
        self.text.AppendText(data)
        s.send(data)
        
    #close the socket    
    def Close(self, event):
        s.close()
            


#the main function
if __name__ == "__main__":
    app = wx.PySimpleApp()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    frame = Chatroom(parent= None, id= -1)
    frame.Show()
    app.MainLoop()
