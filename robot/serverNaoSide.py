import SocketServer

class GnubiquityServer(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def requestDataParser(self):
        data = self.data.split("\n")
        data = data[11]
        data = data.split("&")
        result = {}
        for i in range(len(data)):
            elem = (data[i]).split("=")
            result[elem[0]] = elem[1]
        return result

    def requestParser(self):
        print self.data
        req = self.data.replace("\r", "")
        req = req.split("\n");
        head = req[0]
        head = head.split("/")
        result = {}
        result["method"] = head[0].strip(" ")
        result["protocol"] = head[1].strip(" ")
        result["version"] = head[2].strip(" ")
        result["client"] = self.client_address[0]+":"+str(self.client_address[1])
        result["host"] = (req[1].strip("Host:")).strip(" ")
        result["connectionType"] = (req[2].strip("Connection:")).strip(" ")
        result["userAgent"] = (req[7].strip("User-Agent:")).strip(" ")
        result["data"] = self.requestDataParser()
        print "method : "+result["method"]
        print "host : "+result["host"]
        print "client : "+result["client"]
        print "data : "+str(result["data"])
        return result

    def run(self):
    	runServer();
		
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        #print self.data
        parsedReq = self.requestParser()
        newData = parsedReq["data"]
        newData["citron"] = int(newData["citron"])
        newData["citrouille"] = int(newData["citrouille"])
        newData["melon"] = int(newData["melon"])
        newData["citron"] += 1
        newData["citrouille"] += 1
        newData["melon"] += 1
        self.data = str(newData)
        self.request.sendall(self.data)

#if __name__ == "__main__":
def runServer():
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), GnubiquityServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

runServer()
