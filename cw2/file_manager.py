class FileManager:
    def __init__(self,file_name):
        self.file_name = file_name
    def read_file(self):
        pliczek = open(self.file_name)
        zawartosc = pliczek.read()
        pliczek.close()
        return zawartosc
    def update_file(self,text_data):
        pliczunio = self.read_file()
        nowy = open(self.file_name,"w")
        nowy.write(pliczunio + text_data)
        nowy.close()
