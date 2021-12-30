import sys
class Oyun():
    def __init__(self):
        self.tahta()
        print("""

XOX Oyununa hoş geldiniz!""")
        self.oyun()
    
    def tahta(self):

        self.s1 = ["-","-","-"] # 7 8 9
        self.s2 = ["-","-","-"] # 4 5 6
        self.s3 = ["-","-","-"] # 1 2 3

        self.oyun_alani=[self.s1, self.s2, self.s3]


    def tahta_goster(self):

        print("""
        {} {} {}
        {} {} {}
        {} {} {}
        """.format(self.oyun_alani[0][0], self.oyun_alani[0][1],self.oyun_alani[0][2],self.oyun_alani[1][0],self.oyun_alani[1][1],self.oyun_alani[1][2],self.oyun_alani[2][0],self.oyun_alani[2][1],self.oyun_alani[2][2]))
    
    def kontrol_et(self, parametre):
        if parametre == "1":
            if self.oyun_alani[2][0] == "-":
                return True
            
            else:
                print("Hatalı hamle girdiniz!")
                self.oyun()
        
        elif parametre == "2":
            if self.oyun_alani[2][1] == "-":
                return True
            
            else:
                print("Hatalı hamle girdiniz!")
                self.oyun()
        
        elif parametre == "3":
            if self.oyun_alani[2][2] == "-":
                return True
            
            else:
                print("Hatalı hamle girdiniz!")
                self.oyun()
        
        elif parametre == "4":
            if self.oyun_alani[1][0] == "-":
                return True
            
            else:
                print("Hatalı hamle girdiniz!")
                self.oyun()
        
        elif parametre == "5":
            if self.oyun_alani[1][1] == "-":
                return True
            
            else:
                print("Hatalı hamle girdiniz!")
                self.oyun()
        
        elif parametre == "6":
            if self.oyun_alani[1][2] == "-":
                return True
            
            else:
                print("Hatalı hamle girdiniz!")
                self.oyun()
        
        elif parametre == "7":
            if self.oyun_alani[0][0] == "-":
                return True
            
            else:
                print("Hatalı hamle girdiniz!")
                self.oyun()
        
        elif parametre == "8":
            if self.oyun_alani[0][1] == "-":
                return True
            
            else:
                print("Hatalı hamle girdiniz!")
                self.oyun()
        
        elif parametre == "9":
            if self.oyun_alani[0][2] == "-":
                return True
            
            else:
                print("Hatalı hamle girdiniz!")
                self.oyun()
        
    def oyuncu_sirasi(self,hamle):  # X
        if hamle=="1":
            if self.kontrol_et("1") == True:
                self.oyun_alani[2][0] = "X"
            
        elif hamle == "2":
            if self.kontrol_et("2") == True:
                self.oyun_alani[2][1] = "X"
        
        elif hamle == "3":
            if self.kontrol_et("3") == True:
                self.oyun_alani[2][2] = "X"
        
        elif hamle == "4":
            if self.kontrol_et("4") == True:
                self.oyun_alani[1][0] = "X"
        
        elif hamle == "5":
            if self.kontrol_et("5") == True:
                self.oyun_alani[1][1] = "X"
        
        elif hamle == "6":
            if self.kontrol_et("6") == True:
                self.oyun_alani[1][2] = "X"
        
        elif hamle == "7":
            if self.kontrol_et("7") == True:
                self.oyun_alani[0][0] = "X"
        
        elif hamle == "8":
            if self.kontrol_et("8") == True:
                self.oyun_alani[0][1] = "X"
        
        elif hamle == "9":
            if self.kontrol_et("9") == True:
                self.oyun_alani[0][2] = "X"
        
    def minimax(self, isMaximazing):

        if self.bitti_mi() == "-1":
            return -1
        
        elif self.bitti_mi() == "1":
            return 1
        
        elif self.bitti_mi() == "0":
            return 0
        
        if isMaximazing == True:
            bestscore= -1000
           
            for i in range(0,3):
                for j in range(0,3):
                    if self.oyun_alani[i][j] == "-":
                        self.oyun_alani[i][j] = "O"
                        score=self.minimax(False)
                        self.oyun_alani[i][j] = "-"
                        if score > bestscore:  
                            bestscore = score            
            return bestscore
        
        if isMaximazing == False:
            bestscore= 1000
            
            for i in range(0,3):
                for j in range(0,3):
                    if self.oyun_alani[i][j] == "-":
                        self.oyun_alani[i][j] = "X"
                        score=self.minimax(True)
                        self.oyun_alani[i][j] = "-"
                        if score < bestscore:  
                            bestscore = score            
            return bestscore

    def bilgisayar_sirasi(self):    # O
        
        bestscore= -1000
        a=0
        b=0

        for i in range(0,3):
            for j in range(0,3):
                if self.oyun_alani[i][j] == "-":
                    self.oyun_alani[i][j] = "O"
                    score=self.minimax(False)
                    self.oyun_alani[i][j] = "-"

                    if score > bestscore:
                        bestscore = score
                        a=i
                        b=j
        self.oyun_alani[a][b]= "O"
        return

    def bitti_mi(self):

        #yatay oyuncu
        if self.oyun_alani[0][0] == self.oyun_alani[0][1] == self.oyun_alani[0][2] == "X" or self.oyun_alani[1][0] == self.oyun_alani[1][1] == self.oyun_alani[1][2] == "X" or self.oyun_alani[2][0] == self.oyun_alani[2][1] == self.oyun_alani[2][2] == "X" :
            return "-1"
                    
        #dikey oyuncu
        if self.oyun_alani[0][0] == self.oyun_alani[1][0] == self.oyun_alani[2][0] == "X" or self.oyun_alani[0][1] == self.oyun_alani[1][1] == self.oyun_alani[2][1] == "X" or self.oyun_alani[0][2] == self.oyun_alani[1][2] == self.oyun_alani[2][2] == "X" :         
            return "-1"
                 
        #çarpraz oyuncu
        if self.oyun_alani[0][0] == self.oyun_alani[1][1] == self.oyun_alani[2][2] == "X" or self.oyun_alani[0][2] == self.oyun_alani[1][1] == self.oyun_alani[2][0] == "X":           
            return "-1"
                  
        #yatay bilgisayar
        if self.oyun_alani[0][0] == self.oyun_alani[0][1] == self.oyun_alani[0][2] == "O" or self.oyun_alani[1][0] == self.oyun_alani[1][1] == self.oyun_alani[1][2] == "O" or self.oyun_alani[2][0] == self.oyun_alani[2][1] == self.oyun_alani[2][2] == "O" :          
            return "1"
                
        #dikey bilgisayar
        if self.oyun_alani[0][0] == self.oyun_alani[1][0] == self.oyun_alani[2][0] == "O" or self.oyun_alani[0][1] == self.oyun_alani[1][1] == self.oyun_alani[2][1] == "O" or self.oyun_alani[0][2] == self.oyun_alani[1][2] == self.oyun_alani[2][2] == "O" :           
            return "1"
               
        #çarpraz bilgisayar
        if self.oyun_alani[0][0] == self.oyun_alani[1][1] == self.oyun_alani[2][2] == "O" or self.oyun_alani[0][2] == self.oyun_alani[1][1] == self.oyun_alani[2][0] == "O":
            return "1"
    
        #beraberlik durumu
        beraberlik_kontrol_listesi = []
        for i in range(0,3):
            for j in range(0,3):
                if self.oyun_alani[i][j] != "-":
                    beraberlik_kontrol_listesi.append(self.oyun_alani[i][j])
        
        if len(beraberlik_kontrol_listesi) == 9:
            return "0"

        
    def bitti_mi_gercek(self):

        #yatay oyuncu
        if self.oyun_alani[0][0] == self.oyun_alani[0][1] == self.oyun_alani[0][2] == "X" or self.oyun_alani[1][0] == self.oyun_alani[1][1] == self.oyun_alani[1][2] == "X" or self.oyun_alani[2][0] == self.oyun_alani[2][1] == self.oyun_alani[2][2] == "X" :
            print("Oyuncu Kazandi!")
            self.tahta_goster()
            sys.exit()
        
        #dikey oyuncu
        if self.oyun_alani[0][0] == self.oyun_alani[1][0] == self.oyun_alani[2][0] == "X" or self.oyun_alani[0][1] == self.oyun_alani[1][1] == self.oyun_alani[2][1] == "X" or self.oyun_alani[0][2] == self.oyun_alani[1][2] == self.oyun_alani[2][2] == "X" :
            print("Oyuncu Kazandi!")
            self.tahta_goster()
            sys.exit()
        
        #çarpraz oyuncu
        if self.oyun_alani[0][0] == self.oyun_alani[1][1] == self.oyun_alani[2][2] == "X" or self.oyun_alani[0][2] == self.oyun_alani[1][1] == self.oyun_alani[2][0] == "X":
            print("Oyuncu Kazandi!")
            self.tahta_goster()
            sys.exit()
        
        #yatay bilgisayar
        if self.oyun_alani[0][0] == self.oyun_alani[0][1] == self.oyun_alani[0][2] == "O" or self.oyun_alani[1][0] == self.oyun_alani[1][1] == self.oyun_alani[1][2] == "O" or self.oyun_alani[2][0] == self.oyun_alani[2][1] == self.oyun_alani[2][2] == "O" :
            print("Bilgisayar Kazandi!")
            self.tahta_goster()
            sys.exit()
        
        #dikey bilgisayar
        if self.oyun_alani[0][0] == self.oyun_alani[1][0] == self.oyun_alani[2][0] == "O" or self.oyun_alani[0][1] == self.oyun_alani[1][1] == self.oyun_alani[2][1] == "O" or self.oyun_alani[0][2] == self.oyun_alani[1][2] == self.oyun_alani[2][2] == "O" :
            print("Bilgisayar Kazandi!")
            self.tahta_goster()
            sys.exit()
        
        #çarpraz bilgisayar
        if self.oyun_alani[0][0] == self.oyun_alani[1][1] == self.oyun_alani[2][2] == "O" or self.oyun_alani[0][2] == self.oyun_alani[1][1] == self.oyun_alani[2][0] == "O":
            print("Bilgisayar Kazandi!")
            self.tahta_goster()
            sys.exit()

        #beraberlik durumu
        beraberlik_kontrol_listesi=[]
        for i in range(0,3):
            for j in range(0,3):
                if self.oyun_alani[i][j] != "-":
                    beraberlik_kontrol_listesi.append(self.oyun_alani[i][j])
        
        if len(beraberlik_kontrol_listesi) == 9:
            print("Berabere Bitti!")
            self.tahta_goster()
            sys.exit()
   
    def oyun(self):

        while True:

            self.tahta_goster()
            
            print("Oynamak istediğiniz karenin numarasini giriniz (1-9) ...")
            hamle=input("Hamle: ")

            
            self.oyuncu_sirasi(hamle)
            self.bitti_mi_gercek()
            self.bilgisayar_sirasi()
            self.bitti_mi_gercek()

oyun=Oyun()
oyun()
    