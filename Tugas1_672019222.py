#Alfend.672019222

daftar = {
    'a' : ['b', 'c', 'd'],
    'b' : ['e', 'f', 'g', 'h'],
    'c' : ['i', 'j', 'k'],
    'd' : ['l', 'm', 'n'],
    'f' : ['o', 'p', 'q'],
    'g' : ['r', 's'],
    'k' : ['t'],
    'm' : ['u']
}

awal = 'a'

def var1(var2, var3):
     sudah = []
     now = [var2]

     while now:
        nodeSaatIni = now.pop(0)
        if nodeSaatIni not in sudah:
            sudah.append(nodeSaatIni)
        if nodeSaatIni in var3:
            for anak in var3[nodeSaatIni]:
                now.append(anak)
     return sudah

if __name__ == "__main__":
    print("Output hasil BFS : ")
    print(var1(awal, daftar))
    print("Aku berada di urutan ke : ")
    print((var1(awal, daftar).index('u') + 1))