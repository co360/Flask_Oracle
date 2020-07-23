from flask import Flask, render_template, request
import cx_Oracle as o
from dbHandle import insertData, selectData
from dbHandlePro import pinsertData, pselectData

app = Flask(__name__)


@app.route('/')
def rootFn():
    return 'Hello Flask!'


@app.route('/insertForm')
def insertFormFn():
    return render_template('insertForm.html')


@app.route('/insertResult')
def insertResultFn():
    myname = request.args['myname']
    myage = request.args['myage']
    mybirth = request.args['mybirth']
    rst = insertData(myname, myage, mybirth)
    return rst


@app.route('/selectStudent')
def selectStudentFn():
    data = selectData()
    print(data)
    return render_template('selectStudent.html', stdData=data)


@app.route('/productAdd')
def productAddFn():
    return render_template('product.html')

@app.route('/productAddForm')
def productAddFFn():
    return render_template('a.html')



@app.route('/productList')
def productListFn():
    pname = request.args['pname']
    pnum = request.args['pnum']
    pdate = request.args['pdate']
    rst = pinsertData(pname, pnum, pdate)
    return rst


@app.route('/selectProduct')
def selectProductFn():
    data = pselectData()
    print(data)
    return render_template('productList.html', pData=data)


if __name__ == '__main__':
    app.run(debug=True)
