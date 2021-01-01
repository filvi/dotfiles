import sys
import os
import sqlite3
from datetime import datetime as d



# mi creo le variabili per quando ==============================================
anno =  d.now().strftime("%Y")
mese =  d.now().strftime("%m")
giorno =  d.now().strftime("%d")
ora =  d.now().strftime("%H")
minuti =  d.now().strftime("%M")
args = sys.argv

# si o no ===========================================
yes = {'yes','y'}
no = {'no','n'}

if not os.path.isfile(os.environ['HOME'] + '/.config/worktime/worktime.db'):
    if not os.path.exists(os.environ['HOME'] + '/.config/worktime'):
        os.mkdir(os.environ['HOME'] + '/.config/worktime')
        os.chdir(os.environ['HOME'] + '/.config/worktime')
    

# funzione che mi fa tutto =====================================================
def inserisci_task(*args):
    # definisco il momento in cui inserisco il task ============================
    time = f"{giorno}.{mese}.{anno} - {ora}:{minuti}"

    # importo il nome del task =================================================
    for i in range (1,len(args)):
          # input per inizio alla tot ora
          if args[i] == "-d":
              # raw_input returns the empty string for "enter"
              choice = input('Vuoi eliminare una entry? Questo cambiamento non e\' reversibile? [Y/n] ').lower()
              if choice in yes:
                sql = "ALTER TABLE `task` AUTO_INCREMENT = 1"
                return True
              elif choice in no:
                return False
              else:
                sys.stdout.write("La risposta che hai fornito non e\' valida")
          elif args[i] == "-h":
              actiontype = "help"
          elif args[i] == "-i":
              task = args[i + 1] 
              # mi connetto al DB ==============================================
              conn = sqlite3.connect(os.environ['HOME'] + '/.config/worktime/worktime.db')
              c = conn.cursor()
              sql = f"INSERT INTO task (`DONE`, `TASK`) VALUES ('{time}', '{task}')"
              # esegue la query ================================================
              c.execute(sql)
              # Salva i cambiamenti ============================================
              conn.commit()
              # chiude la connessione ==========================================
              conn.close()
              os.system('clear')
              print(f'Ho inserito {task} con il tag temporale {time}')
          elif args[i] == "-l":
              print('Ecco la lista')
              # mi connetto al DB ==============================================
              conn = sqlite3.connect(os.environ['HOME'] + '/.config/worktime/worktime.db')
              c = conn.cursor()
              sql = "SELECT * FROM task"

              # esegue la query ================================================
              tabella = c.execute(sql)
              rows = tabella.fetchall()
              for row in rows:
                  quando = row[1]
                  task = row[2]
                  print(f"{quando}> {task}")
                  
              # Salva i cambiamenti ============================================
              conn.commit()
              # chiude la connessione ==========================================
              conn.close()

              
    # inserisci qui il codice sql TODO
#    conn = sqlite3.connect(os.environ['HOME'] + '/.config/worktime/worktime.db')
#    c = conn.cursor()
#    if actiontype == "insert":
#      pass
#    elif actiontype == "delete":
#      pass
#    elif actiontype == "list":
#      pass
#    else:
#        print('\n\nworktime version 1.0.1\n')
#        print("Switches: \n-d\t[d]elete \n-l\t[l]ist \n-i\t[i]nsert")

    # sql = f"INSERT INTO task (`DONE`, `TASK`) VALUES ('{time}', '{task}')"
    # # esegue la query ================================================
    # c.execute(sql)
    # # Salva i cambiamenti ============================================
    # conn.commit()
    # # chiude la connessione ==========================================
    # conn.close()





if __name__ == "__main__":
    inserisci_task(*args)
