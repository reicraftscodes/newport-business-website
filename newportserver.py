# ===================== Server Imports ==========================
import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

# ========== Database Connection and ALLOWED_EXTENSIONS ================

DATABASE = "database.db"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

# ===================== Loading Templates ==========================

@app.route("/home")
def runhome():
    return render_template("home.html")

@app.route("/home/createdb")
def rundb():
    return render_template("home.html")

@app.route("/aboutus")
def runAboutUs():
    return render_template("AboutUs.html")

@app.route("/aboutNewport")
def runAboutNewport():
    return render_template("aboutNewport.html")

# ===================== Business Search ==========================

@app.route("/shopSearch")
def shopSearch():
    return render_template("shopSearch.html")

@app.route("/shopSearch/searchresult", methods = ['GET'])
def shopquery():
    search = request.args.get('search', default="Error")
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM newport_database WHERE Company_Account=?;", [search])
    data = cur.fetchall()
    conn.close()
    # enter the file name for the search result page below
    return render_template("listshops.html", data = data)

@app.route("/shopSearch/searchresultbytype", methods = ['GET'])
def shopquerytype():
    searchtype = request.args.get('searchtype', default="Error")
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM newport_database WHERE type=?;", [searchtype])
    data = cur.fetchall()
    conn.close()
    # enter the file name for the search result page below
    return render_template("listshops.html", data = data)

# ===================== Business Search ==========================

@app.route("/businessSearch")
def businessSearch():
    return render_template("businessSearch.html")

@app.route("/businessSearch/searchresult", methods = ['GET'])
def query():
    search = request.args.get('search', default="Error")
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Businesses WHERE name=?;", [search])
    data = cur.fetchall()
    conn.close()
    # enter the file name for the search result page below
    return render_template("listbusinesses.html", data = data)

@app.route("/businessSearch/searchresult2", methods = ['GET'])
def querytype():
    searchtype = request.args.get('searchtype', default="Error")
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Businesses WHERE type=?;", [searchtype])
    data = cur.fetchall()
    conn.close()
    # enter the file name for the search result page below
    return render_template("listbusinesses.html", data = data)

# ========================== News ===============================
@app.route("/news")
def news():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM News ORDER BY dates DESC")
    data = cur.fetchall()
    conn.close()
    return render_template("news.html", data = data)

# ========================== News ===============================
@app.route("/events")
def events():
    return render_template("events.html")

# ========================== Members ===============================
@app.route("/memberSearch")
def member():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users")
    data = cur.fetchall()
    conn.close()
    return render_template("members.html", data = data)

@app.route("/memberSearch/Result")
def result():
    search = request.args.get('members', default="Error")
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    sqlQuery = "SELECT * FROM Users WHERE userName=\"" + search + "\""
    cur.execute(sqlQuery)
    data = cur.fetchall()
    conn.close()
    return render_template("membersSearchResult.html", data = data)

# ===================== Login to Database ==========================

@app.route("/login")
def loadloginpage():
    return render_template("loginpage.html")

app.secret_key = 'fj590Rt?h40gg'

# Cookie sessions
@app.route("/loginuser", methods = ['GET','POST'])
def loginuser():
    if request.method=='POST':
        uName = request.form.get('username', default="Error")
        pw = request.form.get('password', default="Error")
        uType = []
        if checkuName(uName):
            if checkpw(uName, pw):
                if checkusertype(uName, uType) == "member":
                    # resp = make_response(render_template('membersHome.html', msg='hello '+uName, username = uName))
                    session['username'] = request.form['username']
                    conn = sqlite3.connect(DATABASE)
                    conn = conn.cursor()
                    conn.execute("SELECT usercompany FROM Users WHERE userName=?;", [uName])
                    usercompany = conn.fetchall()
                    print(usercompany)
                    conn.close()
                    conn = sqlite3.connect(DATABASE)
                    curSearch = conn.cursor()
                    curSearch.execute("SELECT * FROM newport_database WHERE Company_Account=?;", usercompany[0])
                    dataSearch = curSearch.fetchall()
                    conn.close()
                    resp = make_response(render_template('membersHome.html', msg='hello '+uName, username = uName, dataSearch=dataSearch, usercompany = usercompany[0]))
                    # return render_template("adminEdit.html", dataSearch=dataSearch)
                elif checkusertype(uName, uType) == "admin":
                    resp = make_response(render_template('adminHub.html', msg='Welcome '+uName, username = uName))
                    session['username'] = request.form['username']
            else:
                resp = make_response(render_template('loginpage.html', msg='Incorrect  password'))
        else:
            resp = make_response(render_template('loginpage.html', msg='Incorrect  username'))
        return resp
    else:
        username = 'none'
        if 'username' in session:
            username = escape(session['username'])
        return render_template('loginpage.html', msg='', username = username)

