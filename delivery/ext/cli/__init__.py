import click
from delivery.ext.db import db
from delivery.ext.site import models #noqa


def init_app(app):

    @app.cli.command()
    def create_db():
        """Este comando iniciliaza o db"""
        db.create_all()  #try/except dps


    @app.cli.command()
    def listar_pedidos():
        # todo usuar tabulate
        click.echo("lista de pedidos")


    @app.cli.command()
    def listar_usuarios():
        click('lista de usuarios')
