import threading
import time

def program1():
    for i in range(5):
        print("Program 1 çalışıyor:", i)
        time.sleep(1)

def program2():
    for i in range(5):
        print("Program 2 çalışıyor:", i)
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=program1)
    t2 = threading.Thread(target=program2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Tüm programlar tamamlandı!")

#MULTIPROCESSING

import multiprocessing

def square(number):
  """Verilen sayının karesini hesaplar."""
  return number * number

if __name__ == "__main__":
  numbers = [2, 4, 6, 8, 10]
  processes = []

  # Her sayı için bir işlem oluştur
  for num in numbers:
    p = multiprocessing.Process(target=square, args=(num,))
    processes.append(p)
    p.start()

  # Tüm işlemlerin tamamlanmasını bekle
  for process in processes:
    process.join()

#KARŞILAŞTIRMA
import multiprocessing
import threading

def kare_hesapla(sayi):
    print(f"Hesaplanıyor (Thread/Process ID: {threading.get_ident()}): {sayi} -> {sayi*sayi}")

def coklu_programlama():
    sayilar = [1, 2, 3, 4, 5]
    threads = []
    for sayi in sayilar:
        t = threading.Thread(target=kare_hesapla, args=(sayi,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

def coklu_islemci():
    sayilar = [1, 2, 3, 4, 5]
    processes = []
    for sayi in sayilar:
        p = multiprocessing.Process(target=kare_hesapla, args=(sayi,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    print("Çoklu Programlama Başladı (Thread)...")
    coklu_programlama()
    print("Çoklu Programlama Tamamlandı!")

    print("Çoklu İşlemci Başladı (Process)...")
    coklu_islemci()
    print("Çoklu İşlemci Tamamlandı!")