# @app.route("/loginuser", methods = ['GET', 'POST'])
# def login():
#     if request.method == "POST":
#         uName = request.form.get('username', default="Error")
#         pw = request.form.get('password', default="Error")
#         conn = sqlite3.connect(DATABASE)
#         cur = conn.cursor()
#         count = conn.cursor()
#         sqlQuery1 = "SELECT * FROM Users WHERE userName=\"" + uName + "\" AND password=" + pw
#         cur.execute(sqlQuery1)
#         data = cur.fetchall()
#         sqlQuery2 = "SELECT count(*) FROM Users WHERE userName=\"" + uName + "\" AND password=" + pw
#         count.execute(sqlQuery2)
#         numRow = count.fetchall()
#         print(numRow)
#         sqlQuery3 = "SELECT * FROM Users WHERE userName=\"" + uName + "\" AND password=" + pw
#         conn.commit()
#         conn.close()
#         if numRow[0][0] == 1:
#             if data[0][3] == "member":
#                 resp = make_response(render_template('membersHome.html', msg='hello '+uName, username = uName))
#                 session['username'] = request.form['username']
#             elif data[0][3] == "admin":
#                 resp = make_response(render_template('adminHub.html', msg='Welcome '+uName, username = uName))
#                 session['username'] = request.form['username']
#             else:
#                 resp = make_response(render_template('loginpage.html', msg='Incorrect username or password'))
#         else:
#             resp = make_response(render_template('loginpage.html', msg='Incorrect username or password'))
#         return resp

def checkuName(uName):
    # uName = request.args.get('username', default="Error")
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT userName FROM Users WHERE userName=?;", [uName])
    data = cur.fetchall()
    conn.close()
    if uName in str(data):
        return uName

def checkpw(uName, pw):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT password FROM Users WHERE userName=?;", [uName])
    data = cur.fetchall()
    conn.close()
    if pw in str(data):
        return pw

def checkusertype(uName, uType):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT usertype FROM Users WHERE userName=?;", [uName])
    data = cur.fetchall()
    conn.close()
    if "member" in str(data):
        return "member"
    if "admin" in str(data):
        return "admin"


# ===================== Database functions ==========================

def createTables():
    print("skd;f")
    conn = sqlite3.connect(DATABASE)
    print("skd;f")

    conn.execute('CREATE TABLE IF NOT EXISTS Businesses (\
    						name TEXT NOT NULL,\
    						type TEXT NOT NULL,\
    						emailaddress VARCHAR NOT NULL,\
                            mobilenumber NUMERIC NOT NULL,\
                            description TEXT NOT NULL);')

    conn.execute('CREATE TABLE IF NOT EXISTS News (\
                            title TEXT NOT NULL,\
                            dates DATE NOT NULL,\
                            content TEXT NOT NULL);')

    conn.execute('CREATE TABLE IF NOT EXISTS Users (\
                            userID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,\
                            userName TEXT NOT NULL UNIQUE,\
                            password VARCHAR NOT NULL,\
                            usertype TEXT NOT NULL);')
    conn.commit()
    conn.close()


def populateTables():
    conn = sqlite3.connect(DATABASE)

    conn.cursor()
    conn.execute('INSERT INTO Businesses (name,type,emailaddress,mobilenumber,description)\
     						VALUES ("Argos","Retail","argos@hotmail.com",03456402020,"Argos is a big shop");')
    conn.execute('INSERT INTO Businesses (name,type,emailaddress,mobilenumber,description)\
     						VALUES ("Tesco Express","Groceries","Tesco@hotmail.com",077865465643,"Tesco is a bigger shop");')
    conn.execute('INSERT INTO Businesses (name,type,emailaddress,mobilenumber,description)\
     						VALUES ("Fish and Chips","Food","fishandchips@hotmail.com",0987654321,"Fish and chips sell fish and chips");')
    conn.execute('INSERT INTO Businesses (name,type,emailaddress,mobilenumber,description)\
     						VALUES ("South Wales Argus","Real Estate","southwalesargus@hotmail.com",0123456789,"Houses for sale in the Newport area");')
    conn.execute('INSERT INTO Businesses (name,type,emailaddress,mobilenumber,description)\
     						VALUES ("K G Building & Roofing","Building","KGBuildings@hotmail.com",02921993474,"Roof and home improvemnets in Newport");')
    conn.execute('INSERT INTO Businesses (name,type,emailaddress,mobilenumber,description)\
     						VALUES ("HH Cashflow Finance Ltd","Finance","HHCashflow@hotmail.com",01633439600,"Finance consulting in Newport");')


    users = [(1,"Martin", 1234, "admin"),
            (2,"Matthew", 1234, "admin"),
            (3,"May", 1234, "admin"),
            (4,"Talha", 1234, "admin"),
            (5,"Brian", 1234, "member")]
    conn.executemany("INSERT INTO 'Users' ('userID', 'userName', 'password', 'usertype')\
                    VALUES (?,?,?,?)",users)
    conn.commit()
    conn.close()

# def selectAll():
# 	conn = sqlite3.connect(DATABASE)
# 	cur = conn.cursor()
# 	cur.execute("SELECT * FROM Businesses")
# 	print( cur.fetchall() )
# 	conn.close()

