
from flask import Flask,request,render_template
import filterstop
#print (filterstop.con())

app= Flask(__name__)

@ app.route('/',methods=['GET','Post'])
def index():
    if request.method== 'POST':
        sentence=request.form['sentence']
        clean_sentence=filterstop.rem_stop(sentence)
        result=[0.5,0.6,0.8,0.3,0.4,0.5]
        return render_template('result.html',
                               text=sentence,toxic=result[0],setoxic=result[1],obscene=result[2],
                               threat=result[3],insult=result[4],idhate=result[5])
    return render_template("main.html")



if __name__=="__main__":
    app.run(debug=True)


