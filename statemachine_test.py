from statemachine import StateMachine
from string import upper
import re

i = len(open('1.txt').read().split("\n"))
def doctype_way(txt):
    sped_txt = txt.split( "<",1)[1].split(None,1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word =="!DOCTYPE":
        txt = sped_txt[1].lstrip()
        newstate = 'doctype_state'
    else:
        reason = '!DOCTYPE'
        newstate = 'error_state'
        print reason, i-t+1
    return (newstate,txt)
    
def doctype_state_way(txt):
    sped_txt = txt.split('>',1)
    word = sped_txt[0].upper().strip()
    t = len(txt.split("\n"))
    if word == 'HTML':
        txt = sped_txt[1].lstrip()
        newstate = 'dhtml_state'
    else:
        reason = 'DHTML'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def dhtml_state_way(txt):
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'HTML':
        txt = sped_txt[1].lstrip()
        newstate = 'shtml_state'
    else:
        reason = 'SHTML'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def shtml_state_way(txt):
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'HEAD':
        txt = sped_txt[1].lstrip()
        newstate = 'shead_state'
    elif word =='BODY':
        txt = sped_txt[1].lstrip()
        newstate = 'sbody_state'
    else:
        reason = 'SHEAD or SBODY'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def shead_state_way(txt):
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'TITLE':
        txt = sped_txt[1].lstrip()
        newstate = 'stitle_state'
    elif word =='/HEAD':
        txt = sped_txt[1].lstrip()
        newstate = 'ehead_state'
    else:
        reason = 'STITLE OR EHEAD'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def stitle_state_way(txt):
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == '/TITLE':
        txt = sped_txt[1].lstrip()
        newstate = 'etitle_state'
    else:
        reason = 'ETITLE'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def etitle_state_way(txt):
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == '/HEAD':
        txt = sped_txt[1].lstrip()
        newstate = 'ehead_state'
    else:
        reason = 'EHEAD'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def ehead_state_way(txt):
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'BODY':
        txt = sped_txt[1].lstrip()
        newstate = 'sbody_state'
    else:
        reason = 'SBODY'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def sbody_state_way(txt):
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'P':
        txt = sped_txt[1].lstrip()
        newstate = 'sp_state'
    elif word[0] == 'A':
        txt = sped_txt[1].lstrip()
        newstate = 'sa_state'
    elif word =='/BODY':
        txt = sped_txt[1].lstrip()
        newstate = 'ebody_state'
    else:
        reason = 'SP or SA or EBODY1'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def sp_state_way(txt):
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == '/P':
        txt = sped_txt[1].lstrip()
        newstate = 'ep_state'
    else:
        reason = 'EP'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def ep_state_way(txt):
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'P':
        txt = sped_txt[1].lstrip()
        newstate = 'sp_state'
    elif word[0] == 'A':
        txt = sped_txt[1].lstrip()
        newstate = 'sa_state'
    elif word =='/BODY':
        txt = sped_txt[1].lstrip()
        newstate = 'ebody_state'
    else:
        reason = 'SP or SA or EBODY2'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def sa_state_way(txt):
    sped_txt = txt.split('<',1)[1].split(">",1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == '/A':
        txt = sped_txt[1].lstrip()
        newstate = 'ea_state'
    else:
        reason = 'EA'
        newstate = 'error_state'
        print reason,i-len(sped_txt[1].split("\n"))
    return (newstate,txt)
    
def ea_state_way(txt):
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'P':
        txt = sped_txt[1].lstrip()
        newstate = 'sp_state'
    elif word[0] == 'A':
        txt = sped_txt[1].lstrip()
        newstate = 'sa_state'
    elif word =='/BODY':
        txt = sped_txt[1].lstrip()
        newstate = 'ebody_state'
    else:
        reason = 'SP or SA or EBODY3'
        newstate = 'error_state'
        print reason,i-t+1
    return (newstate,txt)
    
def ebody_state_way(txt):
    if '<' in txt:
        sped_txt = txt.split('<',1)[1].split('>',1)
        t = len(txt.split("\n"))
        if len(sped_txt)>1:
            word = sped_txt[0].upper()
        else:
            word=txt
        if word == '/HTML':
            txt = sped_txt[0]
            newstate = 'finstate'
        else:
            reason = 'EHTML'
            newstate = 'error_state'
            print reason,i-t+1
    else:
        reason = 'EHTML'
        newstate = 'error_state'
        print reason,i
    return (newstate,txt)
    

    
if __name__=='__main__':
    m = StateMachine()
    m.add_state('orig',doctype_way)
    m.add_state('doctype_state',doctype_state_way )
    m.add_state("dhtml_state",dhtml_state_way)
    m.add_state("shtml_state",shtml_state_way)
    m.add_state("shead_state",shead_state_way)
    m.add_state("stitle_state",stitle_state_way)
    m.add_state("etitle_state",etitle_state_way)
    m.add_state("ehead_state",ehead_state_way)
    m.add_state("sbody_state",sbody_state_way)
    m.add_state("sp_state",sp_state_way)
    m.add_state("ep_state",ep_state_way)
    m.add_state("sa_state",sa_state_way)
    m.add_state("ea_state",ea_state_way)
    m.add_state("ebody_state",ebody_state_way)
    m.add_state("finstate",None,end_state=1)
    m.add_state("error_state", None, end_state=1)
    m.set_start('orig')
    m.run(open('1.txt').read())
    
relink = re.compile(r'<A href="(.*)".*>')
print relink.findall(open('1.txt').read())
