from prettytable import PrettyTable
import optparse


myTable = PrettyTable(["Prethodna Rec", "Trenutna Rec", "Unos", "Kod"]) 


def get_arguments():
	parser = optparse.OptionParser()
	# dest= is how to get to the argument provided by user
	parser.add_option("-k", "--keyword", dest="keyword", help="String to Compress")
	parser.add_option("-m", dest="limit", help="Limit M", type='int')
	(options, arguments) = parser.parse_args()
	if not options.keyword:
		parser.error("[-] Please specify keyword, use --help for more info")
	return options

def unique(list1):
    return {item: i + 1 for i, item in enumerate(set(list1))}

def compress(cString, m=None):

    oString = []
    cString = [*cString]
    cipher = unique(cString)
    current = ""
    prev = ""
    input = ""
    code = ""
    for i in range(len(cString)):
        current = cString[i]
        if i == 0:
             myTable.add_row(["", current, "", ""])
        if (prev + current) in cipher:
            prev = prev + current
            input = ""
            code = ""
        else:
            oString.append(cipher.get(prev, 0))
            code = cipher.get(prev, 0);
            if m is None or len(cipher) + 1 <= m:
                cipher[prev + current] = len(cipher) + 1
                input = f"{prev + current} = {len(cipher) + 1}"
            prev = current
        
        # Add row to myTable
        myTable.add_row([prev, current, input, code])
    
    oString.append(cipher.get(prev, 0))
    myTable.add_row([prev, "/", input, cipher.get(prev, 0)])
    return oString



options = get_arguments()

if not options.limit:
    result = compress(options.keyword)
else:
    result = compress(options.keyword, options.limit)
print(myTable)
print("Compressed Output:", result)