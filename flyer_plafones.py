# Flyer plafones 26/11. Uso: python3 flyer_plafones.py
import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import flyers_deco as fd
from flyers_deco import bold,med,cover,logo,BG,OR,CREAM,A
HERE=fd.HERE
def rr(im,r=32):
    m=Image.new('L',im.size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,im.width-1,im.height-1),r,fill=255); return im,m
def flyer():
    W,H=1080,1350
    c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
    d.rectangle((60,60,150,66),fill=OR)
    d.text((60,90),'PLAFONES',font=bold(88),fill=(255,255,255))
    d.text((62,200),'Luz de techo con diseño para tu casa',font=med(36),fill=(210,210,210))
    items=[('medusa-wood-5-luces_ambiente','Plafón Medusa Wood','5 luces, negro','$157.300'),
           ('gad_ambiente','Plafón Gad','Negro o blanco','$203.300')]
    for i,(f,n,s,p) in enumerate(items):
        x=60+i*510; y=270
        card=Image.new('RGB',(470,440),CREAM)
        card.paste(cover(Image.open(A+f+'.png'),470,300),(0,0))
        cd=ImageDraw.Draw(card)
        cd.text((24,312),n,font=bold(28),fill=(20,20,20)); cd.text((24,350),s,font=med(21),fill=(110,110,110)); cd.text((24,380),p,font=bold(36),fill=(215,115,15))
        _,m=rr(card); c.paste(card,(x,y),m)
    card=Image.new('RGB',(980,420),CREAM)
    bi=Image.open(A+'bag-30cm_ambiente.png').convert('RGB'); bi=bi.crop((45,0,555,600)); bi=bi.resize((480,int(600*480/510)))
    card.paste(bi.crop((0,0,480,420)),(0,0))
    cd=ImageDraw.Draw(card)
    cd.text((530,100),'Plafón Bag',font=bold(36),fill=(20,20,20)); cd.text((530,150),'Negro o blanco, 30 cm',font=med(26),fill=(110,110,110)); cd.text((530,210),'$145.200',font=bold(60),fill=(215,115,15))
    _,m=rr(card); c.paste(card,(60,720),m)
    d.rounded_rectangle((60,1170,1040,1316),30,fill=OR)
    lg=logo.copy(); lg.thumbnail((290,80)); d.rounded_rectangle((78,1186,378,1300),20,fill=CREAM); c.paste(lg,(78+(300-lg.width)//2,1186+(92-lg.height)//2),lg)
    d.text((415,1184),'Pedí por WhatsApp',font=med(30),fill=(20,20,20)); d.text((415,1220),'351 349 8646',font=bold(48),fill=(20,20,20))
    d.text((415,1280),'Recta Martinoli 8791 · Córdoba',font=med(22),fill=(20,20,20))
    return c
if __name__=='__main__':
    f=flyer(); f.save(HERE+'/2026-11-26_plafones.jpg',quality=95); fd.story(f).save(HERE+'/2026-11-26_plafones_estado.jpg',quality=95)
