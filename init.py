
import commands,os,configparser,smtplib

class trackServer():
	
	def __init__(self):
		a = open("config.ini","a")
		os.system("chmod 0777 config.ini")
		a.close()

	def init(self):
		content="Track Server\n"
		menu= raw_input(content)
		print menu

	def diskSpace(self):
		space = commands.getstatusoutput("df -h | awk '{print $2}'")
		space = space[1].split("\n")
		space.pop(0)

		partition = commands.getstatusoutput("df -h | awk '{print $1}'")
		partition = partition[1].split("\n")
		partition.pop(0)

		percentaje = commands.getstatusoutput("df -h | awk '{print $5}'")
		percentaje = percentaje[1].split("\n")
		percentaje.pop(0)
		print "Size configuration "+self.loadConfiguration()

		for ind in range(len(space)):
			
			if space[ind][len(space[ind])-1]=='G' and float(self.loadConfiguration()) <  float(percentaje[ind][:len(percentaje[ind])-1]):
				print "Alerta envio mensaje usado "+space[ind] + " particion " + partition[ind] + " " + percentaje[ind]

	def sendMessage(self):
		#server = smtplib.SMTP('smtp.gmail.com:587')
		#server.starttls()

		server.login("","")
		server.sendmail("jorke8710@gmail.com", "jpinedom@hotmail.com", "prueba de mensaje")
		server.quit()

			
	def loadConfiguration(self):
		config = configparser.ConfigParser()
		config.read('config.ini')
		return config.get("files","size") 


obj = trackServer()
obj.diskSpace()
#obj.sendMessage()

		