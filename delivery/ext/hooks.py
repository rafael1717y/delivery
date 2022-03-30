from operator import imod
#from delivery.ext.db import db
#from delivery.ext.migrate import migrate

def init_app(app):

      @app.before_first_request
      def init_everything():
            #if db not initializied:
                  #db.create.all()
            # if migrate.:

            print('>>> Isto roda antes do primeiro request !!!')