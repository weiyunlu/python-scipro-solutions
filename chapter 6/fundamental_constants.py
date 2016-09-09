def const_to_dict(filename):
    mydict = {} #initialize an empty dictionary
    with open(filename, 'r') as infile:
        for line in infile:
            char = line[27] #test the 27th character for being a digit
            try:
                eval(char) #if it was a digit, this works and eval passes to the processing
                pass
            except: #if it was a string, then eval fails and we skip this line
                continue
            name = line[:27].strip()
            value = float(line[27:45].strip())
            unit = line[46:].strip()
            mydict[name] = ({'value': value, 'unit': unit})
    return mydict
    
#test run on constants.txt
if __name__ == '__main__':
    import pprint
    pprint.pprint(const_to_dict('constants.txt'))