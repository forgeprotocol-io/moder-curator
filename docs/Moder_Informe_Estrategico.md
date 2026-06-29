# Moder — Evaluación Estratégica y de Inversión

### ¿Tiene el modelo de negocio de Moder fundamentos para convertirse en la principal plataforma de moda de Latinoamérica y en una empresa de alto crecimiento?

**Documento de trabajo confidencial · Junio 2026**
*Preparado bajo el lente combinado de: socio de Retail (McKinsey), inversionista de growth (Sequoia), experto en marketplaces, economista y científico de datos.*

---

> **Nota de honestidad intelectual (léase primero).** Este informe fue construido para **desafiar**, no para validar, las hipótesis del fundador. Donde la evidencia contradice un supuesto, lo decimos explícitamente y proponemos alternativas. Tres advertencias metodológicas que condicionan todo lo que sigue:
>
> 1. **Jerarquía de evidencia.** Marcamos cada afirmación con su nivel de confianza: **[V]** = verificada adversarialmente contra fuente primaria/secundaria de alta calidad (informes auditados de empresas públicas, prensa tier-1 con sourcing regulatorio); **[D]** = direccional, proveniente de market research comercial (Statista, Grand View, Business of Apps, etc.), útil para ordenar magnitudes pero no para decisiones de precisión; **[M]** = modelo/estimación propia a partir de supuestos declarados.
> 2. **Lo que NO pudimos verificar.** La cifra exacta de TAM/SAM/SOM de Chile y LatAm, los CAC reales Meta vs TikTok en Chile, y los benchmarks de LTV/retención del consumidor de moda **no existen en fuente primaria auditada de acceso público**. Usamos los mejores proxies disponibles, claramente etiquetados. Cualquier decisión de capital debería refinarlos con datos de primera mano (la propia analítica de Moder).
> 3. **Los comparables no son idénticos a Moder.** Zalando (híbrido mayorista) y Lyst (agregador de afiliación) tienen modelos distintos al de suscripción B2B de Moder. Sirven como **cautela direccional**, no como predicción exacta.

---

## Tabla de contenidos

0. Resumen ejecutivo
1. El veredicto y la tesis crítica
2. Metodología y supuestos maestros
3. Dimensionamiento del mercado (Chile, LatAm, España, Europa, EE.UU.)
4. El modelo de Moder y su tensión estructural
5. Economía unitaria del lado de la marca — desafío al supuesto de margen
6. Economía del lado del consumidor — funnel, CAC, Meta vs TikTok, orgánico
7. Benchmark de plataformas: qué copiar y qué NO copiar
8. Efectos de red, flywheel, cold-start, moats y barreras
9. Respuestas directas a las catorce preguntas
10. Modelo financiero — escenarios y valoración
11. Matriz de riesgos
12. KPIs semanales
13. *Si yo fuera el CEO de Moder durante los próximos cinco años*
14. Recomendaciones priorizadas
- Anexo A — Notas metodológicas y supuestos
- Anexo B — Anexo técnico de fórmulas (para actualizar el modelo)
- Anexo C — Bibliografía

---

## 0. Resumen ejecutivo

**Tesis central.** El modelo *tal como está formulado* —un marketplace de descubrimiento de moda cuya única fuente de ingreso inicial es una suscripción fija de CLP 100.000/mes a las marcas— **no tiene, por sí solo, los fundamentos para convertirse en una empresa de alto crecimiento ni en "la principal plataforma de moda de Latinoamérica".** No porque la idea sea mala, sino por cuatro razones cuantificables que desarrollamos en el cuerpo del informe:

1. **El techo de ingreso es estructuralmente bajo.** A CLP 100.000/mes, *1.000 marcas* generan apenas **≈ US$1,26 millones de ARR** **[M]**. Eso no es una empresa de "alto crecimiento" valorada en cientos de millones; es un negocio de software pequeño-mediano. El modelo de suscripción **desacopla el ingreso de Moder del GMV**, regalando precisamente el *upside* que hace valiosos a los marketplaces. **[V — a16z; M]**

2. **Bajo suscripción pura, el consumidor genera US$0 de ingreso directo a Moder.** Es un **centro de costo**, no de ingreso. Como Moder igual debe pagar para atraer y retener consumidores (sin demanda, las marcas no renuevan), la economía se invierte: se paga por adquirir un lado que no monetiza. Por eso el EBITDA es **negativo en 13 de 15 combinaciones** escenario×tamaño que modelamos. **[M]**

3. **El verdadero cuello de botella no es cobrar a las marcas: es la liquidez.** La causa #1 de muerte de marketplaces es nunca alcanzar liquidez (el problema *chicken-and-egg* / cold-start). **[V — a16z, corroborado]** Una suscripción fija *no* resuelve la liquidez; al contrario, **sobre-cobra a las marcas de bajo desempeño**: una marca que vende 1–2 prendas/mes por Moder paga un *take rate efectivo de 100–200% sobre su GMV* **[M]**, lo que dispara el churn de oferta.

4. **El supuesto de margen del fundador (precio = 1,5× costo, es decir 33% de margen bruto) es bajo para moda** y, paradójicamente, *empeora* la propuesta de valor. La moda real opera en 40–70% de margen bruto según categoría. **[D — TrueProfit, comps públicos]** Con márgenes reales, las marcas necesitan vender **menos** prendas para justificar la suscripción —buena noticia— pero el punto crítico (la liquidez) permanece.

**Lo que sí es defendible.** Existe un camino real, pero **no es el del enunciado**. Es un camino en tres actos: (a) usar la suscripción como *wedge* de entrada y herramienta de disciplina, no como modelo final; (b) ganar la batalla de la **liquidez en un nicho geográfico y de categoría estrecho** (Chile, una vertical) antes de hablar de "Latinoamérica"; (c) **migrar la monetización hacia el GMV** (comisión, ads de marca, servicios financieros, datos/IA) a medida que la liquidez aparece. Si Moder ejecuta esto, el activo defendible no es la app: es la **curaduría + los datos de demanda + la relación con las marcas locales**. El capítulo 13 detalla exactamente cómo lo haría yo como CEO.

**Recomendación de inversión (lente Sequoia).** En su formulación actual: **paso** a una ronda de venture de alto crecimiento; **financiable** como negocio de software rentable de nicho. Con el *pivote de monetización* y prueba de liquidez en una cohorte (capítulos 8 y 13): **interesante para una pre-seed/seed pequeña**, condicionada a métricas de liquidez, no de número de marcas.

---

## 1. El veredicto y la tesis crítica

### 1.1 Qué afirma el fundador (hipótesis a auditar)

| # | Hipótesis del fundador | Veredicto | Sección |
|---|---|---|---|
| H1 | La suscripción de marcas es una base de ingreso suficiente para la etapa inicial | **Parcial.** Suficiente para *sobrevivir* en nicho; insuficiente para "alto crecimiento". | §4, §10 |
| H2 | Llegar a 50 → 100 → 250 → 500 → 1.000 marcas construye una empresa grande | **Refutada** para "grande". A 1.000 marcas, ARR ≈ US$1,26M. | §10 |
| H3 | Margen de marca = 1,5× costo (33% bruto) | **Refutada como representativo.** Moda real: 40–70%. | §5 |
| H4 | Una prenda promedio cuesta ~CLP 50.000 | **Plausible** como ticket de gama media chilena; no verificable en primaria. | §3, §5 |
| H5 (implícita) | El reto es conseguir marcas | **Refutada.** El reto es la *liquidez* (demanda que dé ROI a las marcas). | §8 |
| H6 (implícita) | Moder puede ser "la principal plataforma de moda de LatAm" | **Improbable** bajo el modelo actual; posible solo con pivote y foco. | §7, §13 |

