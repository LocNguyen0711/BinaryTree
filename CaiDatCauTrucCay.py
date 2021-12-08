# Cài đạt nút gồm các thành phần:
class Nut:
    def __init__(self, data=None):  # Khởi tạo nút mặt định có dữ liệu là None( Rỗng)
        self.data = data  # data(Dữ liệu của nút),
        self.pLeft = None  # pLeft(Con trỏ nút trái, None),
        self.pRight = None  # pRight(Con trỏ nút phải, None).
# Cài đặt hàm thêm nút mới:

    def ThemNut(self, value):  # Biến value để truyền vào giá trị mới cần thêm,
        # Nếu giá trị mới truyền vào nhỏ hơn dữ liệu nút  <------nếu pLeft(Nút) có data > value-----------------.
        if value < self.data:
            # Xét tiếp con trỏ trái chưa có giá trị,                                                        .
            if(self.pLeft is None):
                # Thì con trỏ trái được KHỞI TẠO thành NÚT TRÁI(có data, pLeft, pRight) với data = value,   .
                self.pLeft = Nut(value)
            # Ngược lại( nếu con trỏ trái đã được khởi tạo thành con trỏ trái(data <> None, pLeft = None, pRight = None)),    .
            else:
                # Do pLeft lúc này là một Nut(data<>None, pLeft=None, pRight=None) nên đệ quy --------------
                self.pLeft.ThemNut(value)
        # Tương tự với nút trái
        elif(self.data < value):  # So sánh
            if(self.pRight is None):  # Chưa có giá trị
                # Khởi tạo NÚT PHẢI(data, pLeft, pRight)
                self.pRight = Nut(value)
            else:  # Ngược lại
                # Gọi lại ThemNut(value) cho Nut hiện tại(pRight có:data<>None, pLeft=None, pRight=None)
                self.pRight.ThemNut(value)

    def TienTu(self):  # Gốc -> con trái -> con phải
        if(self.data != None):  # Nếu data không rỗng( tức là có data, con trỏ trái hoặc con trỏ phải có thể là nút hoặc None) xét tiếp
            print(self.data, end=" -> ")  # In data
            # Sau khi in gốc thì xét tiếp nếu trỏ trái(chỉ có data, pLeft và pRight = None) có là nút con trái(có data, pLeft hoặc pRight khác None) thì xét tiếp
            if self.pLeft:
                # Gọi l: ại để in data và tiếp tục xét xem con trỏ trái của nút con trái có là con trỏ hay không
                self.pLeft.TienTu()
            # Xét tương tự nhu trỏ trái
            if self.pRight:  # Nếu là nút con phải
                self.pRight.TienTu()  # Gọi lại để in data và xét tiếp

    def TrungTu(self):

        if (self.pLeft != None):

            self.pLeft.TrungTu()

        print(self.data, end=" -> ")

        if (self.pRight != None):

            self.pRight.TrungTu()

    def HauTu(self):
        if(self.pLeft != None):
            self.pLeft.HauTu()
        if(self.pRight != None):
            self.pRight.HauTu()
        print(self.data, end=" -> ")

    def DemNutLa(self):
        dem = int
        dem = 0
        while(self.data != None):
            if(self.pLeft == None and self.pRight == None):
                dem = dem + 1
            else:
                if(self.pLeft != None):
                    self.pLeft.DemNutLa()
                else:
                    self.pRight.DemNutLa()
        print(dem)


test = Nut()
while(True):
    print("+-------------------------MENU-------------------------+")
    print("|\n\t1. Để Nhập mới một phần tử.                    |")
    print("|\n\t2. Duyệt cây nhị phân theo cấu trúc tiền tự.   |")
    print("|\n\t3. Duyệt theo trung tự.                        |")
    print("|\n\t4. Duyệt theo hậu tự.                          |")
    print("|\n\t5. Đếm số lá của cây.                          |")
    print("|\n\t0. Để Thoát khỏi chương trình cây nhị phân.    |")
    print("+------------------------------------------------------+")
    print("\n\t(?) Nhập vào lựa chọn: ", end="")
    x = int(input())
    if(x > 5 or x < 0):
        print("(!) Lựa chọn chức năng không tồn tại.")
    if(x == 1):
        print("\n\t(1) Nhập vào giá trị cần thêm mới: ", end="")
        value = input()
        if(test.data == None):
            test = Nut(value)
        else:
            test.ThemNut(value)
    if(x == 2):
        print("\n\t(2) Duyệt cây Tiền Tự -> ", end="")
        test.TienTu()
        print("Null")
    if(x == 3):
        print("\n\t(3) Duyệt cây Trung Tự -> ", end="")
        test.TrungTu()
        print("Null")
    if(x == 4):
        print("\n\t(4) Duyệt cây Hậu Tự -> ", end="")
        test.HauTu()
        print("Null")
    if(x == 5):
        print("Số nút của cây là : ", end="")
        test.DemNutLa()
        print()
    if(x == 0):
        break
