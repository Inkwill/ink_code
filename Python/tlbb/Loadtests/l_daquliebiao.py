from locust import HttpLocust, TaskSet, task


class MyTaskSet(TaskSet):
    @task(2)
    def index(self):
        #res = self.client.get("/serverlist.php?CurrAreaID=12&CurrIOSGrayVersions=101|2|102|2|103|5&CurrGrayVersions=101|1102|2103|3&CurrIOSAuditVersion=2&UserOpenID=bbsbbs")
        res = self.client.get("/serverlist.php?CurrAreaID=1&CurrIOSGrayVersions=101|5|102|2|103|5&CurrGrayVersions=101|1102|2103|3&CurrIOSAuditVersion=2&UserOpenID=test3")
        #res = self.client.get("/serverlist.php?CurrAreaID=1&CurrIOSGrayVersions=101|2|102|2|103|5&CurrGrayVersions=101|1102|2103|3&CurrIOSAuditVersion=2&UserOpenID=test3")
        #print res
        #print res.headers
        #print res.text

    '''
    @task(1)
    def about(self):
        self.client.get("")
    '''
        
class MyLocust(HttpLocust):
    task_set = MyTaskSet
    #host = "http://221.228.206.25:20001"
    #host = "http://221.228.196.153:20001"
    #host = "http://221.228.196.154:20001"
    host = "http://123.206.205.229:20001"

    min_wait = 995
    max_wait = 1100