### 1.2 La tesis crítica en una frase

> Moder está optimizando la variable equivocada (número de marcas que pagan) cuando la variable que determina vida o muerte es **la liquidez del lado consumidor**; y está eligiendo el modelo de monetización (suscripción fija) que **menos captura el valor** que un marketplace exitoso genera.

Esto no es opinión: es la lección consolidada de la literatura de marketplaces. La liquidez —"la probabilidad de vender un ítem listado, o de encontrar lo que buscas"— es **"el aspecto más crítico de un marketplace; sin ella no es valioso para compradores ni vendedores. La mayoría de los marketplaces fracasan porque nunca alcanzan ni mantienen la liquidez"** (a16z, *13 Metrics for Marketplace Companies*, corroborado por Reforge, NFX y Sharetribe). **[V, voto 2-1]**

---

## 2. Metodología y supuestos maestros

**Proceso.** (1) Investigación web multi-fuente con descomposición en 5 ángulos (market sizing, benchmarks de marketplaces, economía de adquisición, network effects/cold-start, valoración y márgenes). (2) Extracción de afirmaciones falsables y **verificación adversarial de 3 votos** (se requería ≥2/3 refutaciones para descartar una afirmación). (3) Construcción de un modelo financiero determinístico parametrizado (Anexo B). (4) Síntesis crítica.

**Resultado de la verificación:** de 13 afirmaciones sometidas a verificación, **12 confirmadas, 1 refutada** (la del margen bruto de Zalando 43,5%, descartada por voto 1-2 → no la usamos). Las 6 afirmaciones de mayor confianza sostienen los argumentos centrales de este informe.

### Supuestos maestros (todos parametrizados en el modelo)

| Parámetro | Valor base | Fuente / nivel |
|---|---|---|
| Tipo de cambio CLP/USD | **950** (promedio 2025 ≈ 951) | exchange-rates.org **[D]** |
| Suscripción | CLP 100.000/mes = 1.200.000/año = **US$1.263/año** | Dato del fundador |
| Precio prenda promedio | CLP 50.000 = **US$53** | Dato del fundador **[H4]** |
| Margen bruto de marca (base) | **55%** (no 33%) | TrueProfit; comps públicos **[D]** — ver §5 |
| Margen bruto de software de Moder | 75% | Estándar SaaS **[D]** |

---

## 3. Dimensionamiento del mercado

> **Advertencia.** Las cifras de esta sección provienen de *market research* comercial **[D]**, no de fuentes primarias auditadas. Las distintas casas difieren hasta 2× entre sí (síntoma de baja confiabilidad). Úsense para ordenar magnitudes, no para precisión.

### 3.1 Chile (el mercado de partida realista)

| Métrica | Valor 2025 | Fuente |
|---|---|---|
| Ingreso e-commerce de moda | **US$2.393 millones** | Statista Market Forecast **[D]** |
| Apparel (ropa) como % de la categoría moda | **52%** | Statista **[D]** |
| Penetración de usuarios del mercado moda | 49,9% (2025) → 59,2% (2029) | Statista **[D]** |
| Share online de la moda | 15–20% | Statista **[D]** |
| Add-to-cart rate | 10,0–10,5% | Statista **[D]** |
| **Cart abandonment** | **84,5–85,0%** | Statista **[D]** |

**Lectura crítica.** El mercado chileno de e-commerce de moda (~US$2,4 mil M) es **suficientemente grande para un SOM atractivo de nicho, pero pequeño para una ambición "LatAm".** Y el dato más importante para Moder es el último: **85% de carritos abandonados**. La fricción de conversión es brutal; cualquier modelo que dependa de que el consumidor *complete* compras debe invertir desproporcionadamente en reducir esa fricción (checkout, pagos, confianza). Baymard confirma que el promedio global es 70,2% y que **48% abandona por costos inesperados** en el checkout. **[D — Baymard]**

### 3.2 Latinoamérica

| Métrica | Valor | Fuente |
|---|---|---|
| Moda online LatAm 2025 → 2031 | US$73,8 mil M → US$167,5 mil M (CAGR 14,6%) | Mobility Foresights **[D]** |
| Apparel LatAm (total, no solo online) 2024 → 2031 | US$87,9 mil M → US$131,1 mil M | Cognitive/Marketintelo **[D]** |
| Share online de la moda LatAm 2025 | ~28,9% (→ >40% al final del periodo) | Mobility Foresights **[D]** |
| Concentración | Brasil + México = **>60%** de la moda online | Mobility Foresights **[D]** |
| Mobile | 68% de compras de moda online vía smartphone (BR/MX) | Mobility Foresights **[D]** |

**Lectura crítica.** Tres hechos incómodos para la tesis "principal plataforma de LatAm": (1) el mercado está **dominado por Brasil y México**, mercados de idioma/regulación/logística distintos a Chile, con incumbentes formidables (Mercado Libre, Shein, Amazon, Dafiti/Global Fashion Group); (2) "LatAm" no es un mercado, son ~6 mercados con dinámicas logísticas y de pago heterogéneas —la expansión es cara y secuencial, no un *flip de switch*; (3) el crecimiento (CAGR ~14,6%) es bueno pero **no extraordinario** frente al costo de competir en él.

### 3.3 España, Europa y Estados Unidos (referencia competitiva)

No son mercados-objetivo realistas de corto plazo, pero definen a los gigantes que eventualmente aparecen en LatAm:

- **Europa:** Zalando opera con **51,8M de clientes activos**, **€15,3 mil M de GMV** y €10,6 mil M de ingresos (2024). **[V, 3-0]** Es la vara de lo que significa "liderar moda" en una región.
- **EE.UU.:** mercado de resale/social commerce maduro (Poshmark, Depop) y publicitario (Pinterest, TikTok Shop).
- **España:** hogar de Inditex (Zara), referencia de *fast fashion* verticalmente integrado.

**Implicación:** "la principal plataforma de moda de Latinoamérica" es un título que hoy disputan Mercado Libre, Shein y Global Fashion Group con miles de millones de GMV. Moder no compite ahí; **debe redefinir la cancha** (curaduría de marcas locales/independientes, una vertical específica) para tener un derecho a ganar.

### 3.4 TAM / SAM / SOM (síntesis, con franjas de incertidumbre)

| Nivel | Definición | Estimación | Confianza |
|---|---|---|---|
| **TAM** | Gasto en moda online LatAm | ~US$74 mil M (2025) | [D] |
| **SAM** | Moda online Chile (mercado de entrada) | ~US$2,4 mil M | [D] |
| **SOM (3–5 años, realista)** | Marcas independientes/curadas Chile capturables | **US$20–60 M de GMV** | [M] |
| **SOM monetizable por Moder (suscripción)** | Ingreso a 250–1.000 marcas | **US$0,3–1,3 M ARR** | [M] |

El salto entre las dos últimas filas es la tesis completa del informe: **el GMV potencial (decenas de millones) empequeñece el ingreso por suscripción (~US$1M).** Ahí vive el valor que el modelo actual regala.

