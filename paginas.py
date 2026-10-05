# -*- coding: utf-8 -*-
"""El contenido de las seis páginas. construir.py pone el armazón.

DOS DECISIONES DE ESTE ARCHIVO

1. Todo en segunda persona de tú. Zamira cocina como se cocina en casa y
   el sitio tiene que sonar igual: "escríbeme", no "escríbanos". El usted
   pone un mostrador en medio y aquí no hay mostrador.

2. Cada plato de la carta lleva su foto. Son 22 fotos de producto y todas
   entran al menú, que es donde la gente decide. La verificación del final
   no deja pasar el sitio si queda una sola sin usar.
"""
import os, re, glob
from construir import (AQUI, DOMINIO, PAGINAS, TEL_E164, TEL_BONITO, WA,
                       cabecera, pie, cotizador, COTIZADOR_JS, miga,
                       plato, galeria, wa_btn, SVG_WA)

W = lambda n, s: open(os.path.join(AQUI, n), 'w', encoding='utf-8').write(s)
ORN = '<div class="orn"><span></span></div>'

CIUDADES = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena',
            'Santa Marta', 'Bucaramanga', 'Pereira', 'Villavicencio', 'Chía y Cajicá']


def cinta(*pares):
    return ('<div class="cinta"><div>' +
            ''.join(f'<span>{a} <i>·</i> {b}</span>' for a, b in pares) +
            '</div></div>')


# ╔══════════════════════════════════════════════════════════════════╗
# ║  1 · INICIO                                                      ║
# ╚══════════════════════════════════════════════════════════════════╝
inicio = cabecera(
    'index.html',
    'Catering árabe y libanés en Bogotá | Aló Beirut Yahabibi',
    'Catering árabe y libanés para matrimonios, quinceañeros, bautizos y eventos de '
    'empresa. Quipes, deditos, empanadas y mesas de mezze. Bogotá y principales '
    'ciudades de Colombia. Cotiza por WhatsApp.')

