# Dime Iluminación y Electricidad – plan de redes (para ejecutar en sesiones programadas)

Negocio: Recta Martinoli 8791, Córdoba. WhatsApp 351 349 8646. Instagram @dime_iluminacion (Windsor connector `instagram`, cuenta 17841441557324448).
Tienda online (usar SIEMPRE este link corto en captions y mensajes): https://tinyurl.com/Dimeilumina  (el original es https://claude.ai/artifact/5dZ5V7nhw8FvUB4SeBL7b7). Nombre de la tienda: Dime Iluminación.
Promo diciembre: descuento especial pagando en EFECTIVO (no inventar porcentaje).

## Productos y precios de venta (IVA incluido)
- Colgante Hersh soga y metal: $62.900 (assets/hersh_armado.jpg, hersh_kit.png)
- Colgante Mann blanco: $71.200 (mann_blanco.png, mann_ambiente.png)
- Colgante Tas 100 negro lineal LED 120 cm: $125.800 (tas-100-colgante_negro-ambiente.png)
- Colgante Jade Hexagon negro LED: $232.300 (jade-hexagon_negro.png)
- Plafón Medusa Wood 5 luces negro: $157.300 (medusa-wood-5-luces_negro.png, _ambiente.png)
- Plafón Gad negro/blanco: $203.300 (gad_negro.png, gad_blanco.png, gad_ambiente.png)
- Plafón Bag 30 cm negro/blanco: $145.200 (bag-30cm_blanco.png, bag-30cm_ambiente.png)
- Velador Petit táctil cobre: $36.300 (petit_cobre-colores.png)

## Estilo de flyer (ver flyer_colgantes.jpg y flyer_colgantes_estado.jpg)
Fondo gris oscuro #202020, naranja #F7941E, títulos blancos en Poppins Bold (/usr/share/fonts/truetype/google-fonts/), tarjetas blancas con foto, nombre, descripción y precio naranja, pie naranja con logo (assets/logo_orig.png), "Pedí por WhatsApp 351 349 8646" y "Recta Martinoli 8791 · Córdoba".
Feed: 1080x1350 JPG. Historia/estado: 1080x1920 JPG (flyer centrado, título "NOVEDAD EN DIME" arriba).

## Publicar
Subir el JPG a este repo (rama main) y usar la URL https://raw.githubusercontent.com/Paola3925/dime-flyers/main/<archivo>.jpg con Windsor `create_image_post` / `create_story` (connector instagram). Caption: gancho corto + precio + WhatsApp + dirección + 10 a 12 hashtags (#iluminacion #colgantes #decoracion #diseñodeinteriores #cordoba #cordobaargentina #iluminacioncordoba #deco #hogar #arquitectura #electricidad). Nombrar archivos con fecha: AAAA-MM-DD_tema.jpg.

## Calendario (hasta 24/12/2026)
Sem 26/11-2/12 colgantes y plafones. 3-9/12 luces decorativas y veladores de regalo. 10-16/12 ambientá tus fiestas. 17-24/12 última semana, retiro rápido y horarios.
Lun feed + historia. Mar historia consejo/encuesta. Mié reel (no se puede crear video: usar historia). Jue feed. Vie historia "para el finde". Sáb historia/consejo. Dom nada en Instagram.
Siempre dejar el flyer vertical para el estado de WhatsApp y avisar por push (la dueña lo sube a mano; WhatsApp no tiene API de estados).

## Luces decorativas (proveedor Topluva) – flyers ya armados
Fotos recortadas en assets/deco/. Script flyers_deco.py: completar el dict PRICES con los precios de venta cuando la dueña los pase (regla: costo x2 x1,21 redondeado a $100) y volver a correrlo para regenerar los flyers con precio. Mientras no haya precio los flyers dicen "Consultá precio".
Flyers listos (feed 1080x1350 y vertical *_estado.jpg 1080x1920) en la raíz del repo: deco_navidad.jpg (cortinas y guirnaldas de Navidad), deco_solares.jpg (guirnaldas y mangueras solares), deco_rincon.jpg (ramo de hadas, velas solares, árbol cerezo, lámpara de pared).
Orden sugerido: lun 30/11 feed deco_navidad; jue 3/12 feed deco_solares; lun 7/12 feed deco_rincon; los días de historia usar las versiones *_estado.jpg de esos mismos tres. Hasta el 24/12 priorizar Navidad y solares. Si faltan precios, el caption dice "Consultá precio por WhatsApp 351 349 8646".
Antes de publicar cualquiera de estos, confirmar con la dueña que el producto está en stock en el local (no prometer disponibilidad).

Suma (26/11): deco_kermes.jpg y deco_kermes_estado.jpg = Kermés solar de 5 m con lámparas vintage (fotos en assets/deco/kermes_*.png). Publicar jueves 10/12 en feed y como historia el viernes 11/12. Precio pendiente: PRICES['kermes_solar'] en flyers_deco.py.

## Recordatorio diario de estados de WhatsApp Business (la dueña los sube a mano)
Cada mañana se le avisa a Paola qué subir hoy al estado de WhatsApp Business (máx. 2 por día). Reglas: (1) incluir siempre el flyer vertical *_estado.jpg del post de Instagram previsto para hoy según el calendario; (2) sumar un segundo de la rotación: deco_kermes, deco_navidad, deco_solares, deco_rincon, flyer_colgantes, 2026-11-26_plafones (y los flyers nuevos que haya en la raíz), sin repetir el mismo dos días seguidos; (3) en diciembre priorizar Navidad, kermés y solares; (4) texto sugerido corto con el link de la tienda https://tinyurl.com/Dimeilumina y "Pagando en efectivo tenés descuento". Los últimos días (21 a 24/12) avisar horarios y retiro rápido. Ya subidos hoy 26/11: kermés y navidad (pendiente de confirmar). Si Paola dice que ya publicó algo, anotarlo acá.