---

## 4. El modelo de Moder y su tensión estructural

Moder es hoy, en su código, un **curador de productos de moda** (crawl + curación de catálogo hacia una hoja de importación). Esa es una pista valiosa: el activo naciente es la **curaduría y los datos de catálogo**, no el cobro de suscripción.

### 4.1 Suscripción vs. take rate: la decisión que define el techo

| Dimensión | Suscripción fija (modelo actual) | Take rate sobre GMV |
|---|---|---|
| Predecibilidad de ingreso | **Alta** (MRR limpio) | Variable |
| Captura del upside de crecimiento | **Nula** (desacoplado del GMV) | **Total** |
| Alineación de incentivos con la marca | Mala a baja liquidez (sobre-cobra) | **Buena** (Moder gana si la marca vende) |
| Simplicidad de venta B2B | **Alta** | Media |
| Techo de valoración | Bajo (múltiplos SaaS sobre ARR pequeño) | Alto (múltiplos sobre GMV/comisión) |

El *take rate* de los marketplaces "usualmente varía de un dígito bajo hasta mediados de 30%, según fragmentación, sustitutos y valor agregado operativo" (Etsy ~6–11%, eBay ~10%, Airbnb ~13–15%, Uber ~20–28%). **[V, 3-0 — a16z]**

**El hallazgo más contraintuitivo del informe:** a la liquidez bajísima del arranque, la suscripción fija **equivale a un take rate altísimo** (ver §5.3). Es decir, el modelo "simple" de suscripción es en realidad **el más caro para la marca** cuando vende poco —exactamente cuando es más frágil y propensa a cancelar.

---

## 5. Economía unitaria del lado de la marca — desafío al supuesto de margen

### 5.1 El supuesto del fundador es bajo para moda

El fundador asume **precio = 1,5× costo ⇒ margen bruto 33%**. La evidencia de la industria dice otra cosa **[D — TrueProfit, comps públicos, FashionUnited]**:

| Categoría | Margen bruto típico |
|---|---|
| Fast fashion / básicos | 30–48% |
| DTC apparel (sano) | 50–60% (top quartile 60–65%) |
| Premium / contemporary | 55–65% |
| Athleisure | 55–65% |
| Lujo / diseñador | 60–70%+ |
| **Mediana 8 comps públicos de apparel** | **55,3%** |

La práctica histórica del retail de moda es el *keystone* (2× costo = 50% de margen), y la mayoría de marcas con marca propia superan eso. **Conclusión: el 33% del fundador corresponde al *piso* (fast fashion); el caso representativo para marcas curadas es 50–60%.** Usamos **55% como base**, con sensibilidad.

### 5.2 ¿Cuántas prendas para recuperar la suscripción y para un ROI 3×?

CLP 100.000/mes de suscripción, prenda de CLP 50.000. **[M]**

| Markup | Margen bruto | Utilidad/prenda | **Prendas para recuperar** (BE) | **Prendas para ROI 3×** |
|---|---|---|---|---|
| 1,5× (supuesto fundador) | 33% | CLP 16.667 | **6,0** | **18,0** |
| 2,0× | 50% | CLP 25.000 | **4,0** | **12,0** |
| 2,5× | 60% | CLP 30.000 | **3,3** | **10,0** |
| **Base 55%** | 55% | CLP 27.500 | **3,6 (≈4)** | **10,9 (≈11)** |

> **Interpretación de "ROI 3×":** lo definimos como *generar utilidad bruta equivalente a 3× la suscripción* (CLP 300.000). Si se exige ROI 3× **neto** (recuperar la suscripción **y además** 3×), las cifras suben ~33% (p. ej., 24 prendas a 1,5×). Ambas lecturas están en el Anexo B.

**Buena noticia para Moder:** corregido el supuesto de margen, una marca necesita **~4 prendas/mes** para no perder dinero y **~11/mes** para un ROI 3×. Es un umbral *alcanzable*. El problema no es el umbral por marca: es **multiplicarlo por 50–1.000 marcas simultáneamente** (la liquidez agregada).

### 5.3 El take rate efectivo: por qué la suscripción fija castiga a la marca débil

Comparando la suscripción contra el GMV que la marca realmente mueve por Moder (margen base 55%): **[M]**

| Ventas/mes de la marca | GMV/mes (CLP) | Utilidad bruta | **Take rate efectivo** (sub/GMV) | ¿Cubre suscripción? |
|---|---|---|---|---|
| 1 | 50.000 | 27.500 | **200%** | ❌ |
| 2 | 100.000 | 55.000 | **100%** | ❌ |
| 4 | 200.000 | 110.000 | **50%** | ✅ (apenas) |
| 7 | 350.000 | 192.500 | 29% | ✅ |
| 11 | 550.000 | 302.500 | 18% | ✅ |
| 13 | 650.000 | 357.500 | **15%** | ✅ |
| 20 | 1.000.000 | 550.000 | **10%** | ✅ |
| 30 | 1.500.000 | 825.000 | 7% | ✅ |

**Esta tabla es la columna vertebral del riesgo del negocio.** Una marca recién llega a un take rate efectivo "normal" de marketplace (10–15%) cuando vende **13–20 prendas/mes por Moder**. Por debajo de eso —que será la *mayoría* de las marcas en el arranque— la marca está pagando un múltiplo del valor que recibe y **racionalmente cancelará**. Esto se traduce directamente en **churn de oferta**, que rompe el lado de la liquidez. La suscripción fija convierte el problema de liquidez en una bomba de tiempo de retención.

---

## 6. Economía del lado del consumidor — funnel, CAC, Meta vs TikTok, orgánico

### 6.1 El funnel y los supuestos

Trabajamos hacia atrás desde las **ventas que las marcas necesitan**. Tres escenarios (Anexo A para todos los parámetros): **[M]**

| Parámetro | Conservador | **Base** | Optimista | Referencia |
|---|---|---|---|---|
| % de descargas que queda activo (→MAU) | 15% | **22%** | 30% | Retención apps shopping D30 ~5–10%; MAU incluye reactivación [D] |
| Conversión a compra mensual (de MAU) | 2% | **3%** | 4% | Conversión apparel ~3,4% [D — Baymard] |
| Ítems por orden | 1,2 | **1,3** | 1,5 | [M] |
| DAU/MAU (stickiness) | 12% | **15%** | 20% | Apps shopping ~10–20% [D] |
| Ventas/marca/mes objetivo | 6 | **10** | 15 | umbral ROI §5 |

### 6.2 ¿Cuántas descargas, MAU y DAU para que 50 marcas estén felices?

| Métrica (50 marcas) | Conservador | **Base** | Optimista |
|---|---|---|---|
| Ventas totales/mes | 300 | **500** | 750 |
| MAU | 12.500 | **≈12.800** | 12.500 |
| DAU | 1.500 | **≈1.900** | 2.500 |
| **Descargas acumuladas necesarias** | 83.300 | **≈58.300** | 41.700 |
| Compradores/mes | 250 | **385** | 500 |

**Lectura:** para que 50 marcas vendan ~10 prendas/mes cada una (felices, ROI positivo), Moder necesita del orden de **~13.000 usuarios activos mensuales, ~1.900 diarios y haber acumulado ~58.000 descargas** (escenario base). Nótese que el MAU es similar entre escenarios porque un funnel mejor (más conversión/retención) reduce las descargas necesarias para el mismo resultado.

