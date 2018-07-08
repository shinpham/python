
class baitap:
    def chuyenchu(so):
        kq = ""
        lsthang={}
        i=1
        j=10*i

        for _ in range(0,len(str(so))):
            lsthang[_]=int(so%j/i)
            i=10*i
            j=10*j
            if _ == 0:
                if lsthang[_] == 0:
                    kq = "mươi" + kq
                else:
                    if lsthang[_] == 1:
                        kq = "một " + kq
                    elif lsthang[_] == 2:
                        kq = "hai " + kq
                    elif lsthang[_] == 3:
                        kq = "ba " + kq
                    elif lsthang[_] == 4:
                        kq = "bốn " + kq
                    elif lsthang[_] == 5:
                        kq = "năm " + kq
                    elif lsthang[_] == 6:
                        kq = "sáu " + kq
                    elif lsthang[_] == 7:
                        kq = "bảy " + kq
                    elif lsthang[_] == 8:
                        kq = "tám " + kq
                    elif lsthang[_] == 9:
                        kq = "chín " + kq
            if _ == 1:
                if lsthang[_] == 0 and lsthang[2] == 0:
                    pass
                elif lsthang[_] == 0 and lsthang[0] == 0:
                    kq = "đồng"
                elif lsthang[_] == 0 and lsthang[0] > 0:
                    kq = "lẻ " + kq
                else:
                    if lsthang[_] == 1:
                        kq = "một " + kq
                    elif lsthang[_] == 2:
                        kq = "hai " + kq
                    elif lsthang[_] == 3:
                        kq = "ba " + kq
                    elif lsthang[_] == 4:
                        kq = "bốn " + kq
                    elif lsthang[_] == 5:
                        kq = "năm " + kq
                    elif lsthang[_] == 6:
                        kq = "sáu " + kq
                    elif lsthang[_] == 7:
                        kq = "bảy " + kq
                    elif lsthang[_] == 8:
                        kq = "tám " + kq
                    elif lsthang[_] == 9:
                        kq = "chín " + kq
            if _ == 2:
                if lsthang[_] == 0:
                    pass
                else:
                    if lsthang[_] == 1:
                        kq = "một trăm " + kq
                    elif lsthang[_] == 2:
                        kq = "hai trăm " + kq
                    elif lsthang[_] == 3:
                        kq = "ba trăm " + kq
                    elif lsthang[_] == 4:
                        kq = "bốn trăm " + kq
                    elif lsthang[_] == 5:
                        kq = "năm trăm " + kq
                    elif lsthang[_] == 6:
                        kq = "sáu trăm " + kq
                    elif lsthang[_] == 7:
                        kq = "bảy trăm " + kq
                    elif lsthang[_] == 8:
                        kq = "tám trăm " + kq
                    elif lsthang[_] == 9:
                        kq = "chín trăm " + kq
        return kq

    dauvao = input("Nhập chuỗi số có 3 chữ số cách nhau dấu cách: ")
    lists = dauvao.split(" ")
    kq=""
    for i in range(0, len(lists)):
        doc = chuyenchu(int(lists[i]))
        kq += doc + "-"
    print(dauvao +"\n"+kq)