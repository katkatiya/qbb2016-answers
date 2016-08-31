"""Parse a single fasta record from stdin and print it"""


class FASTReader(object):
    def __init__( self, file ):
        self.file = file
        self.last_id = None
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.last_id is None:
            line = self.file.readline()
            # verify isheader line
            if line =="":
                raise StopIteration
            assert line.startswith( ">" )
            #indentifer = line[1:].rstrip( "\r\n" ) # extract id --whole line
            indentifer = line[1:].split()[0]
        else:
            indentifer = self.last_id

        seq = [] #create list of sequences

        while True:
            line = self.file.readline().rstrip("\r\n")
            if line.startswith(">"):
                self.last_id = line[1:].split()[0]
                break
            elif line == "":
                if seq:
                    return indentifer, "".join(seq) 
                raise StopIteration #return None, None
            else:
                seq.append(line)
                
        return indentifer, "".join(seq) 
