import subprocess
import os

class Systems():
    def __init__(self,rollno,name="DEFAULT"):
        self.name=name
        self.rollno=rollno

    def create_folder(self):
        try:
            if not os.path.exists(f'./{self.rollno}/'):
                os.mkdir(f'./{self.rollno}')
            return True
        except Exception as e:
            print('Folder creation error',e)
            return False
    def create_container(self,port):
        try:
            a=os.system(f'docker run -p {port}:8765 -v $(pwd)/{self.rollno}:/workdir -d khallnayak/zacodeworld:0.1')
            assert a==0
        except Exception as e:
            print(e)
            return False
        else:
            return True
    
