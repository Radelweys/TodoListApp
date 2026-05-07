import tampilan as tp
tp.tampilanAwal()

todoList = []




def input_tugas():
  print('Masukann tugas kamu: ')
  i = 1
  while i <= 5 :
    masukan_tugas = input('Tugas ke-{}: '.format(i))
    todoList.append(masukan_tugas)
    i+=1
  return todoList

  
  

def tampilkan_tugas(tugas=todoList):
  for i in range(len(tugas)):
    print('Tugas ke-{}: {}'.format(i+1, tugas[i]))


def main():
  
  input_tugas()
  tp.tampilanHasil()

  tampilkan_tugas()
  print('Kamu sudah berhasil mengisi tugas')


main()





