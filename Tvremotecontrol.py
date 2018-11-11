import random
import msvcrt
class Tvremotecontrol():
    def __init__(self,tvstatus="Close",tvvoice=0,channellist=["BBC"],channel="BBC"):
        print("Creatig Tv Remote Control")
        self.tvstatus=tvstatus
        self.tvvoice=tvvoice
        self.channellist=channellist
        self.channel=channel
    def increase_decrease_voice(self):
        while True:
            button=input("For increase TV voice level press '>' , For decrease press '<'")
            if(button==">"):
                if(self.tvvoice!=32):
                    self.tvvoice+=1
                    print("TV voice level is:",self.tvvoice)
            elif(button=="<"):
                if(self.tvvoice!=0):
                    self.tvvoice-=1
                    print("TV voice level is:",self.tvvoice)
            else:
                print("You have entered wrong and now TV voice level is:",self.tvvoice)
                break
    def close_tv(self):
        print("Closing the TV")
        self.tvstatus="Close"
    def open_tv(self):
        print("Opening the TV")
        self.tvstatus="Open"
    def __str__(self):
        return "Tv Status:{}\nTv Voice Level:{}\nTV Channel List:{}\nChannel:{}\n".format(self.tvstatus,self.tvvoice,self.channellist,self.channel)
    def __len__(self):
        return len(self.channellist)
    def random_channel(self):
        randomchannel=random.randint(0,len(self.channellist)-1)
        self.channel=self.channellist[randomchannel]
        print("Now Channel is:",self.channel)
    def add_channel(self,channel):
        print("Channel added:",channel)
        self.channellist.append(channel)


remotecontrol=Tvremotecontrol()

print("""*******************
Television Remote Control
Operations:
1-Open The Television
2-Close The Television
3-Give İnformation About The Television
4-Learn Channel Number
5-Add Channel
6-Pass To Random Channel
7-İncrease TV Voice Level or Decrease TV Voice Level
For Exit press "q"
*******************""")

while True:
    operation=input("Select Operation:")
    if(operation=="q"):
        print("Exiting Program")
        break
    if (operation=="1"):
        remotecontrol.open_tv()
    elif (operation=="2"):
        remotecontrol.close_tv()
    elif (operation=="3"):
        print(remotecontrol)
    elif (operation=="4"):
        print("Channel Nember is :",len(remotecontrol))
    elif (operation == "5"):
        channels=input("Enter The Channel you want to add:")
        adds=channels.split(",")
        for i in adds:
            remotecontrol.add_channel(i)
        print("Add Channel is Complete.")
    elif( operation == "6"):
        remotecontrol.random_channel()
    elif (operation == "7"):
        remotecontrol.increase_decrease_voice()
    else:
        print("You Have Entered Wrong")
