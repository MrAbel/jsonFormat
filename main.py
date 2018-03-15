# -*- coding utf-8 -*-
import wx 
import json
import mainFrame  

class MainWindow(mainFrame.MainFrame): 
	def __init__(self,parent): 
		mainFrame.MainFrame.__init__(self,parent)  
		
	def check_data(self, data):
		if data == "":
			return False
		return True
	
	def get_data(self):
		src_data = self.m_src_data_tc.GetValue()
		
		if self.check_data(src_data):
			try:
				data_obj = json.loads(src_data)
			except (Exception) as e:
				self.print_data('json格式错误，格式化失败！！！')
				return None				
		else:
			return None
		
		return data_obj
	
	def format_data(self, src_data):
		return json.dumps(src_data, indent=4)
	
	def print_data(self, dst_data):
		self.m_dst_data_tc.SetValue(dst_data)
	
	def transfer(self):
		src_data = self.get_data()
		
		if src_data == None:
			return
		
		dst_data = self.format_data(src_data)
		self.print_data(dst_data)
	
	def m_transfer_btnOnLeftDown( self, event ):
		self.transfer()
		event.Skip()
		
app = wx.App(False) 
frame = MainWindow(None) 
frame.Show(True) 
# 主循环
app.MainLoop()