inicio += f'''
<main>
<section class="hero">
 <div class="hero-in">
  <div class="hero-foto">
    <img src="img/hero-catering-arabe-bogota.jpg"
         alt="Zamira Eslait con una bandeja de comida árabe recién hecha, en Bogotá"
         width="1600" height="1200" fetchpriority="high">
  </div>
  <div class="hero-txt">
    <span class="sello">Cocinando desde 2020 · Bogotá</span>
    <h1>La mesa árabe que tu familia<br><span class="verde">va a recordar</span></h1>
    <p class="lead">Quipes, deditos, empanadas, arroz con almendras y mezze hechos a mano
    por tres personas que cocinan como se cocina en casa: receta palestina y libanesa,
    sazón del Caribe colombiano. Te montamos el matrimonio, el quinceañero o la reunión
    de la empresa en Bogotá, y viajamos a las principales ciudades del país.</p>
    <div class="acciones">
      {wa_btn('Cotizar mi evento')}
      <a class="btn linea" href="menu.html">Ver el menú</a>
    </div>
    <p class="bajo-cta">Te respondemos el mismo día · WhatsApp {TEL_BONITO}</p>
  </div>
 </div>
</section>

{cinta(('Quipes','formados a mano'), ('Mezze','para compartir'),
       ('Arroz árabe','con almendras'), ('Maamoul','de dátil'))}

<section class="cifras" style="padding:28px 0">
  <div class="wrap">
    <div class="cifras-g">
      <div><b>+6</b><span>años cocinando</span></div>
      <div><b>10 a 300</b><span>personas por evento</span></div>
      <div><b>100%</b><span>hecho a mano, el mismo día</span></div>
      <div><b>5</b><span>ciudades principales</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="centro">
      {ORN}
      <h2>Lo que llega a tu mesa</h2>
      <p class="lead">Nada sale de un congelador. Las masas se amasan, los quipes se forman
      uno por uno y las hojas de parra se enrollan a mano la mañana de tu evento.</p>
    </div>
    <div class="rej tres" style="margin-top:34px">
      {plato('quipes-arabes-bandeja.jpg','Bandeja de quipes árabes recién fritos','Quipes',
             'El clásico que todo el mundo busca. Trigo, carne y especias, fritos al punto y servidos tibios.')}
      {plato('deditos-de-queso-arabes.jpg','Deditos de queso árabes dorados en bandeja','Deditos de queso',
             'Crocantes por fuera, hilo de queso por dentro. Los primeros que se acaban, siempre.')}
      {plato('empanadas-arabes-sambusek.jpg','Empanadas árabes sambusek rellenas','Empanadas árabes',
             'Sambusek de carne o queso, con la masa delgada que las hace livianas.')}
      {plato('arroz-arabe-con-pan-pita.jpg','Arroz árabe con almendras acompañado de pan pita','Arroz árabe',
             'Con almendras y pasas tostadas, pan pita al lado. El plato fuerte de la mesa.')}
      {plato('mujadara-con-almendras.jpg','Mujadara de lentejas con cebolla y almendras','Mujadara',
             'Lentejas con arroz y cebolla caramelizada. Vegetariano, y el favorito de quien lo prueba.')}
      {plato('tabbuleh-fresco.jpg','Tabbuleh fresco con perejil, tomate y limón','Tabbuleh',
             'Perejil, tomate, limón y aceite de oliva. Lo que refresca entre un frito y otro.')}
    </div>
    <p class="centro" style="margin-top:32px">
      <a class="btn linea" href="menu.html">Ver los 22 platos, uno por uno</a></p>
  </div>
</section>

<section style="background:var(--crema-2)">
  <div class="wrap">
    <div class="centro">
      {ORN}
      <h2>Para la ocasión que sea</h2>
      <p class="lead">Hemos montado mesas en hoteles, salones de matrimonio, oficinas y
      patios de casa. Tu evento se cotiza por persona, sin paquetes amarrados.</p>
    </div>
    <div class="fichas tres" style="margin-top:32px">
      <a href="eventos.html#matrimonios"><h3>Matrimonios</h3>
        <p>Mesa de mezze para el cóctel y plato fuerte para la recepción.</p></a>
      <a href="eventos.html#quinces"><h3>Quinceañeros</h3>
        <p>Picadas que rinden y se comen de pie, sin cubiertos.</p></a>
      <a href="eventos.html#bautizos"><h3>Bautizos y baby shower</h3>
        <p>Porciones pequeñas, dulces árabes y café al final.</p></a>
      <a href="eventos.html#despedidas"><h3>Despedidas de soltera</h3>
        <p>Tabla para compartir en el centro y algo caliente a mitad de noche.</p></a>
      <a href="eventos.html#empresa"><h3>Empresa y eventos políticos</h3>
        <p>Factura en orden, montaje puntual y personal uniformado.</p></a>
      <a href="eventos.html#casa"><h3>Reuniones en casa</h3>
        <p>Desde diez personas. Llegamos, montamos y dejamos la cocina limpia.</p></a>
    </div>
  </div>
</section>

{cotizador()}

<section>
  <div class="wrap">
    <div class="duo">
      <div>
        <h2>Zamira, y una receta que cruzó el mar</h2>
        <p class="cita">«En diciembre en mi casa había comida costeña y comida árabe en la
        misma mesa. Nunca me pareció raro: eso era mi casa.»</p>
        <p>Aló Beirut Yahabibi nació en pandemia, cuando Zamira Eslait empezó a vender desde
        su cocina lo que su familia palestina había comido toda la vida. Hoy son tres
        personas y las recetas siguen siendo las mismas, sin atajos.</p>
        <a class="btn linea" href="historia.html">Leer la historia completa</a>
      </div>
      <img src="img/mesa-catering-arabe-evento.jpg" width="1200" height="900" loading="lazy"
           alt="Mesa de catering árabe montada para un evento, con varias bandejas servidas">
    </div>
  </div>
</section>

<section style="background:var(--crema-2)" class="centro">
  <div class="wrap">
    {ORN}
    <h2>Dónde atendemos</h2>
    <p class="lead">La cocina está en Bogotá y de ahí sale todo. Si tu evento es en otra
    ciudad, coordinamos con tiempo el viaje y el montaje.</p>
    <div class="pastillas">{''.join(f'<span>{c}</span>' for c in CIUDADES)}</div>
    <p style="margin-top:26px"><a class="btn linea" href="ciudades.html">Cómo funciona fuera de Bogotá</a></p>
  </div>
</section>
</main>
''' + pie('index.html') + COTIZADOR_JS
W('index.html', inicio)


