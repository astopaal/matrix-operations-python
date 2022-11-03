class DogrusalCebir():

    matrix = []
    gecici = []

    def olusturulamadi():
        return "Couldn't create matrix!"

    def hata():
        return "An error occured!"

    # asagidaki function parametreden gelen satir değerinden önceki ve sonraki satırları seçer 
    # yani satir degeri haricindeki satirları alır
    # ardından bu satırlar içinden list comp ile parametreden gelen sutun degerinden onceki ve sonraki sutunları seçer. bu sekilde minor matrisi geri döndürür
    def minorHesapla(matris,satir,sutun):
        return [row[:sutun] + row[sutun+1:] for row in (matris[:satir] + matris[satir+1:])] 

    def matrisolustur(): #parametre olarak aldigi satir sayisina gore gecici matrisini sekillendirir
        try:

            print("Enter matrix rows with (commas) between elements")
            print("Press enter after each line")

            for i in range(3):
                row = list(map(int, input().split(","))) #girilen inputu virgülleri baz alarak ayırır bu elemanları map ile int'e çevirir ve liste oluşturur
                DogrusalCebir.gecici.append(row)

            print(f"Matrix created : {DogrusalCebir.gecici}")
        
            return DogrusalCebir.gecici

        except Exception as e:

            print(f"an error occured, error message : {e}")
            DogrusalCebir.olusturulamadi()

    def sabitlecarp(carpan,matris): #parametre aldığı sabit sayıyla matrisi çarpar
        try:

            for i in range(3):
                for j in range(3):
                    matris[i][j] *= carpan
            
            return matris

        except:
            DogrusalCebir.hata()

    def matrisiCikar():

        print("Create the matrix you want to subtract: \n")
        print("Number of rows and columns must be the same.")
        DogrusalCebir.matrisolustur()
        for i in range(len(DogrusalCebir.matrix)):
            for j in range(len(DogrusalCebir.matrix)):
                DogrusalCebir.gecici[i][j] -= DogrusalCebir.matrix[i][j] 

        return DogrusalCebir.matrix

    def matristenCikar(a,b):

        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] -= b[i][j]

        return a

    def matrisleTopla():
        print("Create the matrix you want to aggregate: \n")
        print("Number of rows and columns must be the same.")
        DogrusalCebir.matrisolustur()
        for i in range(len(DogrusalCebir.matrix)):
            for j in range(len(DogrusalCebir.matrix)):
                DogrusalCebir.matrix[i][j] += DogrusalCebir.gecici[i][j]

        return DogrusalCebir.matrix

    def sabitletopla(sabit,matris): #parametre aldığı sabit sayıyıyla matris elemanlarını toplar
        
        try:

            for i in range(3):
                for j in range(3):
                    matris[i][j] += sabit
            return matris

        except:

            DogrusalCebir.hata()
    
    def sabiticikar(matris,cikan): #parametre aldığı sabit sayıyı matristen çıkarır 
        try:

            for i in range(3):
                for j in range(3):
                    matris[i][j] -= cikan

        except:

            DogrusalCebir.hata()

    def sabittenCikar(eksilen,matris): #parametre aldığı sabit SAYIDAN MATRİSİ çıkarır
        try:

            for i in range(3):
                for j in range(3):
                        matris[i][j] = eksilen - matris[i][j]
        
        except:
        
           DogrusalCebir.hata()

    def matrisleCarp():
    
        print("Create the matrix you want to multiply, the number of rows must be the same for the matrices to be multiplied.")
        try:
            rows = int(input("Enter number of rows "))
        
            if rows == len(DogrusalCebir.matrix):
                DogrusalCebir.matrisolustur()
        
            else:
                print(f"The number of rows of the matrix must be : {len(DogrusalCebir.matrix)}!")
        
        except Exception as e:
        
            DogrusalCebir.hata()
            DogrusalCebir.olusturulamadi()
            print(e)

        sonuc = [[0 for x in range(len(DogrusalCebir.gecici[0]))] for y in range(len(DogrusalCebir.matrix))] 

        try:

            for x in range(len(DogrusalCebir.matrix)):
                for y in range(len(DogrusalCebir.gecici[0])):
                    for z in range(len(DogrusalCebir.gecici)):
                        sonuc[x][y] += DogrusalCebir.matrix[x][z] * DogrusalCebir.gecici[z][y]

            print("Multiplication complete, matrix created.")
            print("Result : ")
            print(sonuc)

        except:

            DogrusalCebir.hata()
            DogrusalCebir.olusturulamadi()
            print(e)


    def matrisleriCarp(birinci, ikinci):

        try:

            sonuc = [[0 for x in range(len(ikinci[0]))] for y in range(len(birinci))] 

            for x in range(len(birinci)):
                for y in range(len(ikinci[0])):
                    for z in range(len(ikinci)):
                        sonuc[x][y] += birinci[x][z] * ikinci[z][y]

            return sonuc

        except Exception as e:

            DogrusalCebir.hata()
            DogrusalCebir.olusturulamadi()
            print(e)

    def involutifMi(matris):
    
        birim = [[1,0,0],[0,1,0],[0,0,1]]

        if DogrusalCebir.matrisleriCarp(matris,matris) == birim:
            return True

        else: 
            return False


    def determinantHesapla(matris):


        if len(matris) == 2: #eğer 2x2 matris ise çarpma ve çıakrma işlemi ile sonucu döndürür
            return matris[0][0]*matris[1][1]-matris[0][1]*matris[1][0]

        det = 0

        for i in range(len(matris)): # recursion ile determinantı hesaplar
            det += ((-1)**i)*matris[0][i]*DogrusalCebir.determinantHesapla(DogrusalCebir.minorHesapla(matris,0,i)) 

        return det

    def transpozAl(matris):
        return [list(i) for i in zip(*matris)]

    def tersinial(matris):
        if DogrusalCebir.determinantHesapla(matris)==0:
            return "A matrix whose determinant is 0 cannot be inverted."
        
        det = DogrusalCebir.determinantHesapla(matris)
        kofaktorler = []

        for satir in range(len(matris)):
            kofaktorSatir = []

            for sutun in range(len(matris)):
                minorMatris = DogrusalCebir.minorHesapla(matris, satir, sutun)
                kofaktorSatir.append(((-1)**(satir+sutun)) * DogrusalCebir.determinantHesapla(minorMatris))

            kofaktorler.append(kofaktorSatir)

        ekMatris = DogrusalCebir.transpozAl(kofaktorler)

        return DogrusalCebir.sabitlecarp(det, ekMatris)