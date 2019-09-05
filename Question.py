class question:
    def __init__(self,question,AnsA,AnsB,AnsC,AnsD,Answer):
        self.question = question
        self.AnsA = AnsA
        self.AnsB = AnsB
        self.AnsC = AnsC
        self.AnsD = AnsD
        self.Answer = Answer
    def getquestion(self):
        return self.question
    def getAnsA(self):
        return self.AnsA
    def getAnsB(self):
        return self.AnsB
    def getAnsC(self):
        return self.AnsC
    def getAnsD(self):
        return self.AnsD
    def getAnswer(self):
        return self.Answer
