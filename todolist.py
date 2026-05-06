import tampilan as tp
from data import data 
tp.tampilanAwal()

listku = data()

if not listku:
  print('tugas kamu kosong')
else:
  print('Berikut tugas kamu:')


def input_tugas():
  print('Masukann tugas kamu: ')
  i = 1
  while i <= 5:
    masukan_tugas = input('Tugas ke-{}: '.format(i))
    listku.append(masukan_tugas)
    i+=1
  return listku

  
  

def tampilkan_tugas(tugas_baru=listku):
  for i in range(len(tugas_baru)):
    print('Tugas ke-{}: {}'.format(i+1, tugas_baru[i]))


def main():
  
  input_tugas()
  tp.tampilanHasil()

  tampilkan_tugas()
  print('Kamu sudah berhasil mengisi tugas')


main()





