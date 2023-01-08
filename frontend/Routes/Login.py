from flask import Blueprint,render_template,request,make_response,flash,session,redirect,url_for
from os import getenv
from requests import post,get

from functools import wraps
bp = Blueprint('auth',__name__,url_prefix='/auth')




@bp.route("/login",methods=["GET","POST"])
def login():

    if session.get("user"):
        return redirect(url_for("user.dashboard"))
    if request.method == "POST":

        user = request.form
        if len(user['username']) == 0:
            return response_message("Indique el usuario",415),415
        elif len(user['password']) == 0:
            return response_message("Indique la contraseña",415),415
        else:
            payload = {
                "username":user['username'],
                "password":user['password']
            }
            try:
                url = getenv("API_HOST") + "/auth"
                headers = {"Content-Type":"application/json"}
                req = post(url,headers=headers,json=payload)
                if req.status_code == 401:
                    return response_message("Credenciales invalidas",401),401
                elif req.status_code == 200:
                    token = req.json()['token']
                    req =  get(url,headers={"Authorization": f"Bearer {token}"})
                    if req.status_code == 200:
                        user = req.json()

                        user['token'] = token
                        user['authenticated'] = True

                        session.clear()
                        session['user'] = user
                        return user,200
                    elif req.status_code == 404:
                        return response_message("El usuario no existe",404),404

            except Exception as e:
                flash(response_message("Ocurrio un error, intente denuevo.",False))


    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    session.clear()
    return response_message("Logout",200),200

def LoginRequired(view):
    @wraps(view)
    def checkIfLogin(*args,**kwargs):
        if session.get("user") is not None:
            return view(*args,**kwargs)
        return redirect(url_for("auth.login"))
    return checkIfLogin


def response_message(message : str,code : bool):
    return {
        "message":message,
        "code":code
    }