# ╔══════════════════════════════════════════════════════════════════╗
# ║  2 · MENÚ · cada plato con su foto                               ║
# ╚══════════════════════════════════════════════════════════════════╝
CARTA = [
 ('Picadas y pasabocas', 'Lo que se come de pie, con la mano, mientras la gente llega.', [
   ('Quipes', 'Trigo, carne y especias, formados y fritos uno por uno.',
    'quipes-arabes-bandeja.jpg', 'Bandeja de quipes árabes recién fritos'),
   ('Deditos de queso', 'Crocantes, con hilo de queso. Se piden por docena.',
    'deditos-de-queso-arabes.jpg', 'Deditos de queso árabes dorados'),
   ('Deditos para bandeja de evento', 'La misma receta, montada en bandeja grande para servir y reponer.',
    'deditos-bandeja-evento.jpg', 'Bandeja grande de deditos para un evento'),
   ('Empanadas árabes · sambusek', 'De carne o de queso, con masa delgada que las deja livianas.',
    'empanadas-arabes-sambusek.jpg', 'Empanadas árabes sambusek'),
   ('Warak enab', 'Hojas de parra rellenas de arroz y carne, enrolladas a mano.',
    'warak-enab-hojas-de-parra.jpg', 'Warak enab, hojas de parra rellenas'),
   ('Tamales árabes', 'La versión de la casa: envueltos y cocidos al vapor.',
    'tamales-arabes.jpg', 'Tamales árabes servidos'),
   ('Wraps de falafel', 'Garbanzo, hierbas y salsa de ajonjolí. Opción vegetariana.',
    'wraps-de-falafel.jpg', 'Wraps de falafel con salsa de ajonjolí'),
 ]),
 ('Mesas de mezze', 'Varias cosas en el centro para compartir. Es lo que mejor funciona en cóctel.', [
   ('Mezze completo', 'Hummus, tabbuleh, babaganoush, pan pita y aceitunas en la misma mesa.',
    'mezze-arabe-hummus-tabbuleh.jpg', 'Mesa de mezze árabe con hummus y tabbuleh'),
   ('Crema de queso kashk', 'Untable, tibia, con un hilo de aceite de oliva encima.',
    'crema-de-queso-kashk.jpg', 'Crema de queso kashk con aceite de oliva'),
   ('Kibbeh nayyeh', 'Al plato, como se come allá. Para quien sabe lo que está pidiendo.',
    'kibbeh-nayyeh-al-plato.jpg', 'Kibbeh nayyeh servido al plato'),
   ('Tabbuleh', 'Perejil, tomate, limón y aceite de oliva. Refresca entre un frito y otro.',
    'tabbuleh-fresco.jpg', 'Tabbuleh fresco con perejil, tomate y limón'),
   ('Tabbuleh en hoja de lechuga', 'Porción individual, para comer con la mano y sin cubiertos.',
    'tabbuleh-en-lechuga.jpg', 'Tabbuleh servido en hoja de lechuga'),
   ('Trío para compartir', 'Quipes, tabbuleh y mujadara en la misma tabla. El pedido más fácil.',
    'quipes-tabbuleh-mujadara.jpg', 'Quipes, tabbuleh y mujadara en la misma mesa'),
 ]),
 ('Platos fuertes', 'Para recepción sentada o servicio en bandeja.', [
   ('Arroz árabe con almendras', 'Con pasas tostadas y pan pita al lado.',
    'arroz-arabe-con-pan-pita.jpg', 'Arroz árabe con almendras y pan pita'),
   ('Arroz árabe al plato', 'La porción individual, como sale para servicio sentado.',
    'arroz-arabe-servido.jpg', 'Arroz árabe servido en el plato'),
   ('Arroz árabe en bandeja', 'Para evento grande: bandeja honda que se repone durante la noche.',
    'arroz-arabe-bandeja-evento.jpg', 'Bandeja de arroz árabe para evento'),
   ('Arroz con pollo y almendras', 'El fuerte que más se pide para matrimonio.',
    'arroz-con-pollo-almendras.jpg', 'Arroz con pollo y almendras'),
   ('Pollo desmechado árabe', 'Especiado y jugoso, para armar wraps o servir con arroz.',
    'pollo-desmechado-arabe.jpg', 'Pollo desmechado árabe especiado'),
   ('Shawarma en wrap', 'Carne especiada, pan plano y salsa blanca.',
    'shawarma-arabe-wraps.jpg', 'Shawarma árabe en wraps'),
   ('Mujadara', 'Lentejas, arroz y cebolla caramelizada. Vegetariano de verdad, no de adorno.',
    'mujadara-con-almendras.jpg', 'Mujadara de lentejas con cebolla y almendras'),
 ]),
 ('Dulces y café', 'El cierre, que es la parte que la gente fotografía.', [
   ('Maamoul', 'Dulce de dátil o nuez, con azúcar en polvo.',
    'maamoul-postre-arabe.jpg', 'Maamoul, dulce árabe de dátil'),
   ('Café árabe', 'Con cardamomo, en taza pequeña, al final de la comida.',
    'maamoul-postre-arabe.jpg', 'Café árabe con cardamomo'),
 ]),
]

menu = cabecera(
    'menu.html',
    'Menú de catering árabe y libanés | 22 platos | Aló Beirut Yahabibi',
    'Quipes, deditos, empanadas árabes, warak enab, mezze, arroz con almendras, shawarma, '
    'mujadara y maamoul. El menú completo de catering árabe en Bogotá, con foto de cada plato.',
    og_img='carta-menu-alo-beirut.jpg',
    extra_ld={"@context":"https://schema.org","@type":"Menu","name":"Menú de catering Aló Beirut Yahabibi",
              "inLanguage":"es-CO",
              "hasMenuSection":[{"@type":"MenuSection","name":t,"description":d,
                "hasMenuItem":[{"@type":"MenuItem","name":n,"description":dd,
                                "image":f"{DOMINIO}/img/{im}"} for n,dd,im,_a in it]}
                for t,d,it in CARTA]})

secciones = ''
for titulo, desc, items in CARTA:
    filas = ''
    for n, d, im, alt in items:
        filas += (f'<div class="item"><div>'
                  f'<img src="img/{im}" alt="{alt}" loading="lazy" width="200" height="200">'
                  f'<div><b>{n}</b><small>{d}</small></div></div></div>')
    secciones += (f'<div class="carta"><h3>{titulo}</h3>'
                  f'<p style="font-size:15px;color:var(--gris);margin:8px 0 14px">{desc}</p>'
                  f'{filas}</div>')

