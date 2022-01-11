### Mashqlar

1. Foydalanuvchidan 5 ta son kiritishni talab qilsin. Kiritilgan sonlar ichidan eng kattasini qaytaradigan dastur tuzilsin.
`max` funksiyasidan foydalanilmasin. Ekranga `Eng katta son 48` ko'rinishida chiqsin.
   
   <details><summary>Javob</summary>

     ```python
     i = 1
     bush_list = []
     while i<6:
         son = int(input(f"{i} sonni kiriting: "))
         bush_list.append(son)
         i = i + 1
     
     bush_list.sort()
     
     print('Eng katta son ',bush_list[-1])
     ```
    </details>