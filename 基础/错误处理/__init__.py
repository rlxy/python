# import calendar
# cal = calendar.calendar()
# print(cal)



class mode(object):
	def __init__(self):
		self.list1=[]
	def push(self,number):
		self.list1.append(number)
	def if_metry(self):
		return self.list1 ==[]
	def opp(self):
		return self.list1.pop()
	def zd(self):
		if self.list1:
			return self.list1[-1]
		else:
			return None
	def dir(self):
		if self.if_metry():
			return None
		else:
			return self.list1
	def len(self):
		return len(self.list1)
if __name__=="main":
	mode=mode()
	mode.push(1)
	mode.push(2)
	mode.push(3)
	mode.if_metry()
	mode.opp()
	mode.zd()
	mode.dir()
	mode.len()