### 6.3 ¿Cuánto cuesta conseguir esas descargas? Meta vs TikTok

CPI (costo por instalación) de apps de **shopping en Latinoamérica**: la región más barata del mundo, **US$0,50–2,00**; Meta ~>US$2,00; **TikTok ~US$1,75–4,00**. **[D — Business of Apps, Mapendo]**

Costo de adquirir las descargas necesarias para 50 marcas (escenario base, ~58.300 instalaciones): **[M]**

| Canal | CPI usado | Costo (CLP) | Costo (USD) |
|---|---|---|---|
| **100% Meta Ads** | US$1,5 | ~83,0 M | **~US$87.000** |
| **100% TikTok Ads** | US$2,5 | ~138,4 M | **~US$145.700** |
| Mix con 50% orgánico (solo paga 50%) | US$1,5 | ~41,5 M | **~US$43.700** |

Rango entre escenarios: Meta **US$42k–167k**, TikTok **US$69k–238k**, para *el primer ciclo de 50 marcas*.

> **El golpe demoledor.** El ingreso de Moder con 50 marcas es **US$63.000/año**. Conseguir las descargas necesarias vía Meta cuesta **US$87.000** (y vía TikTok ~US$146.000) — **más que un año entero de ingresos, solo en adquisición de un lado que no monetiza directamente.** Esta es la razón aritmética por la que el modelo de suscripción pura no cierra: el CAC del consumidor se compara contra un ingreso que llega del *otro* lado y que está topado por el precio fijo.

### 6.4 CAC por comprador y el rol del crecimiento orgánico

CAC por **comprador** (no por instalación), escenario base, 100% pagado vía Meta: **~CLP 216.000 (US$227)**. Conservador: ~US$667. Optimista: ~US$83. **[M]**

**¿Cuánto reduce el CAC el crecimiento orgánico?** No hay una cifra verificada universal **[el research no la validó]**, pero la evidencia de los comparables es inequívoca en dirección: los marketplaces de moda que ganaron **no compraron su demanda, la cultivaron**:

- **Vinted, Depop y Poshmark** crecieron *community-led* y *product-led* (contenido social, referidos, "posh parties", estética tipo Instagram), no a punta de Meta Ads. **[D]**
- TikTok/Instagram como canal **orgánico** (no pagado) es el growth loop natural de la moda (contenido → descubrimiento → seguidores → ventas).

**Conclusión modelada:** cada punto de mezcla orgánica reduce proporcionalmente las instalaciones pagadas. Pasar de 0% a 50% orgánico **reduce el costo de adquisición a la mitad**; a 65% orgánico (optimista) lo reduce ~65%. **Para Moder, el orgánico no es un "nice to have": es condición de supervivencia.** El modelo solo se acerca a viable cuando ≥50–65% de la demanda es orgánica.

---

## 7. Benchmark de plataformas: qué copiar y qué NO copiar

| Plataforma | Cómo consiguió usuarios | Cómo consiguió marcas/oferta | Qué funcionó | Qué fracasó | Lección para Moder |
|---|---|---|---|---|---|
| **Zalando** | Marketing masivo + envíos/devoluciones gratis | Mayorista propio → luego marketplace | Escala (51,8M clientes, €15,3B GMV) **[V]** | Margen EBIT ajustado **4,8%**, neto ~2,4% **[V]** | **Escalar en moda NO da altos márgenes.** No copiar el "crecer a toda costa". |
| **Lyst** | SEO de descubrimiento + ads de afiliación | Agregación de catálogos (27.000 marcas, 190 mercados) **[V]** | Tráfico de descubrimiento | **Valoración US$700M → venta US$154M (−78%), ingresos planos ~£50M** **[V]** | **Un agregador de moda no compone crecimiento automáticamente.** Múltiplo de salida real: **2,4× ingresos.** |
| **Vinted** | Community-led, C2C, simplicidad | Vendedores particulares (oferta gratis y abundante) | 100M usuarios, €10B GMV, ~90% share EU **[D]** | (Tardó años en rentabilizar) | **Resolver primero el lado difícil con oferta de bajo costo.** Copiar el motor de comunidad. |
| **Depop** | Estética Instagram, Gen Z, social | Vendedores jóvenes; salió de una revista (PIG) | 90% Gen Z; venta a Etsy **US$1,625B** (2021) **[D]** | Monetización limitada pre-adquisición | **El contenido social ES el canal de adquisición.** Copiar el ADN social. |
| **Poshmark** | "Posh parties", gamificación social | Vendedores particulares (closets) | IPO 2021 a ~US$3B **[D]** | Acción cayó fuerte post-IPO | Comunidad como growth loop; cuidado con la euforia de valoración. |
| **SHEIN** | Performance marketing + influencers a escala industrial + supply ultrarrápido | Cadena de suministro propia (no marketplace puro) | Velocidad de catálogo y precio | Cuestionamientos ESG/laborales/IP | **No copiable** por una startup; ilustra el poder del supply, no de la suscripción. |
| **ASOS / Farfetch** | Marketing + catálogo amplio | Marcas + boutiques (Farfetch) | Crecimiento inicial | **Farfetch al borde del colapso** (rescate de Coupang) | **El modelo "boutiques de lujo agregadas" quema caja.** No copiar la economía. |
| **Pinterest / Instagram Shopping / TikTok Shop** | Base social masiva preexistente | Comerciantes sobre la red social | Descubrimiento visual nativo | Conversión/checkout inconsistente | **El descubrimiento visual funciona; Moder no tiene la base social — debe construir el loop, no asumirlo.** |

### Síntesis: qué copiar y qué no

**Copiar:** (1) el **motor de comunidad/contenido** de Vinted/Depop/Poshmark como canal de adquisición orgánico; (2) la **estética social-first** (la moda se descubre, no se busca); (3) **resolver primero el lado difícil** con oferta abundante y de bajo costo de incorporación; (4) la **curaduría** como diferenciador (el activo que Moder ya tiene en su producto).

**NO copiar:** (1) el "crecer a toda costa" de Zalando (márgenes delgados); (2) la economía de agregador de lujo de Lyst/Farfetch (no compone, valoraciones colapsan); (3) la dependencia de **performance marketing pagado** como motor principal (insostenible para el ingreso de Moder); (4) asumir una base social que no se tiene (Instagram/TikTok Shop).

---

## 8. Efectos de red, flywheel, cold-start, moats y barreras

### 8.1 El problema del cold-start (chicken-and-egg)

Es el riesgo #1. **[V]** Moder lo enfrenta agravado por su modelo: cobra a las marcas *antes* de poder garantizarles demanda. Tácticas con evidencia (NFX, a16z) para resolverlo: **[D]**

1. **Atacar primero el lado más difícil.** En moda curada, el lado difícil suele ser la **demanda con intención** (consumidores que compran), no las marcas. Conseguir 50 marcas es fácil; conseguir 13.000 MAU que compren, no.
2. **Estrechar el mercado (single-player utility + foco).** No "moda LatAm", sino *una* ciudad/categoría/tribu (p. ej., "marcas independientes chilenas de diseño" o "streetwear local"). La liquidez es local antes que global.
3. **Dar valor de un solo lado primero.** La **curaduría** (el producto actual de Moder) puede dar valor al consumidor *aunque no haya transacción*: ser el mejor lugar para *descubrir* marcas locales. Eso atrae demanda antes que la oferta esté monetizada.
4. **Subsidiar el lado escaso.** Al inicio, regalar/descontar la suscripción a marcas ancla a cambio de exclusividad o contenido.

