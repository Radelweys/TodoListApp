import tampilan as tp
tp.tampilanAwal()

todoList = []

def input_tugas():
  print('Masukann tugas kamu: ')
  i = 1
  while i <= 5:
    masukan_tugas = input('Tugas ke-{}: '.format(i))
    tugas_baru = todoList.append(masukan_tugas)
    i+=1
  return tugas_baru

  
  

def tampilkan_tugas(tugas_baru=todoList):
  for i in range(len(tugas_baru)):
    print('Tugas ke-{}: {}'.format(i+1, tugas_baru[i]))


def main():
  input_tugas()
  tp.tampilanHasil()
  tampilkan_tugas()


main()





