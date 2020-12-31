from flask import Flask,request,session
import systems
app=Flask(__name__)
app.secret_key='LAVDALASUN'
PORTS=[6970,6971,6972]
OBJ_DICT={}

@app.route('/login/',methods=['POST'])
def login():
    if 'rollno' not in request.json.keys():
        return 'ROLL NO REQ'
    if PORTS==[]:
        return 'FULL'
    if request.json['rollno'] in session:
        rollno=request.json['rollno']
        OBJ_DICT[rollno]['obj']=systems.Systems(rollno)
        OBJ_DICT[rollno]['obj'].create_container(PORTS[0])
        port=PORTS.pop(0)
        return f'http://0.0.0.0:{port}'
    else:
        rollno=request.json['rollno']
        session[rollno]={}
        OBJ_DICT[rollno]={}
        OBJ_DICT[rollno]['obj']=systems.Systems(rollno)
        OBJ_DICT[rollno]['obj'].create_folder()
        OBJ_DICT[rollno]['obj'].create_container(PORTS[0])
        port=PORTS.pop(0)
        return f'http://0.0.0.0:{port}'
if __name__=='__main__':
    app.run(host='0.0.0.0',port='6969')


