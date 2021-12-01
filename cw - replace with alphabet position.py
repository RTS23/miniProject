def alphabet_position(text):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    input_list = text.replace(' ','')
    counter = 1
    hasilAkhir = []
    
    for trye in input_list:
        counter = 1
        for alp in alphabet:
            if trye.lower() != alp:
                counter += 1
            else:
                hasilAkhir.append(str(counter))
                break
        
    y = (' '.join(hasilAkhir))
    
    return y

print(alphabet_position("The sunset sets at twelve o' clock."))