def deleteTables():
    conn = sqlite3.connect(DATABASE)
    conn.execute('DROP TABLE IF EXISTS Businesses')
    conn.execute('DROP TABLE IF EXISTS Users')
    conn.commit()
    conn.close()


# ====================== Admin Controls ================================
@app.route("/admin")
def runAdminHub():
    return render_template("adminHub.html")

@app.route("/admin/AddBusiness")
def runAddDB():
    print('hello')
    return render_template("adminAddBussiness.html")

@app.route("/admin/AddUser")
def runAddUser():
    print('hello user')
    return render_template("adminAddUser.html")


@app.route("/admin/EditBusiness")
def runEditDB():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT Company_Account FROM newport_database ORDER BY Company_Account ASC;")
    data = cur.fetchall()
    dataSearch = [(0),(0),(0),(0),(0),(0),(0),(0),(0)]
    conn.close()
    return render_template("adminEdit.html", dataAll=data, dataSearch=dataSearch)

@app.route("/admin/EditBusiness/Search")
def searchEdit():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT Company_Account FROM newport_database ORDER BY Company_Account ASC;")
    dataAll = cur.fetchall()

    searchComp = request.args.get('searchBus', default="Error")
    curSearch = conn.cursor()
    curSearch.execute("SELECT * FROM newport_database WHERE Company_Account=?;", [searchComp])
    dataSearch = curSearch.fetchall()
    conn.close()

    return render_template("adminEdit.html", dataAll=dataAll, dataSearch=dataSearch)

@app.route("/admin/EditBusiness/Edit", methods=['POST'])
def editBusiness():
    ID = request.form.get('ID', default='Error')
    compName = request.form.get('compName', default="Error")
    compType = request.form.get('compType', default="Error")
    salutation = request.form.get('salutation', default="Error")
    fName = request.form.get('fName', default="Error")
    lName = request.form.get('lName', default="Error")
    phoneNum = request.form.get('phoneNum', default="Error")
    mobileNum = request.form.get('mobileNum', default="Error")
    eMail = request.form.get('eMail', default="Error")
    street = request.form.get('street', default="Error")
    postCode = request.form.get('postCode', default="Error")
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        sqlQuery = "UPDATE newport_database SET Company_Account=\"" + compName + "\",Type=\"" + compType + "\",Salutation=" + "\"" + salutation + "\",FirstName=" + "\"" + fName + "\",LastName=\"" + lName + "\",Phone=" + phoneNum + ",Mobile=" + mobileNum + ",Email=\"" + eMail + "\",Street=\"" + street + "\",PostCode=\"" + postCode + "\"" + " WHERE ID=" + ID
        print("Hello1")
        cur.execute(sqlQuery)
        print("Hello2")
        conn.commit()
        msg = "Record has been successfully edited"
    except:
        conn.rollback()
        msg = "Error in insert operation" + sqlQuery
    finally:
        return msg
        conn.close()

@app.route("/admin/addbussinessdata", methods = ['POST'])
def AddBussinessDetails():
    print('this is invoked')
    Company = request.form.get('Company_Account', default="Error")
    print(Company)
    Salutation = request.form.get('Salutation', default="Error")
    Type = request.form.get('type', default="Error")
    FirstName = request.form.get('FirstName', default="Error")
    LastName = request.form.get('LastName', default="Error")
    Phone = request.form.get('Phone', default="Error")
    Mobile = request.form.get('Mobile', default="Error")
    print(Mobile)
    Email = request.form.get('Email', default="Error")
    Street = request.form.get('Street', default="Error")
    PostCode = request.form.get('PostCode', default="Error")
    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        insertsql = "INSERT INTO newport_database ('Company_Account', 'type', 'Salutation', 'FirstName', 'LastName', 'Phone', 'Mobile', 'Email', 'Street', 'PostCode')\
		 			VALUES (\'" + Company + "\',\'" + Type + "\',\'" + Salutation + "\',\'" + FirstName + "\',\'" + LastName + "\',\'" + Phone + "\',\'" + Mobile + "\',\'" + Email + "\',\'" + Street + "\','" + PostCode + "\')"
        # print(insertsql)
        c.execute(insertsql)
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        return msg
        conn.close()

@app.route("/admin/addusersdata", methods = ['POST'])
def AddUserDetails():
    print('this is invoked')
    UserID = request.form.get('userID', default="Error")
    print(UserID)
    Username = request.form.get('userName', default="Error")
    Password = request.form.get('password', default="Error")
    Usertype = request.form.get('usertype', default="Error")
    Company = request.form.get('usercompany', default="Error")

    try:
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        insertsqluser = "INSERT INTO Users ('userID', 'userName', 'password', 'usertype', 'usercompany')\
		 			VALUES (\'" + UserID + "\',\'" + Username + "\',\'" + Password + "\',\'" + Usertype + "\','" + Company + "\')"

        # print(insertsql)
        c.execute(insertsqluser)
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        return msg
        conn.close()
# ===================== Starting the Server ==========================
if __name__ == "__main__":
    # deleteTables()
    # createTables()
    # populateTables()
    # selectAll()
    app.run(debug=True)

# msg = 'DB recreated'
