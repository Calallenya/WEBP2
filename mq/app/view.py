# coding: utf-8

import codecs
import os.path
import string

from mako.template import Template
from mako.lookup import TemplateLookup

#----------------------------------------------------------
class View_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.lookup_o = TemplateLookup('./templates')

   #-------------------------------------------------------
   def createContent_px(self, data_opl, form):
   #-------------------------------------------------------
      #Aufzählung
      if form == "Startseite":
         template_o = self.lookup_o.get_template('Startseite.tpl')
         markup_s = template_o.render(data_o=data_opl, listform=form)
         return markup_s
      elif form == "Pflege_Mitarbeiterdaten":
         template_o = self.lookup_o.get_template('Pflege_Mitarbeiterdaten.tpl')
         markup_s = template_o.render(data_o=data_opl, listform=form)
      elif form == "Pflege_Weiterbildungen":
         template_o = self.lookup_o.get_template('Pflege_Weiterbildungen.tpl')
         markup_s = template_o.render(data_o=data_opl, listform=form)
      elif form == "Sichtweise_Mitarbeiter":
         template_o = self.lookup_o.get_template('Sichtweise_Mitarbeiter.tpl')
         markup_s = template_o.render(data_o=data_opl, listform=form)
      elif form == "Sichtweise_Weiterbildungen":
         template_o = self.lookup_o.get_template('Sichtweise_Weiterbildungen.tpl')
         markup_s = template_o.render(data_o=data_opl, listform=form)
      elif form == "Mitarbeiter":
         template_o = self.lookup_o.get_template('Mitarbeiter.tpl')
         markup_s = template_o.render(data_o=data_opl, listform=form)
      elif form == "Weiterbildungen":
         template_o = self.lookup_o.get_template('Weiterbildungen.tpl')
         markup_s = template_o.render(data_o=data_opl, listform=form)
      elif form == "Zertifikate":
         template_o = self.lookup_o.get_template('Zertifikate.tpl')
         markup_s = template_o.render(data_o=data_opl, listform=form)
      else:
         template_o = self.lookup_o.get_template('Startseite.tpl')
         markup_s = template_o.render(data_o=data_opl, listform=form)
      return markup_s

#-------------------------------------------------------
   def createForm_px(self, id_spl, form, data_opl):
   #-------------------------------------------------------
      template_o = self.lookup_o.get_template("form.tpl")
      markup_s = template_o.render(data_o = data_opl, key_s = id_spl, listform=form)
      return markup_s

   #-------------------------------------------------------
   def readFile_p(self, fileName_spl):
   #-------------------------------------------------------
      content_s = ''
      with codecs.open(os.path.join('templates', fileName_spl), 'r', 'utf-8') as fp_o:
         content_s = fp_o.read()
      return content_s
# EOF
