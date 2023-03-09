class ComplexNumber:
    
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    
    
    def __sub__(self,obj):
        r = self.real - obj.real
        i = self.imag - obj.imag
        return f"{r} - {abs(i)}j" if i<0 else f"{r} + {i}j"
    
    
    def __mul__(self,obj):
        r = (self.real*obj.real) - (self.imag*obj.imag)
        i = (self.real*obj.imag) + (self.imag*obj.real)
        return f"{r} - {abs(i)}j" if i<0 else f"{r} + {i}j"
    
    
    def __truediv__(self,obj):
        dr = (obj.real**2+obj.imag**2)
        r = round(((self.real*obj.real)+(self.imag*obj.imag))/dr,2)
        i = round(((self.imag*obj.real)-(self.real*obj.imag))/dr,2)
        return f"{r} - {abs(i)}j" if i<0 else f"{r} + {i}j"
    
    
    def __floordiv__(self,obj):
        dr = (obj.real**2+obj.imag**2)
        r = ((self.real*obj.real)+(self.imag*obj.imag))//dr
        i = ((self.imag*obj.real)-(self.real*obj.imag))//dr
        return f"{r} - {abs(i)}j" if i<0 else f"{r} + {i}j"
    
    
    def __mod__(self,obj):
        dr = (obj.real**2+obj.imag**2)
        r = ((self.real*obj.real)+(self.imag*obj.imag))/dr
        i = ((self.imag*obj.real)-(self.real*obj.imag))/dr
        re = round(r - int(r),2)
        im = round(i - int(i),2)
        return f"{re} - {abs(im)}j" if im<0 else f"{re} + {im}j"



while 1:
    print("1.Subtration\t\t2.Multiplication\t3.Division\n4.Floor Division\t5.Remainder\t\t6.quit")
    k = input("\nEnter your choice : ")

    if k != '6':
        
        a1,b1 = map(int,input("\nEnter real1 and imaginary1 part : ").split())
        a2,b2 = map(int,input("Enter real2 and imaginary2 part : ").split())
        a = ComplexNumber(a1,b1)
        b = ComplexNumber(a2,b2)
    
        if k == '1':
            print(f"\n\tSubtration {(a.real,a.imag)} from {(b.real,b.imag)} is {a-b}\n")
        elif k == '2':
            print(f"\n\tMultiplication of {(a.real,a.imag)} and {(b.real,b.imag)} is {a*b}\n")
        elif k == '3':
            print(f"\n\tDivision of {(a.real,a.imag)} by {(b.real,b.imag)} is {a/b}\n")
        elif k == '4':
            print(f"\n\tFloor Division of {(a.real,a.imag)} by {(b.real,b.imag)} is {a//b}\n")
        elif k == '5':
            print(f"\n\tReminder on Dividing {(a.real,a.imag)} upon {(b.real,b.imag)} is {a%b}\n")
        else:
            print("\n\tSelect valid number")
    else:
        break