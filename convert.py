




class Convert:
    def __init__(self, input_file: str, output_file: str, start_code_block="scb", end_code_block="ecb"):
        self.input_file = input_file
        self.output_file = output_file
        self.start_code_block = start_code_block
        self.end_code_block = end_code_block

    
    def py2ipynb(self):
        with open(self.input_file, "r") as f:
            sorok = f.readlines()
            """for sor in sorok:
                if í.start_code_block in sor:
                    print("ok")"""
            

            start_block_index = []
            end_block_index = []
            
            for sor_index in range(len(sorok)):
                
                if self.start_code_block in sorok[sor_index]:
                    start_block_index.append(sor_index)
                if self.end_code_block in sorok[sor_index]:
                    end_block_index.append(sor_index)
            block_length_index_dict = dict(zip(start_block_index, end_block_index))
            
            block_length_index_list = []

            for start, end in block_length_index_dict.items():
                block_length_index_list.append([start, end])
            print(block_length_index_list)
            print(block_length_index_dict)
            
                

            
                
                


a = Convert("test.py", "test.ipynb")
a.py2ipynb()