def ip_to_bin(ip):
    ip = ip.split('.')
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

if __name__ == '__main__':
    user = int(input("1.Convertir BIN_to_IP | 2.Convertir IP_to_BIN : "))
    if user == 1:
        print(bin_to_ip(str(input('Entrez votre BIN : '))))
    elif user == 2:
        print(ip_to_bin(str(input('Entrez votre IP : '))))
    