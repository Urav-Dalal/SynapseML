class Titandex:
    def __init__(self,Name,Height,Strength,winningstreak):
        self.Name=Name
        self.Height=Height
        self.Strength=Strength
        self.winningstreak=winningstreak

    def TitanvsScout(self):
        n=int(input("enter number of fights VS scouts "))

        for i in range(n):
            scoutName=input("enter scout name ")
            scoutStrength=int(input("enter scout strength "))

            if(self.Strength>scoutStrength):

                print("titan "+self.Name+" is the winner")
                self.winningstreak=self.winningstreak+1
                print("titan "+self.Name+" winningstreak is ",str(self.winningstreak))
            elif(self.Strength==scoutStrength):

                print("it is a draw")
                self.winningstreak=0
                print("titan "+self.Name + " winning streak reset to "+str(self.winningstreak))

            else:

                print("scout "+scoutName+" is the winner")
                self.winningstreak=0
                print("titan "+self.Name+" winning streak reset to "+str(self.winningstreak))

    def Titanvstitan(self):
        p=int(input("enter number of fights VS titans "))

        for j in range(p):
            titanName=input("enter titan name ")
            titanStrength = int(input("enter titan strength "))

            if(self.Name==titanName):
                print(self.Name+" cant fight itself")
            elif(self.Strength>titanStrength):
                self.winningstreak = self.winningstreak + 1
                print("titan "+self.Name+" is the winner")
                print("titan "+self.Name+" winning streak is "+str(self.winningstreak))
            elif(titanStrength>self.Strength):
                print("titan "+titanName+" is the winner")
                self.winningstreak=0
                print(self.Name+" winning streak is reset to "+str(self.winningstreak))
            else:
                print("it is a draw")
                self.winningstreak=0
                print("titan "+self.Name+" winning streak is reset to "+str(self.winningstreak))



Name=input("enter titan name ")
Height=int(input("enter titan height "))
Strength=int(input("enter titan strength "))
winningstreak=0
titan=Titandex(Name,Height,Strength,winningstreak)
titan.TitanvsScout()
titan.Titanvstitan()
