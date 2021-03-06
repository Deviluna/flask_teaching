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
    if id in ('600477'):
        return """<title>Don't buy it!!!</title>
                <pre>
                                                                  +---------------------------------+
+----------------------+                          |                                 |
|                      |                          |   slump in 600477               |
|  a man bought 600477 |  +---------------------> |                                 |
|                      |                          |                                 |
+----------------------+                          |                                 |
                                                  |         it's very common        |
                                                  |                                 |
                                                  +----------X---X-+----------------+
  +---------------------------+                                    |
  |                           |                                    |
  |                           |                                    |
  |                           |                                    |
  |                           |                                    |
  |   if you bought 600477,   |                                    |
  |   you would be sad.       |                                    |
  |                           X                                    |
  |                           X                                    |
  |                           |                                    |
  |                           +------------------------------------+
  |                           |
  +---------------------------+


                                       XX
               XXXXX     XXXX       XXXXXXX
             XX         XX   X      XXX   XX         X XXX         XXX  X XX   XX X  X
            X           X     X    XX      X        X                      X           XX
          XX           XX     X    X       X      X         X             X
          XXXXX       X       X   X        X    XX         X             X              X
         X    XX     XX      XX  X         X   XXX        X    XX                      X
        XX     X     X       X   X         X       X   X  X  X XX       X
        X      X     XX     X    X         X             X                            X
         XX XX X      XXX XX     X       XX            X               X
                                  XXXX XX                             X              X
                                                     XX               X
                                                                      X             X
                                                                                   X
                                                                                   X
                                X XXXXXX    X
                              X        X    X
                           XX               X
                          X                 XXXXX
                          X                 XX    XXX
                            X  X           XX       X
                                  X X      X        X
                                    XX    XX     XXX
                        XXXXXXXX X X      X XXXXX

                </pre>
        
                """
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