from jinja2 import Environment, FileSystemLoader
import json




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
            
            env = Environment(loader=FileSystemLoader("blocks/"))
            base_template = env.get_template("base.json.jinja")
            

            code_blocks = []

            print(len(block_length_index_list))
            with open("blocks/code.json.jinja", "r") as f:
                
                for i in range(len(block_length_index_list)):
                    code_blocks.append(json.dumps(sorok[block_length_index_list[i][0]:block_length_index_list[i][1]]))
                
                code_block = f.read()
                code_template = env.get_template("code.json.jinja")
                content1 = code_template.render(blocks = code_blocks)
                
                with open(self.output_file, "w") as f:
                    content2 = base_template.render(blocks=content1)
                    
                    f.write(content2)
                    
            

            
            
            
            
            
                

            
                
                


a = Convert(input_file="test.py", output_file="test.ipynb")
a.py2ipynb()