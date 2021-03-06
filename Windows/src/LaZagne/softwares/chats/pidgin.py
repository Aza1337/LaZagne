import WConio
import xml.etree.cElementTree as ET
import os
from config.constant import *
from config.write_output import print_output, print_debug
from config.header import Header

class Pidgin():
	def retrieve_password(self):
		# print title
		Header().title_debug('Pidgin')
		
		if 'APPDATA' in os.environ:
			directory = os.environ['APPDATA'] + '\.purple'
			path = os.path.join(directory, 'accounts.xml')
		else:
			print_debug('ERROR', 'The APPDATA environment variable is not defined.')
			return
		
		if os.path.exists(path):
			tree = ET.ElementTree(file=path)
			
			root = tree.getroot()
			accounts = root.getchildren()
			pwdFound = []
			for a in accounts:
				values = {}
				aa = a.getchildren()
				noPass = True

				for tag in aa:
					cpt = 0
					if tag.tag == 'name':
						cpt = 1
						values['Login'] = tag.text
					
					if tag.tag == 'password':
						values['Password'] = tag.text
						noPass = False
					
				if noPass == False:
					pwdFound.append(values)
				
			# print the results
			print_output("Pidgin", pwdFound)
		else:
			print_debug('INFO', 'Pidgin not installed.')
			
