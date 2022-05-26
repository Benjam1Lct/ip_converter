def ip_to_bin(cidr):
    cidr = cidr.split('/')
    ip = cidr[0].split('.')
    bin = []
    for i in ip:
        binTemp = []
        count = 0
        a = i
        a = int(a)
        if  a == 0:
            for i in range(8):
                bin.append("0")
        else:
            while a > 0:
                count += 1
                binTemp.append(str(a%2))
                a = a//2
            if len(binTemp) < 8:
                while len(binTemp) < 8:
                    binTemp.append("0")
            idx = len(binTemp) - 1
            while idx >= 0:
                bin.append(str(binTemp[idx]))
                idx = idx - 1
    return "".join(bin)

def bin_to_ip(bin):
    a = 0
    b = 8
    result = []
    newBin = []
    for i in bin:
        newBin.append(i)
    for i in range(4):
        resultTemp = 0
        coef = 1
        convBin = newBin[a:b]
        convBin = list(reversed(convBin))
        for j in convBin:
            if int(j) == 1:
                resultTemp = resultTemp + coef
            coef = coef*2
        result.append(str(resultTemp))
        a += 8
        b += 8

    return ".".join(result)

def masque(ip):
    ip = ip.split('/')
    ip = ip[1]
    count = 0
    result = []
    while count <= 32:
        if count < int(ip):
            result.append("1")
        else:
            result.append("0")
        count += 1
    return "".join(result)

def ad_reseau(ip, masque):
    result = []
    ip = list(ip)
    masque = list(masque)
    for i in range(32):
        if int(masque[i]) and int(ip[i]) == 1:
            result.append("1")
        else:
            result.append("0")
    return "".join(result)

def nb_machine(ip):
    ip = ip.split('/')
    nb_machine = 2**(32-int(ip[1]))-2
    return nb_machine

def ad_broadcast(ip, ipBin, masque):
    result = []
    reverseMasque = []
    ip = ip.split('/')
    ip = ip[1]
    ipBin = list(ipBin)
    masque = list(masque)
    for i in masque:
        if int(i) == 1:
            reverseMasque.append("0")
        elif int(i) == 0:
            reverseMasque.append("1")
    for i in range(32):
        if int(ipBin[i]) or int(reverseMasque[i]) == 1:
            result.append("1")
        else:
            result.append("0")
    return "".join(result)

def first_machine(ip):
    ip = list(ip)
    result = []
    for i in range(31):
        result.append(ip[i])
    result.append("1")
    return "".join(result)
    

def last_machine(ip):
    ip = list(ip)
    result = []
    for i in range(31):
        result.append(ip[i])
    result.append("0")
    return "".join(result)

if __name__ == "__main__":
    ip = str(input("entrez votre adresse IP avec CIDR : "))
    print("Adresse IP :", ip)
    print("Masque de sous reseau :", bin_to_ip(masque(ip)))
    print("Adresse reseau :", bin_to_ip(ad_reseau(ip_to_bin(ip), masque(ip))))
    print("Nombre de machine :", nb_machine(ip))
    print("Adresse de broadcast :", bin_to_ip(ad_broadcast(ip, ip_to_bin(ip), masque(ip))))
    print("Premiere machine :", bin_to_ip(first_machine(ad_reseau(ip_to_bin(ip), masque(ip)))))
    print("Derniere machine :", bin_to_ip(last_machine(ad_broadcast(ip, ip_to_bin(ip), masque(ip)))))