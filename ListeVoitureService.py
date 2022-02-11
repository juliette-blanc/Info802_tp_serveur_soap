from spyne import Application, rpc, ServiceBase, Unicode, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json


class ListeVoitureService(ServiceBase):

    @rpc(_returns=Iterable(Unicode))
    def afficheListeVoiture(ctx):
        mon_json = {"voiture":
                            [{"nom": "Citroen C1", "autonomie": 120, "temps_recharge": 20},
                            {"nom": "Seat Ibiza", "autonomie": 150, "temps_recharge": 15},
                            {"nom": "Renault Kadjar", "autonomie": 200, "temps_recharge": 20},
                            {"nom": "Renault Clio", "autonomie": 100, "temps_recharge": 25}]
                   }
        yield u'%s' % json.dumps(mon_json)


# lance le service avec la classe ListeVoitureService en paramètre
application = Application([ListeVoitureService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())
wsgi_application = WsgiApplication(application)