### 8.2 ¿Hay efectos de red reales? (escéptico)

**Honestamente: débiles en el modelo actual.** Un marketplace de moda tiene efectos de red **más débiles** que uno de servicios homogéneos (Uber) porque la moda es de *gusto heterogéneo* y *baja frecuencia*. Más marcas no necesariamente mejoran la experiencia (pueden generar *ruido*; por eso la **curaduría** importa). El efecto de red genuino aparece por el lado de **datos**: cuantas más transacciones, mejor la recomendación/curaduría con IA → mejor conversión → más ventas para marcas → más marcas. Ese es el flywheel a construir.

### 8.3 El flywheel objetivo de Moder

```
   Curaduría/IA superior  →  Descubrimiento que convierte  →  Ventas para las marcas
            ↑                                                          ↓
   Más datos de demanda   ←  Más consumidores que vuelven  ←  Marcas felices renuevan/llegan
```

El combustible de este volante **no es la suscripción** —es la **calidad de la curaduría y los datos**. Por eso el modelo de monetización debe migrar a algo acoplado al GMV/datos.

### 8.4 Moats y barreras de entrada (evaluación fría)

| Moat potencial | ¿Real para Moder hoy? | Cómo construirlo |
|---|---|---|
| Efecto de red de dos lados | Débil | Liquidez en nicho + datos |
| **Datos propietarios de demanda/curaduría + IA** | **El más prometedor** | Acumular transacciones y señal de gusto local |
| Marca/comunidad | Por construir | Community-led growth (copiar Depop) |
| Relaciones con marcas locales / exclusividad | Construible y defendible | Contratos, curaduría, co-marketing |
| Costos de cambio | Bajos (suscripción cancelable) | Integrar inventario/analítica/pagos de la marca (volverse su sistema operativo) |
| Economías de escala | No a este tamaño | — |

**Barreras de entrada del sector (contra Moder):** capital de los incumbentes (Mercado Libre, Shein), logística y pagos, y la **baja barrera para que otro lance una app de catálogo** (el software es commodity; la curaduría + datos + comunidad no). La verdadera barrera defendible que Moder puede erigir es **ser el sistema operativo de descubrimiento de las marcas locales** (datos + audiencia + herramientas), no la app en sí.

---

## 9. Respuestas directas a las catorce preguntas

*(Escenario base; rangos = conservador–optimista. Todo [M] salvo indicación.)*

1. **¿Cuántas descargas necesita Moder?** Para sostener 50 marcas felices: **~58.000 acumuladas** (42k–83k). Escala lineal aproximada: ~117k para 100 marcas, ~292k para 250, ~583k para 500, **~1,17M para 1.000**.
2. **¿Cuántos MAU?** **~13.000** para 50 marcas; ~260.000 para 1.000.
3. **¿Cuántos DAU?** **~1.900** para 50 marcas (DAU/MAU 15%); ~38.000 para 1.000.
4. **¿Qué % de descargas permanece activo?** **~22%** base (15–30%). Ojo: la retención D30 de apps de shopping es de un dígito (~5–10%) **[D]**; el 22% asume reactivación y un producto pegajoso —es *optimista* y debe validarse.
5. **¿Qué % compra?** De los MAU, **~3%/mes** (2–4%) **[D — apparel ~3,4%]**. De las descargas totales, ~0,5–1%/mes.
6. **¿Cuántas prendas por comprador?** **~1,3 por orden** (1,2–1,5); frecuencia baja (moda = compra poco frecuente).
7. **¿Cuántas ventas mensuales para que 50 empresas estén felices?** **~500/mes** (300–750), es decir **~10 prendas/marca/mes**. Mínimo para que *la mayoría* supere break-even (≥4/marca con margen real): ~200–300/mes; para ROI 3× generalizado: ~550/mes.
8. **¿Cuánto costaría esas descargas solo con Meta?** **~US$87.000** (US$42k–167k) para el ciclo de 50 marcas.
9. **¿Y con TikTok?** **~US$146.000** (US$69k–238k).
10. **¿Cuánto reduce el CAC el crecimiento orgánico?** Proporcional a la mezcla: **50% orgánico ⇒ −50% del costo pagado; 65% ⇒ −65%.** Es la palanca decisiva.
11. **¿Qué KPIs semanales?** Ver §12 (liquidez, no vanidad).
12. **¿Riesgos principales?** Ver §11 (cold-start/liquidez, churn de marcas por take rate efectivo, CAC > ingreso, techo de ingreso, competencia).
13. **¿Moats principales?** Datos propietarios + IA de curaduría; comunidad/marca; relaciones de exclusividad con marcas locales; ser el SO de las marcas (§8.4).
14. **¿Barreras de entrada?** Bajas para clonar la app; altas para replicar datos + comunidad + curaduría + relaciones. Ahí debe invertir Moder.

**Bonus — ¿Cómo construir el efecto de red?** (1) Liquidez en un nicho estrecho primero; (2) curaduría/IA que mejore con cada transacción (efecto de red de datos); (3) comunidad/contenido como loop de adquisición; (4) volverse infraestructura de la marca (inventario, analítica, pagos) para crear costos de cambio.

---

## 10. Modelo financiero — escenarios y valoración

> Todas las cifras en USD a CLP/USD = 950. P&L simplificado, supuestos en Anexo A–B. **[M]**

### 10.1 Ingreso por suscripción (el techo)

| Marcas | MRR (CLP) | ARR (CLP) | **ARR (USD)** |
|---|---|---|---|
| 50 | 5,0 M | 60,0 M | **63.158** |
| 100 | 10,0 M | 120,0 M | **126.316** |
| 250 | 25,0 M | 300,0 M | **315.789** |
| 500 | 50,0 M | 600,0 M | **631.579** |
| 1.000 | 100,0 M | 1.200,0 M | **1.263.158** |

### 10.2 P&L por escenario (EBITDA, USD)

**Escenario Conservador**

| Marcas | ARR | Acq. consumidor | Acq. marca | Opex | **EBITDA** | Margen |
|---|---|---|---|---|---|---|
| 50 | 63k | 117k | 14k | 150k | **−218k** | −344% |
| 250 | 316k | 583k | 70k | 450k | **−788k** | −249% |
| 1.000 | 1.263k | 2.333k | 280k | 1.100k | **−2.450k** | −194% |

**Escenario Base**

| Marcas | ARR | Acq. consumidor | Acq. marca | Opex | **EBITDA** | Margen |
|---|---|---|---|---|---|---|
| 50 | 63k | 44k | 6k | 150k | **−136k** | −216% |
| 100 | 126k | 87k | 11k | 250k | **−222k** | −176% |
| 250 | 316k | 219k | 28k | 450k | **−381k** | −121% |
| 500 | 632k | 437k | 56k | 700k | **−562k** | −89% |
| 1.000 | 1.263k | 874k | 113k | 1.100k | **−823k** | −65% |

**Escenario Optimista**

