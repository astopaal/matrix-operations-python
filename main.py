import functions as f

matrix = f.DogrusalCebir.matrix

try:

    print("enter matrix rows with commas between elements \nGo to the next row by pressing enter after each row\nYou can only create 3x3 matrix.")

    for i in range(3):

        row = list(map(int, input().split(","))) #girilen inputu virgülleri baz alarak ayırır bu elemanları map ile int'e çevirir ve liste oluşturur
        matrix.append(row)

    if (len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3) :

        print("Main matrix must be 3x3. Please make sure the number of columns is 3!")
        f.DogrusalCebir.olusturulamadi()
        matrix.clear()

    else:

        print(f"Matrix created : {matrix}")

except:

    f.DogrusalCebir.hata()
    f.DogrusalCebir.olusturulamadi()


    
print("""Select the operation you want to perform on the matrix you created:\n
Type 1 for aggregation\n
Type 2 for extraction\n
Type 3 for extraction\n
Type 4 to calculate determinant\n
Type 5 to control involutivity \n
Type 5 to inverse matrix then press Enter..
""")

try:
    islem = int(input())
    
except Exception as e:
    f.DogrusalCebir.hata()
    print(e)

if islem==1:
    print("Type 1 to sum the matrix with a fixed number\nType 2 to sum the matrix with another matrix then press enter")
    secim = int(input())

    if secim==1:
        sabit = int(input("Enter the fixed number you want to sum: "))
        print(f"Sonuç: {f.DogrusalCebir.sabitletopla(sabit,matrix)}\n")

    elif secim==2:
        
        sonuc = f.DogrusalCebir.matrisleTopla()
        print(f"Result: {sonuc}\n")
        

    else:
        print("An incorrect value was entered, please try again.")
        
    
if islem==2:
    print("Type 1 to subtract the matrix you created from the fixed number.\nType 2 to subtract a constant number from the matrix you created.\nType 3 to subtract the matrix you created from another matrix.\nType 4 to subtract the matrix you created from another matrix then press enter.")
    secim = int(input())
    sonuc = 0

    if secim == 1:
        sabit = int(input("Enter the constant number you want to subtract: "))
        sonuc = f.DogrusalCebir.sabittenCikar(sabit,matrix)

    elif secim == 2:
        sabit = int(input("Enter the constant number you want to subtract: "))
        sonuc = f.DogrusalCebir.sabiticikar(matrix,sabit)

    elif secim == 3:
        print("Create the matrix you want to subtract: \n")
        print("The number of rows and columns must be the same.")
        cikan = f.DogrusalCebir.matrisolustur()
        sonuc = f.DogrusalCebir.matristenCikar(matrix,cikan)

    elif secim == 4:
        print("Create the matrix you want to subtract: \n")
        print("The number of rows and columns must be the same.")        
        cikarilan = f.DogrusalCebir.matrisolustur()
        sonuc = f.DogrusalCebir.matristenCikar(cikarilan,matrix)

    else:
        print("An incorrect value was entered, please try again.")
    print(f"Result: {sonuc}")

if islem==3:
    print("Type 1 to multiply the matrix by a constant.\n Type 2 to multiply the matrix by another matrix then press enter")
    secim = int(input())

    if secim == 1:
        sabit = int(input("Enter the fixed number you want to multiply:"))
        sonuc = f.DogrusalCebir.sabitlecarp(sabit, matrix)

    if secim == 2:
        sonuc = f.DogrusalCebir.matrisleCarp()
    print(f"Result: {sonuc}")

if islem==4:
    det = f.DogrusalCebir.determinantHesapla(matrix)
    print(f"Determinant: {det}")

if islem==5:
    if f.DogrusalCebir.involutifMi(matrix):
        print("Matrix is involutive")
    else:
        print("Matrix is not involutive")

if islem==6:
    sonuc = f.DogrusalCebir.tersinial(matrix)
    print(f"The inverse of the entered matrix: {sonuc}")