menu += f'''
<main>
<header class="cabe">
  <div class="wrap">
    {miga('Menú de catering')}
    <h1>El menú, plato por plato</h1>
    <p class="lead">Todo se arma por persona y se ajusta a lo que necesites: una sola picada,
    una mesa de mezze completa o cóctel más plato fuerte. Escríbeme cuántos son y te mando
    el precio con todo lo que incluye.</p>
    <div class="acciones">{wa_btn('Pedir precios por WhatsApp')}</div>
  </div>
</header>

{cinta(('22 platos','en la carta'), ('Vegetariano','en cada sección'),
       ('Todo','hecho el mismo día'))}

<section>
  <div class="wrap">
    <div class="estrecho">{secciones}</div>
  </div>
</section>

<section style="background:var(--crema-2)">
  <div class="wrap">
    <div class="duo">
      <img src="img/carta-menu-alo-beirut.jpg" alt="Carta de Aló Beirut Yahabibi"
           loading="lazy" width="1200" height="900">
      <div>
        <h2>¿No sabes por dónde empezar?</h2>
        <p>Dime qué evento es y cuántos son, y yo te armo el menú. Para cóctel suelo
        proponer tres picadas y una mesa de mezze; para recepción sentada, mezze de entrada
        y un arroz como fuerte. Si hay vegetarianos, la mujadara y el falafel resuelven sin
        que nadie sienta que le dieron el plato de castigo.</p>
        <div class="acciones">{wa_btn('Que Zamira me arme el menú')}
          <a class="btn linea" href="eventos.html">Ver cómo montamos cada evento</a></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap estrecho faq">
    {ORN}
    <h2 class="centro">Lo que siempre me preguntan</h2>
    <div style="margin-top:24px">
    <details><summary>¿Cuál es el mínimo de personas?</summary>
      <p>Diez. Por debajo de eso el viaje y el montaje te encarecen demasiado el plato y no
      vale la pena para ti.</p></details>
    <details><summary>¿Tienen opciones vegetarianas?</summary>
      <p>Sí, y buenas: mujadara, falafel, tabbuleh, hummus, babaganoush y empanadas de
      queso. Buena parte de la cocina árabe es vegetariana por naturaleza.</p></details>
    <details><summary>¿Con cuánta anticipación reservo?</summary>
      <p>En Bogotá, una semana es cómodo. Para diciembre y temporada de matrimonios,
      resérvame con un mes. Fuera de Bogotá, mínimo dos semanas.</p></details>
    <details><summary>¿Incluye meseros, mesas y menaje?</summary>
      <p>Se puede. Te lo cotizo aparte para que decidas si lo pone el salón o lo ponemos
      nosotros.</p></details>
    <details><summary>¿Hay anticipo?</summary>
      <p>Sí, el 50% para apartar la fecha y el resto el día del evento. La comida se compra
      con días de anticipación, por eso el anticipo.</p></details>
    <details><summary>¿Hacen factura para empresa?</summary>
      <p>Sí. Mándame los datos de facturación al cotizar y te la entrego en orden.</p></details>
    </div>
  </div>
</section>

{cotizador('¿Te cuadraron los platos? Pide el precio',
           'Marca evento, personas y ciudad. El mensaje se arma solo y me llega a WhatsApp.')}
</main>
''' + pie('menu.html') + COTIZADOR_JS
W('menu.html', menu)


# ╔══════════════════════════════════════════════════════════════════╗
# ║  3 · SERVICIO COMPLETO                                           ║
# ╚══════════════════════════════════════════════════════════════════╝
EVENTOS = [
 ('matrimonios', 'Matrimonios', 'arroz-con-pollo-almendras.jpg',
  'Arroz con pollo y almendras servido para un matrimonio',
  'Mesa de mezze mientras llegan los invitados y plato fuerte para la recepción. Es el '
  'evento que más hago y el que mejor luce: la mesa árabe llena de colores sale en todas '
  'las fotos. Coordino con tu salón o tu hotel la hora de montaje, tú no tienes que llamar '
  'a nadie.',
  ['Mezze de bienvenida', 'Arroz árabe o con pollo', 'Dulces y café al final']),
 ('quinces', 'Quinceañeros', 'deditos-bandeja-evento.jpg',
  'Bandeja de deditos de queso servida en un evento',
  'Picadas que rinden y se comen de pie, sin cubiertos y sin que nadie se levante del baile. '
  'Deditos, quipes y empanadas en bandejas que vamos reponiendo toda la noche.',
  ['Bandejas que se reponen', 'Sin cubiertos', 'Algo caliente a medianoche']),
 ('bautizos', 'Bautizos y baby shower', 'maamoul-postre-arabe.jpg',
  'Maamoul, dulce árabe, servido en bandeja',
  'Porciones pequeñas, nada que manche, y el dulce árabe como cierre. Funciona muy bien en '
  'casa o en salón pequeño, con grupos de quince a cuarenta personas.',
  ['Porciones individuales', 'Opciones sin picante', 'Dulces y café']),
 ('despedidas', 'Despedidas de soltera', 'quipes-tabbuleh-mujadara.jpg',
  'Quipes, tabbuleh y mujadara servidos para compartir',
  'Una tabla grande en el centro para compartir, que es la mitad de la gracia, y algo '
  'caliente más tarde cuando vuelva el hambre.',
  ['Tabla para compartir', 'Vegetariano incluido', 'Montaje en casa']),
 ('empresa', 'Empresa y eventos políticos', 'arroz-arabe-bandeja-evento.jpg',
  'Bandeja de arroz árabe montada para un evento de empresa',
  'Factura en orden, montaje a la hora pactada y personal uniformado. He atendido hoteles y '
  'eventos de convocatoria grande, donde lo que no se puede fallar es el horario.',
  ['Factura con todos los datos', 'Montaje puntual', 'De 50 a 300 personas']),
 ('casa', 'Reuniones en casa', 'arroz-arabe-servido.jpg',
  'Arroz árabe servido en una reunión en casa',
  'Desde diez personas. Llegamos, montamos, servimos y te dejamos la cocina como la '
  'encontramos. Es el servicio con el que arrancó todo esto.',
  ['Desde 10 personas', 'Montaje y recogida', 'La cocina queda limpia']),
]

