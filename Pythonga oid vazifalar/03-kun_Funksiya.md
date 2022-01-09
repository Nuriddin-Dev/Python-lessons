### Funksiyaga oid topshiriqlar.

1. `Assalomu alaykum` so'zini chaqiradigan funksiya tuzing.
Funksiya nomini `salomlashuv` deb nomlang.
   
   <details><summary>Javob</summary>

     ```python
     def salomlashuv():
    print("Assalomu alaykum")

    salomlashuv()
     ```
    </details>
   
2. `deraza` nomli funksiya yarating. Va u konsolga quyidagicha chiqsin.
   
   ```shell
   +------+-------+
   |      |       |
   |      |       |
   +------+-------+
   |      |       |
   |      |       |
   +------+-------+
   ```
   <details><summary>Javob</summary>

     ```python
      def funksiya1():
          print('+------+-------+')
      
      def funksiya2():
          print('|      |       |')
      
      def deraza():
          funksiya1()
          funksiya2()
          funksiya2()
          funksiya1()
          funksiya2()
          funksiya2()
          funksiya1()
      
      deraza()
     ```
    </details>
   
3. Quyidagi dastur natijasi ayting.
   ```shell
   def kvadrat(x):
       y = x ** 2
       return y
   natija = kvadrat(14)
   
   print(f"{14} ning kvadrati {natija} ga teng.")
   ```

   <details><summary>Javob</summary>

     ```python
     14 ning kvadrati 196 ga teng.
     ```
    </details>