TikTok (la dueña lo sube a mano, no hay API de publicación): 1 video por día, idealmente 19 a 21 h. Usar los .mp4 del repo (reel_colgantes y los nuevos); si no hay video nuevo, armar uno con reel_build.py. El recordatorio diario (9:07 h) incluye descripción, hashtags y música sugerida.

## Productos Candil en la tienda (ids 79-89) – flyers listos con precio (26/11)
Ya están en la tienda con precio de venta, se publican CON precio (los precios son los de la tienda; no inventar otros). Script: flyers_candil.py (datos y fotos en assets/candil/).
- 2026-11-26_lamparas_escritorio(.jpg/_estado.jpg): Pipo Mesa $78.400, Pipo Pinza $78.400, Tablero $107.300, Serena $125.600.
- 2026-11-26_veladores(.jpg/_estado.jpg): Softy $44.900, Spicy $46.600, Indu $89.400, Petit táctil $36.300.
- 2026-11-26_apliques(.jpg/_estado.jpg): Fiona $54.100, Aki $102.300, Neo $114.000. (Bonnie LED dimerizable $101.800 quedó afuera: sumarla en un próximo flyer.)
Orden sugerido (historias): vie 27/11 lamparas_escritorio_estado; sáb 28/11 veladores_estado; mar 1/12 apliques_estado. Las versiones feed (1080x1350) sirven como reemplazo de lunes/jueves si falta confirmar stock de las luces decorativas. En las historias de regalo (semana 3-9/12) reutilizar veladores.

## Regla de la dueña (26/11): todo lo que se carga en la tienda también va a las redes
Cuando la dueña pase material (productos, fotos, listas) y se cargue en la tienda, ese mismo material se usa para armar flyers para todas las redes: Instagram (feed 1080x1350 e historia 1080x1920), TikTok y estado de WhatsApp (vertical 1080x1920, el mismo *_estado.jpg) y Google (publicación de Google Business Profile con el flyer de feed). Usar siempre los precios de la tienda.
Imágenes: antes de armar, revisar que cada producto tenga foto buena (nítida, de al menos ~600 px de lado, sin marcas de agua ni texto encima). Si falta foto, es chica o borrosa, o hay un producto sin precio en la tienda, armar igual lo que se pueda y pedirle a la dueña en la notificación la foto o el dato que falta (nombrando el producto). Fotos de ambiente (producto instalado) rinden más en Instagram y TikTok que el fondo blanco.

## Rol (26/11): publicista y mano derecha de la dueña
La dueña me delegó todo el marketing de Dime: planificar, armar y publicar contenido, responder a clientes, cuidar la imagen y proponer ideas, sin pedir aprobación por cada paso. Si falta material (fotos, precios, datos, stock), se lo pido en la notificación, concreto y corto.
Canales conectados en Windsor (26/11): Instagram (publica), Google Business Profile (cuenta locations/5480672217782500635: create_local_post para publicar, reply_to_review para responder reseñas) y TikTok (solo comentarios: no se puede publicar, la dueña sube el vertical a mano). Publicar también en Google Business con el flyer de feed (misma info y precios) y responder reseñas con tono cálido y breve, sin prometer stock ni descuentos con porcentaje; reseñas negativas o delicadas: no responder y avisar.

## Veladores infantiles $22.000 (28/11) – cargados en la tienda (ids 99-103)
Conejo con overol, chanchito con hoja, astronauta con nube, osito con portaobjetos y el de bandeja: todos $22.000 en la tienda, fotos sin fondo en assets/infantiles/ (generadas con rembg sobre las fotos de la dueña; script flyers_infantiles.py). Flyer: 2026-11-28_veladores_infantiles(.jpg/_estado.jpg), precio 'Cada uno $22.000'. Para sacar fondos: fotos con el producto solo, enfocado; si el producto es blanco, usar fondo oscuro. Pendiente: modelo astronauta en cápsula verde (foto con fondo claro, no salió el recorte) y precio de los veladores infantiles viejos (ids 91-98, 'Consultar precio') a confirmar con la dueña. Sugerido: historia mar 1/12 o vie 4/12 y regalo en semana 3-9/12.

## Velador panda y elefante $43.000 (28/11)
Tienda: panda (id 92) reemplazado por la foto nueva sin fondo, con luz azul retocada (la foto blanca queda como segunda imagen) y elefante (id 91): ambos $43.000. Flyer: 2026-11-28_veladores_figuras(.jpg/_estado.jpg) con 'Cada uno $43.000' (script flyers_panda_elefante.py, imágenes en assets/infantiles/). Pendiente de precio: capibaras, honguitos y conejito (ids 93, 94, 97, 98).

## Reprogramación (sáb 28/11) tras fotos nuevas de la dueña
Sáb 28/11 historia: veladores_infantiles_estado (publicada). Dom 29/11: nada en Instagram (recordar foto del local al estado).
Lun 30/11 feed: 2026-11-28_veladores_infantiles (regalo de Navidad, $22.000 c/u). Mar 1/12 historia: apliques_estado. Mié 2/12 historia: veladores_figuras_estado (panda/elefante $43.000). Jue 3/12 feed: veladores_figuras o deco_solares si la dueña confirma stock y pasa precios. Vie 4/12 historia: veladores_infantiles_estado o lamparas. Luces decorativas/navideñas: esperar fotos reales + precio + stock de la dueña antes de publicar.