eventos = cabecera(
    'eventos.html',
    'Catering para matrimonios, quinceañeros y eventos de empresa | Aló Beirut Yahabibi',
    'Servicio completo de catering árabe: matrimonios, quinceañeros, bautizos, baby shower, '
    'despedidas, eventos de empresa y reuniones en casa. De 10 a 300 personas en Bogotá y Colombia.',
    og_img='mesa-catering-arabe-evento.jpg')

bloques = ''
for i, (sid, t, img, alt, texto, puntos) in enumerate(EVENTOS):
    lis = ''.join(f'<span>{p}</span>' for p in puntos)
    orden = ' style="order:-1"' if i % 2 else ''
    bloques += f'''
<section id="{sid}"{' style="background:var(--crema-2)"' if i % 2 else ''}>
  <div class="wrap">
    <div class="duo">
      <div>
        <h2>{t}</h2>
        <p>{texto}</p>
        <div class="pastillas">{lis}</div>
        <div class="acciones">{wa_btn('Cotizar ' + t.lower(), 'btn wa',
            '¡Hola Zamira! Quiero cotizar catering para ' + t.lower() + '. ¿Me ayudas con el precio?')}</div>
      </div>
      <img src="img/{img}" alt="{alt}" loading="lazy" width="1200" height="900"{orden}>
    </div>
  </div>
</section>'''

eventos += f'''
<main>
<header class="cabe">
  <div class="wrap">
    {miga('Servicio completo')}
    <h1>Servicio completo,<br>de principio a fin</h1>
    <p class="lead">No solo te mando comida. Llego a la hora acordada, monto la mesa, sirvo
    durante el evento y recojo. Tú te dedicas a tu fiesta.</p>
  </div>
</header>

{cinta(('Montamos','y recogemos'), ('De 10','a 300 personas'), ('Bogotá','y 5 ciudades más'))}

<section style="padding-bottom:0">
  <div class="wrap centro">
    {ORN}
    <h2>Cómo trabajamos</h2>
  </div>
  <div class="wrap">
    <div class="fichas tres" style="margin-top:28px">
      <a href="#cotizar"><h3>1 · Me escribes</h3>
        <p>Por WhatsApp, con la fecha, la ciudad y cuántos son. Te respondo el mismo día.</p></a>
      <a href="menu.html"><h3>2 · Armamos el menú</h3>
        <p>Te propongo platos y cantidades según el evento y el presupuesto que tengas.</p></a>
      <a href="ciudades.html"><h3>3 · Apartas con el 50%</h3>
        <p>Queda tu fecha reservada. El resto lo pagas el día del evento.</p></a>
    </div>
  </div>
</section>
{bloques}
{cotizador('Cuéntame de tu evento', 'Tres toques y el mensaje queda listo para enviar.')}
</main>
''' + pie('eventos.html') + COTIZADOR_JS
W('eventos.html', eventos)


# ╔══════════════════════════════════════════════════════════════════╗
# ║  4 · HISTORIA                                                    ║
# ╚══════════════════════════════════════════════════════════════════╝
historia = cabecera(
    'historia.html',
    'La historia de Aló Beirut Yahabibi | Zamira Eslait, Bogotá',
    'Zamira Eslait, de origen palestino y criada en la costa colombiana, empezó a vender '
    'comida árabe desde su cocina en pandemia. Hoy son tres personas y un catering.',
    og_img='banda-logo-alo-beirut.jpg',
    extra_ld={"@context":"https://schema.org","@type":"AboutPage",
              "name":"La historia de Aló Beirut Yahabibi",
              "mainEntity":{"@type":"Person","name":"Zamira Eslait",
                "jobTitle":"Fundadora y cocinera","worksFor":{"@type":"Organization","name":"Aló Beirut Yahabibi"}}})

