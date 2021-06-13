import PySimpleGUI as sg



def input_data():
    mantissa_bits=int(input('Enter number of the mantissa bits : '))
    expo_bits=int(input('Enter number of the expo bits : '))
    float_binary=input("Enter the floating point binary : ")
    return float_binary,mantissa_bits,expo_bits
def convert_binary(float_binary,mantissa_bits,expo_bits):
    expo_part=float_binary[-int(expo_bits):]
    mantissa_part=float_binary[:-int(expo_bits)]
    print(mantissa_part)
    exp=0
    for x in range(0,len(expo_part)):
        expo_bits=expo_bits-1
    
        if(int(expo_part[x])==1 and x==0):
            exp =exp - 2**int(expo_bits)
            print(exp)
        else:
            exp=exp+(int(expo_part[x]) *(2**int(expo_bits)))
    print(exp)
    mantissa_val=0
    expo_val=float(0)
    if exp>0:
        real_part=mantissa_part[1:exp+1]
        
        decimal_part=mantissa_part[len(real_part)+1:]
        mantissa_val=0
        expo_val=0
        
        real_part_len=len(real_part)
        for x in range(0,len(real_part)):
            mantissa_val=mantissa_val+((int(real_part[x]))*2**(real_part_len-1))
            
            real_part_len=real_part_len-1
        y=len(decimal_part)
        for x in range(0,len(decimal_part)-1):
            expo_val=expo_val+(int(decimal_part[x])*1/(2**(x+1)))    
            
        return expo_val+mantissa_val
    elif exp<0:
        decimal_part=mantissa_part[1:int(mantissa_bits)]
        
        for i in range(0,-(exp)):
            decimal_part='0'+decimal_part
            
        for x in range(0,len(decimal_part)-1):
            expo_val=expo_val+(int(decimal_part[x])*1/(2**(x+1)))
        
        return expo_val        

    elif exp==0:
        real_part=mantissa_part[1:exp+1]
        for x in range(len(real_part),0,-1):
            mantissa_val=mantissa_val+((int(mantissa_part[x]))*2**x)
        return mantissa_val 
        


float_num,mantisaa,expo=input_data()

val=convert_binary(float_num,mantisaa,expo)
print(val)
        

     