| Marcas | ARR | Acq. consumidor | Acq. marca | Opex | **EBITDA** | Margen |
|---|---|---|---|---|---|---|
| 50 | 63k | 15k | 2k | 150k | **−104k** | −164% |
| 250 | 316k | 73k | 11k | 450k | **−218k** | −69% |
| 500 | 632k | 146k | 23k | 700k | **−237k** | −37% |
| 1.000 | 1.263k | 292k | 45k | 1.100k | **−174k** | −14% |

**Lectura.** Bajo suscripción pura, **ningún escenario alcanza EBITDA positivo dentro del rango 50–1.000 marcas.** El mejor caso (optimista, 1.000 marcas) sigue en −14%. La causa: el costo de sostener la demanda del consumidor (que no monetiza directamente) + opex supera al ingreso topado por el precio fijo.

### 10.3 LTV, CAC y Payback

**Trampa analítica frecuente — el "LTV/CAC del lado marca" se ve genial y es engañoso:**

- ARPA = US$1.263/año; churn de marca base 25% ⇒ vida media 4 años; margen bruto software 75% ⇒ **LTV marca ≈ US$3.789**.
- CAC marca (venta B2B) ≈ US$450 ⇒ **LTV/CAC ≈ 8,4×** y **payback ≈ 5,7 meses**. *Excelente… en aislamiento.*

**La realidad fully-loaded:** hay que sumar el costo de adquirir la demanda del consumidor que hace que la marca venda. En base, eso es ~US$874/marca/año en adquisición de consumidor. **Incluido eso, la contribución neta por marca cae a ~US$277/año** y el **LTV/CAC fully-loaded cae por debajo de ~1× hasta que el orgánico domina.** Esta es la diferencia entre un modelo que parece sano y uno que no cierra.

**LTV del consumidor (bajo suscripción pura): US$0 directo.** Moder no captura nada de la transacción. Este único hecho condena la economía y es el argumento más fuerte para migrar a take rate.

### 10.4 Punto de equilibrio (suscripción pura, base)

Contribución neta por marca ≈ **US$277/año**. Marcas necesarias para cubrir opex:

| Opex (etapa) | Marcas para EBITDA ≥ 0 |
|---|---|
| US$150k | **~542** |
| US$250k | ~904 |
| US$450k | ~1.627 |
| US$700k | ~2.531 |
| US$1,1M | ~3.978 |

**El break-even exige del orden de 540 marcas con el equipo más austero, y miles si el equipo crece.** Está muy por encima del objetivo de 50 y del horizonte cómodo de 1.000 — *salvo* que el orgánico empuje el CAC del consumidor cerca de cero (lo que sube la contribución por marca y baja el break-even).

### 10.5 Flujo de caja y necesidad de capital

Con EBITDA negativo en todos los tamaños bajo suscripción pura, el **FCF es negativo** y la empresa **requiere capital continuo** solo para sostener la demanda. Quemar US$130k–800k/año (base) para construir un negocio cuyo ARR tope es ~US$1,3M **no es financiable como venture de alto crecimiento**; es, en el mejor caso, un pequeño negocio rentable *si y solo si* el CAC del consumidor tiende a cero vía orgánico.

### 10.6 Valoración potencial

**(a) Suscripción pura — múltiplos sobre ARR** (SaaS público mediano ~6× EV/Rev 2025; alto crecimiento 8–12×; bajo crecimiento 1–2×; **salida real de marketplace de moda Lyst = 2,4×**). **[D / V]**

| Marcas | ARR (USD) | 2,4× (Lyst) | 6× (SaaS med.) | 10× (alto crec.) |
|---|---|---|---|---|
| 250 | 316k | 0,76M | 1,9M | 3,2M |
| 500 | 632k | 1,5M | 3,8M | 6,3M |
| 1.000 | 1.263k | 3,0M | 7,6M | **12,6M** |

Incluso con un múltiplo generoso de alto crecimiento, **Moder-suscripción a 1.000 marcas vale ~US$8–13M.** No es un *outcome* de venture.

**(b) Con take rate sobre GMV (12%)** —el mismo volumen de ventas, pero capturando comisión:

| Marcas | GMV/año (USD) | Ingreso @12% | EV @4× ingreso |
|---|---|---|---|
| 250 | 1,58M | 189k | 0,76M |
| 1.000 | 6,32M | 758k | 3,0M |

**Hallazgo matizado y honesto:** a estos volúmenes *bajos*, la suscripción fija incluso **recauda más** que un take rate del 12% (porque su take rate efectivo es >12%). Esto **no** valida la suscripción —confirma que **a baja liquidez sobre-cobra a las marcas** (§5.3). El take rate gana cuando el GMV por marca crece; la estrategia correcta es **híbrida y dependiente de la liquidez** (§13). El verdadero salto de valoración no viene de elegir suscripción vs comisión a este tamaño: viene de **multiplicar el GMV** (más ventas por marca) y **añadir capas de monetización de alto margen** (ads, datos/IA, servicios financieros) sobre una base líquida.

---

## 11. Matriz de riesgos

| # | Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|---|
| R1 | **Cold-start / no alcanzar liquidez** | Alta | Fatal | Nicho estrecho; valor de un solo lado (curaduría); subsidiar lado escaso |
| R2 | **Churn de marcas por take-rate efectivo alto a baja liquidez** | Alta | Alto | Precio por desempeño; garantía de ventas/ROI; tiers |
| R3 | **CAC consumidor > ingreso** (dependencia de paid) | Alta | Alto | Community/PLG; orgánico ≥50–65%; contenido como canal |
| R4 | **Techo de ingreso de la suscripción** | Cierta | Estratégico | Migrar a monetización acoplada a GMV/datos |
| R5 | **Competencia de incumbentes** (Mercado Libre, Shein, GFG) | Media-Alta | Alto | No competir de frente; nicho curado/local |
| R6 | **Baja barrera para clonar la app** | Media | Medio | Moat de datos + comunidad + relaciones |
| R7 | **Conversión/checkout** (85% abandono en Chile) | Alta | Alto | Inversión en checkout, pagos locales, confianza |
| R8 | **Expansión LatAm prematura** (6 mercados heterogéneos) | Media | Alto | Dominar Chile primero; expandir por liquidez probada |
| R9 | **Dependencia de un solo modelo de ingreso** | Cierta | Medio | Roadmap de ads/SaaS/IA/afiliación (ya contemplado) |
| R10 | **Sobre-optimizar # de marcas (métrica de vanidad)** | Media | Estratégico | Gobernar por KPIs de liquidez (§12) |

---

## 12. KPIs semanales (gobernar por liquidez, no por vanidad)

**Métrica estrella (North Star):** *prendas vendidas por marca activa por semana* (proxy directo de liquidez y de ROI de la marca).

| Categoría | KPI semanal | Por qué |
|---|---|---|
| **Liquidez** | % de marcas que vendieron ≥1 prenda esta semana; ventas/marca activa; tiempo a primera venta de una marca nueva | El predictor #1 de supervivencia [V] |
| **Demanda** | MAU/WAU/DAU; DAU/MAU; nuevas descargas; % orgánico vs pagado | Salud del lado consumidor |
| **Conversión** | Visita→add-to-cart→compra; abandono de carrito | 85% abandono en Chile [D] |
| **Retención** | Cohorte de compradores recurrentes (repeat purchase rate); retención D7/D30 | "La métrica de retención de marketplaces" [V] |
| **Unit economics** | CAC por comprador por canal; CAC blended; % orgánico | Viabilidad |
| **Oferta/retención de marca** | Churn semanal de marcas; NRR de marcas; take rate efectivo promedio | Bomba de tiempo §5.3 |
| **Caja** | Burn semanal; runway en meses | Supervivencia |