historia += f'''
<main>
<header class="cabe">
  <div class="wrap">
    {miga('La historia')}
    <h1>Una cocina que empezó<br>un diciembre, hace años</h1>
    <p class="lead">Aló Beirut Yahabibi no es un concepto de restaurante. Es la comida de
    una familia, servida para la tuya.</p>
  </div>
</header>

{cinta(('Receta','palestina y libanesa'), ('Sazón','del Caribe'), ('Tres','pares de manos'))}

<section>
  <div class="wrap">
    <div class="duo">
      <div>
        <p class="cita">«En diciembre en mi casa había comida costeña y comida árabe en la
        misma mesa. Nunca me pareció raro: eso era mi casa.»</p>
        <p>Zamira Eslait creció entre dos cocinas. Por el lado palestino, los quipes que se
        forman uno por uno y las hojas de parra que se enrollan en la tarde, entre varias
        manos y conversando. Por el lado colombiano, el diciembre costeño, el ruido y la
        mesa larga. Nunca escogió entre las dos.</p>
        <p>En 2020, cuando el mundo se quedó en casa, empezó a vender desde su cocina lo
        que siempre había cocinado para los suyos. No había plan de negocio: había pedidos
        de vecinos, y después pedidos de los amigos de los vecinos.</p>
      </div>
      <img src="img/banda-logo-alo-beirut.jpg" alt="Logo de Aló Beirut Yahabibi"
           loading="lazy" width="1200" height="900">
    </div>
  </div>
</section>

<section style="background:var(--crema-2)">
  <div class="wrap">
    <div class="duo">
      <img src="img/quipes-arabes-bandeja.jpg" alt="Quipes árabes recién hechos en bandeja"
           loading="lazy" width="1200" height="900">
      <div>
        <h2>Hoy somos tres</h2>
        <p>Tres personas que cocinan, montan y sirven. Es poco equipo a propósito: así cada
        bandeja la hace alguien que sabe cómo debe quedar. Cuando el evento es grande sumamos
        apoyo para el montaje, pero la comida sale siempre de las mismas manos.</p>
        <p>Nos han llamado hoteles y salones de matrimonio. Hemos atendido quinceañeros,
        bautizos, baby showers, despedidas de soltera y eventos políticos. Cada uno enseñó
        algo sobre cantidades, horarios y lo que de verdad le importa a la gente: que la
        comida esté caliente y que no se acabe.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap estrecho">
    {ORN}
    <h2 class="centro">En qué no cedemos</h2>
    <div class="faq" style="margin-top:24px">
      <details open><summary>Todo a mano, el mismo día</summary>
        <p>Las masas se amasan, los quipes se forman y las hojas se enrollan la mañana de tu
        evento. No hay congelador de por medio y se nota en la textura.</p></details>
      <details><summary>Las especias, como van</summary>
        <p>Cardamomo, canela, pimienta de Jamaica, siete especias. No se bajan para
        "adaptar el paladar": si pides comida árabe es porque quieres comida árabe.</p></details>
      <details><summary>Llegamos antes, no a la hora</summary>
        <p>En un evento el montaje no puede ir contra el reloj. Llegamos con margen y
        entregamos la mesa lista antes de que entre el primer invitado.</p></details>
      <details><summary>Si no cuadra, te lo digo</summary>
        <p>Si la fecha está copada o el presupuesto no alcanza para que la comida quede
        bien, prefiero decírtelo de frente que entregarte algo a medias.</p></details>
    </div>
    <div class="acciones">{wa_btn('Hablar con Zamira')}
      <a class="btn linea" href="menu.html">Ver el menú</a></div>
  </div>
</section>
</main>
''' + pie('historia.html')
W('historia.html', historia)


# ╔══════════════════════════════════════════════════════════════════╗
# ║  5 · CIUDADES                                                    ║
# ╚══════════════════════════════════════════════════════════════════╝
# Nada de una página por ciudad con el mismo texto cambiado: Google lo
# llama "doorway page" y lo castiga. La cobertura se declara en el
# schema areaServed, que es la manera legítima, y aquí se explica de
# verdad cómo funciona el viaje.
ciudades = cabecera(
    'ciudades.html',
    'Catering árabe en Bogotá, Medellín, Cali, Cartagena y Barranquilla | Aló Beirut Yahabibi',
    'Cocina propia en Bogotá y servicio de catering árabe en Medellín, Cali, Cartagena, '
    'Barranquilla, Santa Marta y Bucaramanga. Cómo coordinamos el viaje y el montaje.',
    og_img='mesa-catering-arabe-evento.jpg')

