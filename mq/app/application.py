# coding: utf-8
import cherrypy
from .database import Database_cl
from .view import View_cl

#----------------------------------------------------------
class Application_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.db_o = Database_cl()
      self.view_o = View_cl()

   @cherrypy.expose
   #-------------------------------------------------------
   def index(self, **url):
   #-------------------------------------------------------
      form = url.get("index", "Startseite")
      return self.createContent_p(form)
   @cherrypy.expose
   #-------------------------------------------------------
   def add(self, **url):
   #-------------------------------------------------------
      form = url.get("index", "Startseite")
      return self.createForm_p(form)

   @cherrypy.expose
   #-------------------------------------------------------
   def edit(self, id_spl, **url):
   #-------------------------------------------------------
      form = url.get("index", "Startseite")
      return self.createForm_p(form, id_spl)

   @cherrypy.expose
   #-------------------------------------------------------
   #Argumente hinzufügen für zweites Teammitglied
   def save(self, id_spa, name1_spa, vorname1_spa, matrnr1_spa, semesternr1_spa, name2_spa, vorname2_spa, matrnr2_spa, semesternr2_spa, **url):
   #-------------------------------------------------------
      form = url.get("index", "Startseite")
      id_s = id_spa
      data_a = [ name1_spa, vorname1_spa, matrnr1_spa, semesternr1_spa, name2_spa, vorname2_spa, matrnr2_spa, semesternr2_spa]
      if id_s != "None":
         self.db_o.update_px(id_s, data_a)
      else:
         self.db_o.create_px(data_a)
      return self.createContent_p(form)

   @cherrypy.expose
   #-------------------------------------------------------
   def delete(self, _id, **url):
      form = url.get("index", "Startseite")
      self.db_o.delete_px(_id)
      raise cherrypy.HTTPRedirect("/?index=" + form )
   #-------------------------------------------------------

   @cherrypy.expose
   #-------------------------------------------------------
   def default(self, *arguments, **kwargs):
   #-------------------------------------------------------
      msg_s = "unbekannte Anforderung: " + \
      str(arguments) + \
      ' ' + \
      str(kwargs)
      raise cherrypy.HTTPError(404, msg_s)
   default.exposed= True

   #-------------------------------------------------------
   def createContent_p(self, form):
   #-------------------------------------------------------
      data_o = self.db_o.read_px()
      return self.view_o.createContent_px(data_o, form)

   #-------------------------------------------------------
   def createForm_p(self, form, id_spl = None):
   #-------------------------------------------------------
      if id_spl != None:
         data_o = self.db_o.read_px(id_spl)
      else:
         data_o = self.db_o.getDefault_px()
      return self.view_o.createForm_px(id_spl, form, data_o)
# EOF
