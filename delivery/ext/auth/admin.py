from calendar import c
from flask_admin.contrib.sqla import ModelView

# self representa o próprio admin aqui fora de um classe...
def format_user(self, request, user, *args):
      return user.email.upper()


class UserAdmin(ModelView):
      """Interface admin de users"""
      
      column_formatters = {"email": format_user}