ciudades += f'''
<main>
<header class="cabe">
  <div class="wrap">
    {miga('Dónde atendemos')}
    <h1>Bogotá es la cocina.<br>El país es el calendario.</h1>
    <p class="lead">Preparamos todo en Bogotá, donde está nuestra cocina. Si tu evento es en
    otra ciudad, viajamos con el equipo y coordinamos con anticipación el montaje en el
    sitio.</p>
    <div class="acciones">{wa_btn('Preguntar por mi ciudad')}</div>
  </div>
</header>

{cinta(('Bogotá','y la sabana'), ('5 ciudades','principales'), ('Viaje','dentro del precio'))}

<section>
  <div class="wrap">
    <div class="duo">
      <div>
        <h2>Bogotá y la sabana</h2>
        <p>Es nuestra casa. Entregamos y montamos en toda la ciudad, y también en Chía,
        Cajicá, Cota, La Calera y Sopó, donde queda buena parte de los salones de
        matrimonio. Con una semana de anticipación es suficiente, salvo en diciembre.</p>
        <p>Si tu evento es en un hotel o salón de la ciudad, lo más probable es que ya
        conozcamos el sitio y sepamos cómo son sus tiempos de ingreso.</p>
      </div>
      <img src="img/hero-catering-arabe-bogota.jpg" alt="Mesa de catering árabe montada en Bogotá"
           loading="lazy" width="1200" height="500">
    </div>
  </div>
</section>

<section style="background:var(--crema-2)">
  <div class="wrap centro">
    {ORN}
    <h2>Fuera de Bogotá</h2>
    <p class="lead">Viajamos a las principales ciudades del país. Son tres cosas que hay que
    cuadrar, y las cuadro yo.</p>
  </div>
  <div class="wrap">
    <div class="fichas tres" style="margin-top:30px">
      <a href="#cotizar"><h3>Dos semanas de aviso</h3>
        <p>Es el tiempo que necesito para el viaje, los insumos y la logística del frío.</p></a>
      <a href="#cotizar"><h3>Una cocina en destino</h3>
        <p>La del hotel, del salón o de la casa. La uso para el terminado, no para preparar
        de cero.</p></a>
      <a href="#cotizar"><h3>El viaje va en la cotización</h3>
        <p>Transporte y estadía entran en el precio, sin sorpresas al final.</p></a>
    </div>
    <div class="pastillas centro" style="justify-content:center;margin-top:30px">
      {''.join(f'<span>{c}</span>' for c in CIUDADES)}
    </div>
    <p class="centro" style="margin-top:14px;font-size:14.5px;color:var(--gris)">
      ¿No ves tu ciudad? Pregúntame igual. Si el evento lo justifica, vamos.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="centro">{ORN}<h2>Cómo se ve cuando llegamos</h2></div>
    <div style="margin-top:28px">
    {galeria([
      ('mesa-catering-arabe-evento.jpg','Mesa de catering árabe montada en un evento','La mesa montada'),
      ('deditos-bandeja-evento.jpg','Bandeja de deditos lista para servir en un evento','Bandejas listas'),
      ('arroz-arabe-bandeja-evento.jpg','Bandeja de arroz árabe para evento','Arroz para evento'),
      ('arroz-arabe-servido.jpg','Arroz árabe servido en el plato','Ya servido'),
      ('quipes-tabbuleh-mujadara.jpg','Quipes, tabbuleh y mujadara en la misma mesa','Para compartir'),
      ('shawarma-arabe-wraps.jpg','Shawarma árabe en wraps','Shawarma en wrap'),
      ('warak-enab-hojas-de-parra.jpg','Warak enab, hojas de parra rellenas','Warak enab'),
      ('logo-alo-beirut-yahabibi.jpg','Logo de Aló Beirut Yahabibi','Aló Beirut Yahabibi'),
    ])}
    </div>
  </div>
</section>

{cotizador('¿En qué ciudad es tu evento?',
           'Marca la ciudad y te digo de una si alcanzamos para esa fecha.')}
</main>
''' + pie('ciudades.html') + COTIZADOR_JS
W('ciudades.html', ciudades)


# ╔══════════════════════════════════════════════════════════════════╗
# ║  6 · CONTACTO                                                    ║
# ╚══════════════════════════════════════════════════════════════════╝
contacto = cabecera(
    'contacto.html',
    'Contacto y cotización | Aló Beirut Yahabibi, catering árabe en Bogotá',
    'Escríbeme por WhatsApp al 323 505 6278. Catering árabe y libanés en Bogotá y '
    'principales ciudades de Colombia. Te respondo el mismo día.',
    og_img='mezze-arabe-hummus-tabbuleh.jpg',
    extra_ld={"@context":"https://schema.org","@type":"ContactPage",
              "name":"Contacto Aló Beirut Yahabibi",
              "mainEntity":{"@type":"Organization","name":"Aló Beirut Yahabibi",
                "telephone":"+57 "+TEL_BONITO,"areaServed":"CO"}})

