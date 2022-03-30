from delivery.ext.auth import models # noqa
from delivery.ext.auth.commands import list_users, add_user 

from delivery.ext.db import db
from delivery.ext.admin import admin as main_admin
from delivery.ext.auth.admin import UserAdmin
from delivery.ext.auth.models import User


def init_app(app):
      """TODO: inicializar Flask Simple Login + JWT """
      app.cli.command()(list_users)
      app.cli.command()(add_user)

      main_admin.add_view(UserAdmin(User, db.session))