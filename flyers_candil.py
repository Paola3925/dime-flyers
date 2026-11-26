# Flyers Candil (productos de la tienda ids 79-89). Uso: python3 flyers_candil.py
# Genera AAAA-MM-DD_<tema>.jpg (feed 1080x1350) y _estado.jpg (1080x1920) en la raíz.
import os,sys,datetime
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFilter
import flyers_deco as fd
from flyers_deco import bold,med,cover,logo,BG,OR,CREAM
HERE=fd.HERE; C=HERE+'/assets/candil/'; A=fd.A
SETS={
 'lamparas_escritorio':('LÁMPARAS DE ESCRITORIO','Para estudiar, trabajar o leer',[
   ('79_l_mpara_de_escritorio_pipo_mesa.jpg','Lámpara Pipo Mesa','Base, E27, brazo flexible','$78.400'),
   ('80_l_mpara_de_escritorio_pipo_pinza.jpg','Lámpara Pipo Pinza','Pinza, E27, brazo flexible','$78.400'),
   ('81_l_mpara_de_escritorio_tablero.jpg','Lámpara Tablero','Articulada, chapa de acero','$107.300'),
   ('82_l_mpara_de_escritorio_serena.jpg','Lámpara Serena','E27, estructura de madera','$125.600')]),
 'veladores':('VELADORES','Luz suave para tu mesa de luz',[
   ('87_l_mpara_de_mesa_recargable_softy.jpg','Velador Softy','Recargable, luz arriba y abajo','$44.900'),
   ('88_l_mpara_de_mesa_recargable_spicy.jpg','Velador Spicy','Recargable, luz arriba y abajo','$46.600'),
   ('89_l_mpara_de_mesa_recargable_indu.jpg','Velador Indu','Recargable, 36 cm, regulable','$89.400'),
   (A+'petit_cobre-colores.png','Velador Petit','Táctil, aluminio cobre','$36.300')]),
 'apliques':('APLIQUES DE CABECERA','Leé tranquilo sin ocupar la mesa de luz',[
   ('83_aplique_de_cabecera_fiona_e14.jpg','Aplique Fiona','E14, estructura de madera','$54.100'),
   ('85_aplique_de_cabecera_led_aki.jpg','Aplique LED Aki','LED 5 W, aluminio','$102.300'),
   ('86_aplique_de_cabecera_led_neo.jpg','Aplique LED Neo','LED 6,5 W, aluminio','$114.000')]),
}
def photo(path,w,h):
    im=Image.open(path if path.startswith('/') else C+path).convert('RGB')
    bg=cover(im,w,h).filter(ImageFilter.GaussianBlur(18))
    r=min(w/im.width,h/im.height); fg=im.resize((int(im.width*r),int(im.height*r)))
    bg.paste(fg,((w-fg.width)//2,(h-fg.height)//2)); return bg
def rmask(size,r=32):
    m=Image.new('L',size,0); ImageDraw.Draw(m).rounded_rectangle((0,0,size[0]-1,size[1]-1),r,fill=255); return m
def flyer(key):
    title,sub,items=SETS[key]; W,H=1080,1350
    c=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(c)
    d.rectangle((60,60,150,66),fill=OR)
    d.text((60,90),title,font=bold(88 if len(title)<14 else 66),fill=(255,255,255))
    d.text((62,200),sub,font=med(36),fill=(210,210,210))
    for i,(f,n,s,p) in enumerate(items):
        if i<4 and not (len(items)==3 and i==2):
            x=60+(i%2)*510; y=270+(i//2)*450; card=Image.new('RGB',(470,440),CREAM)
            card.paste(photo(f,470,300),(0,0)); cd=ImageDraw.Draw(card)
            cd.text((24,312),n,font=bold(28),fill=(20,20,20)); cd.text((24,350),s,font=med(21),fill=(110,110,110)); cd.text((24,380),p,font=bold(36),fill=(215,115,15))
            c.paste(card,(x,y),rmask(card.size))
        else:
            card=Image.new('RGB',(980,420),CREAM); card.paste(photo(f,490,420),(0,0)); cd=ImageDraw.Draw(card)
            cd.text((530,100),n,font=bold(36),fill=(20,20,20)); cd.text((530,150),s,font=med(26),fill=(110,110,110)); cd.text((530,210),p,font=bold(60),fill=(215,115,15))
            c.paste(card,(60,735),rmask(card.size))
    d.rounded_rectangle((60,1170,1040,1316),30,fill=OR)
    lg=logo.copy(); lg.thumbnail((290,80)); d.rounded_rectangle((78,1186,378,1300),20,fill=CREAM); c.paste(lg,(78+(300-lg.width)//2,1186+(114-lg.height)//2),lg)
    d.text((415,1184),'Pedí por WhatsApp',font=med(30),fill=(20,20,20)); d.text((415,1220),'351 349 8646',font=bold(48),fill=(20,20,20))
    d.text((415,1280),'Recta Martinoli 8791 · Córdoba',font=med(22),fill=(20,20,20))
    return c
if __name__=='__main__':
    day=sys.argv[1] if len(sys.argv)>1 else datetime.date.today().isoformat()
    for k in SETS:
        f=flyer(k); f.save(f'{HERE}/{day}_{k}.jpg',quality=95); fd.story(f,'NOVEDAD EN DIME').save(f'{HERE}/{day}_{k}_estado.jpg',quality=95)
