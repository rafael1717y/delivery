import click
from delivery.ext.db import db
from delivery.ext.db import models # no qa



def init_app(app):
    
    @app.cli.command()
    def create_db():
        """Este comando iniciliaza o db"""
        db.create_all()  #try/except dps


    

    @app.cli.command()
    def listar_pedidos():
        # TODO: usuar tabulate
        click.echo("lista de pedidos")