**Métricas de vanidad a evitar como objetivo:** número total de descargas, número total de marcas, "usuarios registrados". Son resultados, no salud.

---

## 13. *Si yo fuera el CEO de Moder durante los próximos cinco años*

> Escrito en primera persona, como haría el CEO. El principio rector: **la liquidez manda; la monetización sigue a la liquidez; el foco vence a la ambición.**

### Año 1 — Ganar la liquidez en un nicho minúsculo (no escalar marcas)

**Qué haría:**
1. **Redefinir la cancha.** No "moda de LatAm". Elegiría **una vertical y una ciudad**: p. ej., *marcas independientes/de diseño chilenas* en Santiago. Mejor ser el #1 indiscutido de un nicho que el #20 de "moda".
2. **Invertir la prioridad: demanda primero.** Conseguir 50 marcas es trivial; lo difícil es **13.000 MAU que compran**. Construiría la audiencia con **contenido y comunidad** (copiar a Depop/Vinted): curaduría editorial, TikTok/Instagram orgánico, embajadores locales. Objetivo: que Moder sea *el mejor lugar para descubrir marcas chilenas* aunque aún no transacciones mucho (valor de un solo lado, §8.1).
3. **Reescribir el pricing.** Mientras no haya liquidez, **no cobraría CLP 100.000 fijos a marcas que venden poco** (las espantaría, §5.3). Usaría: gratis/freemium para entrar + **comisión sobre ventas** (10–15%) para alinear incentivos, o un híbrido "base baja + comisión". La suscripción plena se reserva para cuando la marca ya factura por Moder.
4. **Instrumentar todo.** North Star = ventas/marca activa/semana. Tablero de liquidez (§12) desde el día 1.

**Qué NO haría:** no perseguiría las "50 marcas" como meta; no gastaría en Meta Ads más de lo mínimo para *aprender* (no para crecer); no hablaría de expansión a LatAm.

**Hito de salida del Año 1:** una cohorte donde **≥60% de marcas vende ≥4 prendas/mes** y **≥30% de la demanda es orgánica**. Eso es product-market fit de liquidez.

### Año 2 — Densificar y probar el motor de retención

5. **Profundizar antes de ampliar.** Más vendedores y más compradores en el *mismo* nicho hasta que el repeat-purchase rate y el DAU/MAU sean sólidos. La liquidez es local.
6. **Construir el moat de datos/IA.** Cada transacción alimenta la curaduría/recomendación. La IA de descubrimiento (no un chatbot de moda genérico) que **suba la conversión** es el verdadero producto. Aquí Moder ya tiene ventaja: su producto nace como *curador*.
7. **Migrar el pricing hacia el valor.** Para marcas que ya venden 13–20 prendas/mes, introducir suscripción + comisión decreciente; el take rate efectivo entra en zona sana (10–15%).
8. **Empezar el flywheel de contenido-comunidad** con presupuesto de referidos (no de paid puro).

**Hito:** unit economics fully-loaded con LTV/CAC > 3× **incluyendo** el costo del consumidor, gracias a ≥50% orgánico.

### Año 3 — Capas de monetización de alto margen (donde aparece el "alto crecimiento")

9. **Activar ingresos acoplados al GMV:** comisión madura, **ads/destacados de marca** (alto margen), **market intelligence** (vender a las marcas datos de demanda que solo Moder tiene), y **afiliación**.
10. **Servicios para la marca (volverse su SO):** analítica, inventario, pagos, fulfillment ligero → costos de cambio reales.
11. **Recién aquí**, con liquidez y monetización probadas, levantar una ronda de crecimiento. La historia ya no es "1.000 marcas pagando US$100"; es "GMV de US$X creciendo Y%, con 4 fuentes de ingreso y un moat de datos".

### Año 4 — Expansión geográfica disciplinada

12. **Replicar el playbook de liquidez** en un segundo mercado **solo si** el primero está líquido y rentable a nivel de contribución. Orden por dificultad/oportunidad: probablemente **Perú/Colombia** antes que Brasil/México (donde los incumbentes son brutales). Cada mercado se gana por liquidez, no por lanzamiento simultáneo.

### Año 5 — Plataforma regional de descubrimiento curado

13. Posición objetivo: **la plataforma de descubrimiento y datos de las marcas independientes/curadas de la región**, con monetización multi-capa sobre una base de GMV real. Esa empresa **sí** puede aspirar a múltiplos de crecimiento; la de "suscripción a 1.000 marcas", no.

### Lo que NO haría en ningún momento (resumen)
- No usar "número de marcas" como métrica norte.
- No financiar la demanda principalmente con paid ads.
- No expandir a LatAm antes de liquidez+rentabilidad de contribución en Chile.
- No aferrarme a la suscripción fija como modelo final.
- No competir de frente con Mercado Libre/Shein en moda masiva.

---

## 14. Recomendaciones priorizadas

| Prioridad | Recomendación | Impacto | Plazo |
|---|---|---|---|
| **P0** | Cambiar la métrica norte de "# marcas" a **ventas/marca activa/semana** (liquidez) | Reorienta toda la empresa | Inmediato |
| **P0** | **Rediseñar el pricing**: comisión/híbrido en vez de suscripción fija a baja liquidez | Frena churn de oferta | 0–3 meses |
| **P0** | **Estrechar el mercado** a un nicho/ciudad/categoría | Hace la liquidez alcanzable | 0–3 meses |
| **P1** | Construir **demanda orgánica** (contenido/comunidad), no comprarla | Salva la economía unitaria | 0–12 meses |
| **P1** | Explotar la **curaduría/IA + datos** como moat | Defensibilidad | 6–18 meses |
| **P2** | Atacar el **85% de abandono** (checkout, pagos locales, confianza) | Sube conversión | 3–12 meses |
| **P2** | Diseñar el **roadmap de monetización acoplada al GMV** (ads, datos, financiero) | Rompe el techo de ingreso | 12–36 meses |
| **P3** | Expansión geográfica **por liquidez probada** | Crecimiento sostenible | 36–60 meses |

---

## Anexo A — Notas metodológicas y supuestos

**Conversión monetaria.** CLP/USD = 950 (promedio 2025). Sensibilidad: ±10% mueve todas las cifras USD ±10% pero no altera conclusiones.

**Supuestos de unit economics de marca.** Precio prenda CLP 50.000; margen bruto base 55% (sensibilizado 33%/50%/60%). "Recuperar suscripción" = utilidad bruta = CLP 100.000. "ROI 3×" = utilidad bruta = CLP 300.000 (versión neta en Anexo B).

**Supuestos de funnel (consumidor).** Ver tabla §6.1. Nota crítica: el "% de descargas activo" base (22%) es **optimista** frente a la retención D30 de apps de shopping (~5–10% [D]); se justifica solo si Moder logra un producto muy pegajoso. Recomendamos validar con datos propios cuanto antes.

**Supuestos del P&L de Moder.** Opex anual cargado por etapa: 50→US$150k; 100→US$250k; 250→US$450k; 500→US$700k; 1.000→US$1,1M. CAC marca (B2B): US$700/450/300 (cons/base/opt). Margen bruto software 75%. Adquisición de consumidor anual ≈ instalaciones necesarias × (1 − % orgánico) × CPI (simplificación: trata las instalaciones requeridas como reposición anual de la base, dado el alto churn; es conservador para bases de baja retención).

