import os
import secrets

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from dotenv import load_dotenv

from router import executar_comando


# Carrega as variáveis armazenadas no arquivo .env.
load_dotenv()


app = Flask(__name__)


# Chave usada pelo Flask para proteger a sessão.
app.secret_key = os.getenv(
    "FLASK_SECRET_KEY",
    secrets.token_hex(32)
)


# Senha usada para entrar no Nexus Web.
SENHA_WEB = os.getenv("NEXUS_WEB_PASSWORD")


if not SENHA_WEB:
    raise RuntimeError(
        "A variável NEXUS_WEB_PASSWORD não foi encontrada no arquivo .env."
    )


def usuario_autenticado():
    """
    Retorna True quando o usuário já realizou o login.
    """

    return session.get("autenticado", False)


@app.route("/login", methods=["GET", "POST"])
def login():

    erro = ""

    if request.method == "POST":

        senha_digitada = request.form.get(
            "senha",
            ""
        )

        # Compara as senhas de maneira mais segura.
        if secrets.compare_digest(
            senha_digitada,
            SENHA_WEB
        ):

            session["autenticado"] = True

            return redirect(
                url_for("pagina_inicial")
            )

        erro = "Senha incorreta."

    return render_template(
        "login.html",
        erro=erro
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )


@app.route("/", methods=["GET", "POST"])
def pagina_inicial():

    # Bloqueia o painel caso o usuário não esteja autenticado.
    if not usuario_autenticado():

        return redirect(
            url_for("login")
        )


    comando = ""

    comando_pendente = ""

    resposta = ""


    if request.method == "POST":

        acao = request.form.get(
            "acao",
            ""
        )

        comando = request.form.get(
            "comando",
            ""
        ).strip()


        # O comando ainda não é executado.
        # Primeiro ele é mostrado para confirmação.
        if acao == "preparar":

            if comando:

                comando_pendente = comando

            else:

                resposta = "Digite um comando."


        # O router só é chamado depois da confirmação.
        elif acao == "confirmar":

            if comando:

                resposta_router = executar_comando(
                    comando
                )


                if resposta_router:

                    resposta = resposta_router

                else:

                    resposta = "Comando executado."


            else:

                resposta = (
                    "Nenhum comando foi recebido."
                )


        elif acao == "cancelar":

            resposta = "Comando cancelado."


    return render_template(

        "index.html",

        comando=comando,

        comando_pendente=comando_pendente,

        resposta=resposta

    )


def iniciar_servidor_web():

    print("Nexus Web iniciado.")

    print(
        "Acesso local:"
    )

    print(
        "http://127.0.0.1:5000"
    )


    app.run(

        host="0.0.0.0",

        port=5000,

        debug=False,

        use_reloader=False

    )


if __name__ == "__main__":

    iniciar_servidor_web()