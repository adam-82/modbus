from bitstring import BitArray
a = "bin" 
# Create a BitArray from an integer
b = BitArray(int=2,length=8)
b.reverse()


y = {0:"Fault",1:"Running",2:"Pump Available"}
result = {}
for r,label in y.items():
    result[("%s_%s" % (a,label.replace("  "," ").replace(" ","_"))).lower()] = b[r]
    
result['%s_bits'%a]=b.bin

print(result)
