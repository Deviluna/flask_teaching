from flask import Flask,request,current_app,abort,redirect




app=Flask(__name__)#start a flask instance for routing,using WSGI(Web Server Gateway Interface) protocol
#why the parameter "__name__" is essential?
# because flask constructor needs it to check the root path of this app,
# you can verify in its source code


@app.route("/")#route
def index():#view
    user_agent=request.headers.get('User-Agent')
    return "<h1>Welcome to Deviluna's Homepage</h1>"+"<p>your browser is %s</p>"%user_agent


@app.route("/stock/<id>")#sorry, my English is poor, can not explain it now.
def analyse_stock(id):
    if id in ('600477','000839'):
        return "<h1>%s is very dangerous!!!Don't buy it!!!</h1>"%id
    elif id=='604777':
        return redirect("http://caodong.tech")
    elif len(str(id))!=6:
        abort(404)
        #return "<h1>Bad Request</h1><p>the stock id shoule be 6 digits</p>",400 #return a status code 400(BAD REQUEST) to client.
    else:
        return "<h1>Sorry, no ideas about %s</h1>"%id

if __name__=="__main__":
    app_ctx=app.app_context()
    app_ctx.push()
    print("print ctx:",app_ctx)
    print("Using programme context to check url map:",app.url_map)
    app.run(debug=True,host='0.0.0.0',port=5001)
    #host address is important,the default host is 127.0.0.1


#sth to be explained later, such as hooks.