**Niveles de confianza.** [V] verificado adversarialmente; [D] direccional (market research comercial); [M] modelo propio. Las casas de market research difieren significativamente entre sí; las cifras [D] son para magnitud, no precisión.

**Limitaciones declaradas.** No se obtuvo fuente primaria auditada para: TAM/SAM/SOM Chile/LatAm; CAC Meta/TikTok específicos de Chile; LTV/frecuencia/retención del consumidor de moda chileno. El supuesto de margen 1,5× del fundador se reemplazó por 55% (evidencia [D]); el único benchmark de margen de apparel propuesto en verificación (Zalando 43,5%) fue **refutado** y no se usó. Comparables (Zalando, Lyst) tienen modelos distintos al de Moder.

---

## Anexo B — Anexo técnico de fórmulas (para actualizar el modelo)

Variables: `SUB` = suscripción mensual (CLP); `P` = precio prenda (CLP); `m` = margen bruto de marca; `FX` = CLP/USD.

**1. Economía de marca**
- Utilidad por prenda: `u = P · m`  (equivalente: con markup `k`, `m = (k−1)/k`, `u = P·(k−1)/k`)
- Prendas para recuperar suscripción: `BE = SUB / u`
- Prendas para ROI 3× (bruto): `Q3 = 3·SUB / u`
- Prendas para ROI 3× (neto): `Q3n = (SUB + 3·SUB) / u = 4·SUB / u`
- Take rate efectivo a `v` ventas/mes: `TR(v) = SUB / (v·P)`
- Ventas para take rate objetivo `t`: `v* = SUB / (t·P)`

**2. Ingreso Moder (suscripción)**
- `ARR = N · SUB · 12`;  `ARR_USD = ARR / FX`  (N = nº de marcas)

**3. Funnel de consumidor** (parámetros: `a`=% activo, `c`=conversión mensual de MAU, `i`=ítems/orden, `s`=DAU/MAU; `vpb`=ventas objetivo/marca)
- Ventas totales: `S = N · vpb`
- MAU: `MAU = S / (c · i)`
- Descargas acumuladas: `INST = MAU / a`
- DAU: `DAU = MAU · s`
- Compradores/mes: `B = S / i`

**4. Costo de adquisición**
- Costo descargas canal X: `Cx = INST · CPIx · FX`  (CPI en USD)
- Con orgánico `g`: descargas pagadas `INSTp = INST · (1−g)`; costo `= INSTp · CPIx · FX`
- CAC por comprador: `CAC_B = (INST · CPI · FX) / B`

**5. P&L Moder (anual)**
- Acq. consumidor: `AC = INST · (1−g) · CPI · FX / FX = INST·(1−g)·CPI` (USD)
- Acq. marca: `AM = N · churn · CAC_marca`
- `EBITDA = ARR_USD − AC − AM − Opex`

**6. LTV / CAC / Payback (lado marca)**
- `ARPA = SUB·12/FX`; vida media `= 1/churn`; `LTV = ARPA · (1/churn) · m_sw` (m_sw = margen software)
- `LTV/CAC = LTV / CAC_marca`; `Payback (meses) = CAC_marca / (ARPA · m_sw / 12)`
- **Fully-loaded:** contribución neta/marca `= ARPA − (AC/N) − (AM/N)`; usar esto para el LTV/CAC realista.

**7. Break-even (suscripción)**
- Contribución neta/marca `cn = ARPA − AC/N − AM/N`
- Marcas para EBITDA≥0: `N* = Opex / cn`

**8. Valoración**
- Suscripción: `EV = ARR_USD · múltiplo` (2,4× Lyst / 6× SaaS mediano / 8–12× alto crecimiento)
- Con take rate: `Rev = GMV · t`; `GMV = S · P · 12 / FX`; `EV = Rev · múltiplo`

*El script `docs/moder_model.py` implementa todas estas fórmulas y reproduce cada tabla; modifíquense los parámetros del diccionario `scen` y los supuestos maestros para actualizar el modelo.*

---

## Anexo C — Bibliografía

**Fuentes verificadas (primaria / secundaria de alta calidad) [V]**
1. Zalando SE — *Annual Report 2024 / FY2024 Results* (corporate.zalando.com/investor-relations). Clientes activos 51,8M; GMV €15,3B; ingresos €10,6B; EBIT ajustado 4,8%.
2. TechCrunch (9 abr 2025) — *"Lyst, the fashion marketplace once valued at $700M, sells to Japan's ZOZO for $154M"* (corroborado por Business of Fashion, WWD, PYMNTS, Companies House, comunicado de ZOZO). Ingresos ~£50,1M; múltiplo ~2,4×; 190 mercados, 27.000 marcas.
3. Andreessen Horowitz (a16z) — *"13 Metrics for Marketplace Companies"* (definiciones canónicas: liquidez, GMV, take rate, repeat purchase; triangulado con Reforge, NFX, Sharetribe). *Nota: a16z es técnicamente un blog pero es la referencia canónica de la industria; usado solo para definiciones, no para cifras de mercado.*

**Fuentes direccionales (market research / agregadores) [D]**
4. Statista Market Forecast — *Fashion / Apparel — Chile* (ingreso e-commerce moda US$2.393M 2025; apparel 52%; penetración; add-to-cart 10–10,5%; abandono 84,5–85%).
5. Mobility Foresights — *Latin America Online Fashion Market* (US$73,8B 2025 → US$167,5B 2031; share online 28,9%).
6. Cognitive Market Research / Marketintelo — *South America / Latin Fashion Apparel Market* (US$87,9B 2024).
7. Baymard Institute — *Cart Abandonment Rate* (promedio 70,2%; moda 72–74%; 48% abandona por costos inesperados).
8. Business of Apps — *App User Acquisition Costs (2025) / Cost per Install* (CPI shopping LatAm US$0,50–2,00; TikTok US$1,75–4; Meta >US$2).
9. Mapendo — *Cost per Install by Country 2025*.
10. TrueProfit / FashionUnited / comps públicos — márgenes brutos de apparel por categoría (fast fashion 30–48%; DTC 50–60%; lujo 60–70%; mediana comps 55,3%).
11. Aventis Advisors / Multiples.vc / Value Add VC — múltiplos SaaS EV/Revenue 2024–2026 (mediano ~6×; alto crecimiento 8–12×; bajo 1–2×).
12. Etsy Inc. — comunicado de adquisición de Depop (US$1,625B, 2021; 90% Gen Z).
13. Coberturas de Vinted y Poshmark (Failory, prensa) — historia de cold-start community-led; Poshmark IPO ~US$3B 2021.
14. exchange-rates.org / X-Rates — CLP/USD promedio 2025 ≈ 951.

**Fuentes consultadas con baja confiabilidad (no usadas como evidencia principal):** Grand View Research, Expert Market Research, Mordor Intelligence, FirstPageSage, NFX (post de tácticas, usado solo direccionalmente para cold-start).

---

*Fin del documento. El modelo cuantitativo es reproducible vía `docs/moder_model.py`. Toda cifra marcada [D] debe refinarse con datos primarios de Moder antes de decisiones de capital.*