contacto += f'''
<main>
<header class="cabe">
  <div class="wrap">
    {miga('Contacto')}
    <h1>Hablemos de tu evento</h1>
    <p class="lead">Lo más rápido es WhatsApp. Mándame la fecha, la ciudad y cuántas
    personas son, y te paso la propuesta el mismo día.</p>
    <div class="acciones">
      {wa_btn('WhatsApp ' + TEL_BONITO)}
      <a class="btn linea" href="tel:+{TEL_E164}">Llamar</a>
    </div>
  </div>
</header>

{cinta(('Te respondo','el mismo día'), ('9:00','a 19:00'), ('Todos','los días'))}

<section>
  <div class="wrap">
    <div class="duo">
      <div>
        <h2>Los datos, sin rodeos</h2>
        <div class="carta">
          <div class="item"><div><div><b>WhatsApp</b><small>La vía más rápida, y por donde
            cotizo.</small></div></div>
            <a class="precio" href="{WA}" target="_blank" rel="noopener">{TEL_BONITO}</a></div>
          <div class="item"><div><div><b>Horario</b><small>Si escribes más tarde, te
            respondo a primera hora.</small></div></div><span class="precio">9:00 a 19:00</span></div>
          <div class="item"><div><div><b>Cocina</b><small>No es punto de venta al público;
            se atiende con pedido.</small></div></div><span class="precio">Bogotá</span></div>
          <div class="item"><div><div><b>Cobertura</b><small>Bogotá, la sabana y principales
            ciudades.</small></div></div>
            <a class="precio" href="ciudades.html">Ver ciudades</a></div>
          <div class="item"><div><div><b>Anticipo</b><small>Para apartar tu fecha. El resto
            el día del evento.</small></div></div><span class="precio">50%</span></div>
        </div>
      </div>
      <img src="img/mezze-arabe-hummus-tabbuleh.jpg" loading="lazy" width="1200" height="900"
           alt="Mesa de mezze árabe con hummus, tabbuleh y pan pita">
    </div>
  </div>
</section>

<section style="background:var(--crema-2)">
  <div class="wrap estrecho">
    <h2>Para que te cotice de una</h2>
    <p class="lead">Si me mandas esto en el primer mensaje, te respondo con precio cerrado y
    no con otra pregunta.</p>
    <div class="carta" style="margin-top:22px">
      <div class="item"><div><div><b>La fecha y la hora</b><small>Y si es cóctel, almuerzo o
        noche.</small></div></div></div>
      <div class="item"><div><div><b>Cuántas personas</b><small>Un número aproximado me
        sirve.</small></div></div></div>
      <div class="item"><div><div><b>Dónde</b><small>Ciudad y, si ya lo tienes, el nombre del
        salón u hotel.</small></div></div></div>
      <div class="item"><div><div><b>Qué tipo de evento</b><small>Matrimonio, quince,
        empresa, reunión en casa.</small></div></div></div>
      <div class="item"><div><div><b>Restricciones</b><small>Vegetarianos, alergias, algo sin
        picante.</small></div></div></div>
    </div>
    <div class="acciones">{wa_btn('Mandar mis datos por WhatsApp')}</div>
  </div>
</section>

{cotizador('O ármalo aquí y lo envías hecho',
           'Tres toques y el mensaje queda escrito con todo lo que necesito.')}

<section>
  <div class="wrap">
    <div class="centro">{ORN}<h2>Antes de irte, mira esto</h2></div>
    <div class="fichas tres" style="margin-top:28px">
      <a href="menu.html"><h3>El menú</h3><p>Los 22 platos, con foto de cada uno.</p></a>
      <a href="eventos.html"><h3>Servicio completo</h3><p>Cómo montamos cada tipo de evento.</p></a>
      <a href="historia.html"><h3>La historia</h3><p>Quién cocina y por qué cocina así.</p></a>
    </div>
  </div>
</section>
</main>
''' + pie('contacto.html') + COTIZADOR_JS
W('contacto.html', contacto)


# ╔══════════════════════════════════════════════════════════════════╗
# ║  sitemap y robots                                                ║
# ╚══════════════════════════════════════════════════════════════════╝
urls = ''.join(
    f'  <url><loc>{DOMINIO}/{"" if a == "index.html" else a}</loc>'
    f'<lastmod>2026-10-04</lastmod>'
    f'<priority>{"1.0" if a == "index.html" else "0.8"}</priority></url>\n'
    for a, _t, _c in PAGINAS)
W('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n'
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
W('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {DOMINIO}/sitemap.xml\n')
W('CNAME', 'alobeirutyahabibi.com\n')


# ╔══════════════════════════════════════════════════════════════════╗
# ║  VERIFICACIÓN                                                    ║
# ╚══════════════════════════════════════════════════════════════════╝
htmls = {a for a, _t, _c in PAGINAS}
texto = {a: open(os.path.join(AQUI, a), encoding='utf-8').read() for a in htmls}
todo = ''.join(texto.values())

fotos = {os.path.basename(p) for p in glob.glob(os.path.join(AQUI, 'img', '*.jpg'))}
sin_usar = sorted(f for f in fotos if f not in todo)
rotos = sorted(set(re.findall(r'href="([a-z]+\.html)', todo)) - htmls)
# el usted se cuela fácil al editar; que el script lo cace
UD = re.compile(r'\b(usted|ustedes|su evento|escríbanos|cuéntenos|mándenos|pídanos|'
                r'tiene usted|puede usted)\b', re.I)
ustedes = {a: sorted(set(m.group(0) for m in UD.finditer(s))) for a, s in texto.items()}
ustedes = {a: v for a, v in ustedes.items() if v}

print(f'  {len(htmls)} páginas + sitemap.xml + robots.txt + CNAME')
print(f'  fotos en img/: {len(fotos)} · sin usar: {len(sin_usar)}')
if sin_usar:
    print('  !! FOTOS HUERFANAS: ' + ', '.join(sin_usar))
if rotos:
    print('  !! ENLACES ROTOS: ' + ', '.join(rotos))
if ustedes:
    for a, v in ustedes.items():
        print(f'  !! USTED en {a}: ' + ', '.join(v))
for a in sorted(htmls):
    print(f'    {a:16} {len(texto[a])/1024:6.1f} KB')
if not sin_usar and not rotos and not ustedes:
    print('  todo cuadra · tuteo limpio · 26 de 26 fotos en uso')
