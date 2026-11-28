# Flyer velador panda + elefante (tienda ids 92 y 91, $43.000 c/u). Uso: python3 flyers_panda_elefante.py [AAAA-MM-DD]
import os,sys,datetime
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
import flyers_deco as fd
from flyers_deco import bold,med,logo,BG,OR,CREAM
HERE=fd.HERE; D=HERE+'/assets/infantiles/'
def rmask(size,r=32):
    m=Image.new('L',size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,size[0]-1,size[1]-1),r,fill=255); return m
def flyer():
    W,H=1080,1350; c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
    d.rectangle((60,60,150,66),fill=OR)
    d.text((60,86),'VELADORES CON FIGURAS',font=bold(68),fill=(255,255,255))
    d.text((62,180),'Luz suave para el cuarto de los chicos',font=med(32),fill=(210,210,210))
    d.rounded_rectangle((640,246,1020,314),34,fill=OR); d.text((665,256),'CADA UNO $43.000',font=bold(34),fill=(20,20,20))
    for i,(f,n) in enumerate([('prod_panda_azul.jpg','Velador panda con bambú'),('elefante_store.jpg','Velador elefante')]):
        w,h=480,830-0; ph=Image.open(D+f).convert('RGB'); ih=h-70
        r=min(w/ph.width,ih/ph.height); ph=ph.resize((int(ph.width*r),int(ph.height*r)),Image.LANCZOS)
        cd=Image.new('RGB',(w,780),ph.getpixel((2,2)) if i==0 else (255,255,255)); h=780; ih=h-70
        r=min(w/ph.width,ih/ph.height); cd.paste(ph,((w-ph.width)//2,(ih-ph.height)//2))
        ImageDraw.Draw(cd).rectangle((0,ih,w,h),fill=CREAM); ImageDraw.Draw(cd).text((20,ih+16),n,font=bold(30),fill=(20,20,20))
        c.paste(cd,(60+i*500,330),rmask(cd.size,30))
    # alto de tarjetas: 330..1110
    d.rounded_rectangle((60,1170,1040,1316),30,fill=OR)
    lg=logo.copy(); lg.thumbnail((290,80)); d.rounded_rectangle((78,1186,378,1300),20,fill=CREAM); c.paste(lg,(78+(300-lg.width)//2,1186+(114-lg.height)//2),lg)
    d.text((415,1184),'Pedí por WhatsApp',font=med(30),fill=(20,20,20)); d.text((415,1220),'351 349 8646',font=bold(48),fill=(20,20,20))
    d.text((415,1280),'Recta Martinoli 8791 · Córdoba',font=med(22),fill=(20,20,20))
    return c
if __name__=='__main__':
    day=sys.argv[1] if len(sys.argv)>1 else datetime.date.today().isoformat()
    f=flyer(); f.save(f'{HERE}/{day}_veladores_figuras.jpg',quality=95); fd.story(f,'NOVEDAD EN DIME').save(f'{HERE}/{day}_veladores_figuras_estado.jpg',quality=95)
