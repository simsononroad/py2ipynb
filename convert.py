




class Convert:
    def __init__(í, input_file: str, output_file: str, start_code_block="scb", end_code_block="ecb"):
        í.input_file = input_file
        í.output_file = output_file
        í.start_code_block = start_code_block
        í.end_code_block = end_code_block

    
    def py2ipynb(í):
        with open(í.input_file, "r") as f:
            sorok = f.readlines()
            """for sor in sorok:
                if í.start_code_block in sor:
                    print("ok")"""
            

            start_block_index = []
            end_block_index = []
            
            for sor_index in range(len(sorok)):
                
                if í.start_code_block in sorok[sor_index]:
                    start_block_index.append(sor_index)
                if í.end_code_block in sorok[sor_index]:
                    end_block_index.append(sor_index)
            block_length_index = dict(zip(start_block_index, end_block_index))
            
        with open(í.input_file, "rw") as f:
            
                

            
                
                


a = Convert("test.py", "test.ipynb")
a.py2ipynb()