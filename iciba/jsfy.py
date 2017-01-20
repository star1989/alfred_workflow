#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# 金山翻译
# author by star
import sys
from workflow import Workflow,web
api_url = "http://dict-co.iciba.com/api/dictionary.php"
app_key = "DB77106E3D56416869155B591C53C9C5"
ICON_DEFAULT = 'icon.png'
update_settings = {'version': '1.0.0', 'github_slug': 'star1989/alfred_workflow'}
wf = Workflow(update_settings=update_settings)
word = sys.argv[1]

def getTransResult():
    url = api_url+"?w="+word+"&type=json&key="+app_key
    res = web.get(url)
    return res.json()

def genAlfred(data):
    if data.get('word_name','') != "":
        wf.add_item(
            title=u"am:[" + data['symbols'][0]['ph_am'] + "] ,en:["+data['symbols'][0]['ph_en']+"]",
            subtitle=u"phonic for " + word + "[by star]",
            arg=u"am:[" + data['symbols'][0]['ph_am'] + "] ,en:["+data['symbols'][0]['ph_en']+"]==="+data['symbols'][0]['ph_am_mp3'],
            valid=True,
            icon=ICON_DEFAULT)
        #mean
        for part in data['symbols'][0]['parts']:
            cur_title = u""+part['part']
            cur_title = cur_title + ','.join(part['means'])
            sub_title = u""+part['part']+" for "  + word + "[by star]"
            wf.add_item(
                title=cur_title,
                subtitle=sub_title,
                arg=cur_title+"==="+data['symbols'][0]['ph_am_mp3'],
                valid=True,
                icon=ICON_DEFAULT)
    else:
        wf.add_item(title=u'error...',
                    subtitle=u"something has wrong...",
                    arg=data['word_name'],
                    valid=True,
                    icon=ICON_DEFAULT)
    wf.send_feedback()

def main(wf):
    data = getTransResult()
    genAlfred(data)
    exit()

if __name__ == u"__main__":
    update_settings = {'version': '1.0.0','github_slug':'0.0.0'}
    wf = Workflow(update_settings=update_settings)
    sys.exit(wf.run(main))