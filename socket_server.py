#!/usr/bin/env Python

import SocketServer

class EchoHandler(SocketServer.BaseRequestHandler):

	def handler(self):
		print "got connection free :",self.client_address
		data = 'dummy'

		while len(data)
			data=self.request.recv(1024)
			print data 
			self.request.send(data)

		print "client left"


serverAddr = ("0.0.0.0",9000)

server = SocketServer.TCPServer(serverAddr, EchoHandler)

server.serve_forever()


