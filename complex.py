class complex_number:
    def __init__(self,i=0,r=0):
        self.real=r
        self.imag=i
    def display_complex_number(self):
        print "The complex Number is: {0}+{1}j".format(self.real,self.imag)



c1=complex_number(8,9)
c1.display_complex_number()
if __name__=="__main__":
    main()

        
