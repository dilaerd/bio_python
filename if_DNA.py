sequence = input("Please enter a sequence:").upper()
dna = "ACGT"
sequence = sequence.replace(" ", "")

for i in sequence:
    if i in dna:
        define = 1
    else:
        define = 0
        break
if define == 1:
    print("This is a valid DNA sequence")
else:
    print("{} (base {}) is not a valid base. This is not a valid DNA sequence.".format(i,sequence.find(i)+1))
