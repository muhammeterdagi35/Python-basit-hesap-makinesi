print(
    '''
    toplama(+)
    çıkarma(-)
    çarpma(*)
    bölme(/)
'''
)
while True:

 sayi1 = int(input("1.sayıyı giriniz:"))
 sayi2 = int(input("2.sayıyı giriniz:"))
 islem =input('yapmak istediğniiz işlemi giriniz (+-*/):')

 if islem == '+':
    print(sayi1 , '+' , sayi2 , '=' , sayi1 + sayi2)
   

 elif islem == '-':
    print(sayi1 , '-' , sayi2 , '=' , sayi1 - sayi2)
   


 elif islem == '*':
    print(sayi1 , '*' , sayi2 , '=' , sayi1 * sayi2)
   


 elif islem == '/':
    print(sayi1 , '/' , sayi2 , '=' , sayi1 // sayi2)
   

 else:
    print('geçersiz işlem girdiniz')
 
