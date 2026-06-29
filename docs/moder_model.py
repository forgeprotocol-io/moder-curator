#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modelo financiero Moder — genera todas las tablas del informe.
Todos los supuestos estan parametrizados y documentados.
"""

FX = 950.0  # CLP por USD (promedio 2025, ~951 segun exchange-rates.org)
SUB_M = 100_000          # suscripcion mensual CLP
SUB_Y = SUB_M * 12       # 1.200.000 CLP/ano
PRENDA = 50_000          # precio prenda promedio CLP

def usd(clp): return clp / FX

print("="*70)
print("1) ECONOMIA UNITARIA DEL LADO MARCA (markup -> margen bruto)")
print("="*70)
print(f"{'Markup':>7} {'GM%':>6} {'Util/prenda':>12} {'BE prendas':>11} {'ROI3x prendas':>14} {'GMV BE':>10} {'TakeRate@BE':>12}")
for mk in [1.5, 2.0, 2.5]:
    costo = PRENDA/mk
    util = PRENDA - costo
    gm = util/PRENDA
    be = SUB_M/util
    roi3 = 3*SUB_M/util
    gmv_be = be*PRENDA
    take_be = SUB_M/gmv_be
    print(f"{mk:>6}x {gm*100:>5.0f}% {util:>12,.0f} {be:>11.1f} {roi3:>14.1f} {gmv_be:>10,.0f} {take_be*100:>11.0f}%")

print()
print("Take rate efectivo (suscripcion/GMV) segun ventas/mes de la marca:")
print(f"(margen bruto base = 55% -> util/prenda = {PRENDA*0.55:,.0f} CLP)")
GM_REAL = 0.55
util_real = PRENDA*GM_REAL
print(f"{'Ventas/mes':>10} {'GMV/mes':>12} {'Util bruta':>11} {'TakeRate':>9} {'Cubre sub?':>10}")
for v in [1,2,4,7,11,13,20,30]:
    gmv = v*PRENDA
    ub = v*util_real
    tr = SUB_M/gmv
    cubre = "si" if ub>=SUB_M else "no"
    print(f"{v:>10} {gmv:>12,.0f} {ub:>11,.0f} {tr*100:>8.0f}% {cubre:>10}")

print()
print("="*70)
print("2) INGRESO MODER POR # MARCAS (solo suscripcion)")
print("="*70)
print(f"{'Marcas':>7} {'MRR CLP':>12} {'ARR CLP':>14} {'ARR USD':>10}")
brand_counts = [50,100,150,250,350]
for n in brand_counts:
    mrr = n*SUB_M
    arr = n*SUB_Y
    print(f"{n:>7} {mrr:>12,.0f} {arr:>14,.0f} {usd(arr):>10,.0f}")

print()
print("="*70)
print("3) FUNNEL DE CONSUMIDOR — escenarios (para 50 marcas felices)")
print("="*70)
# escenarios: (nombre, active%, conv mensual buyer/MAU, items/order, DAU/MAU, ventas/marca objetivo)
scen = {
  "Conservador": dict(active=0.15, conv=0.02, items=1.2, stick=0.12, vpb=6,  cpi_meta=2.0, cpi_tt=3.0, organic=0.30, churn=0.40),
  "Base":        dict(active=0.22, conv=0.03, items=1.3, stick=0.15, vpb=10, cpi_meta=1.5, cpi_tt=2.5, organic=0.50, churn=0.25),
  "Optimista":   dict(active=0.30, conv=0.04, items=1.5, stick=0.20, vpb=15, cpi_meta=1.0, cpi_tt=1.75,organic=0.65, churn=0.15),
}
N0 = 50
for name,s in scen.items():
    sales = N0*s['vpb']
    mau = sales/(s['conv']*s['items'])
    installs = mau/s['active']
    dau = mau*s['stick']
    print(f"\n[{name}] ventas/marca={s['vpb']} -> ventas totales/mes={sales:,.0f}")
    print(f"   MAU={mau:,.0f} | DAU={dau:,.0f} | descargas acumuladas necesarias={installs:,.0f}")
    print(f"   %descargas activa={s['active']*100:.0f}% | conv compra(MAU)={s['conv']*100:.0f}% | items/orden={s['items']} | DAU/MAU={s['stick']*100:.0f}%")
    # costo descargas Meta vs TikTok (CPI en USD -> CLP)
    cost_meta = installs*s['cpi_meta']*FX
    cost_tt = installs*s['cpi_tt']*FX
    paid_inst = installs*(1-s['organic'])
    cost_meta_org = paid_inst*s['cpi_meta']*FX
    print(f"   Costo 100% Meta (CPI ${s['cpi_meta']}): {cost_meta:,.0f} CLP (${usd(cost_meta):,.0f})")
    print(f"   Costo 100% TikTok (CPI ${s['cpi_tt']}): {cost_tt:,.0f} CLP (${usd(cost_tt):,.0f})")
    print(f"   Con {s['organic']*100:.0f}% organico, descargas pagadas={paid_inst:,.0f}; costo Meta={cost_meta_org:,.0f} CLP (${usd(cost_meta_org):,.0f})")
    # CAC por comprador
    buyers = sales/s['items']  # compradores activos/mes
    cac_buyer_meta = (installs*s['cpi_meta']*FX)/buyers
    print(f"   Compradores/mes={buyers:,.0f} | CAC/comprador (Meta, sin organico)={cac_buyer_meta:,.0f} CLP (${usd(cac_buyer_meta):,.0f})")

print()
print("="*70)
print("4) P&L MODER — escenarios x # marcas (solo suscripcion)")
print("="*70)
# opex anual USD por etapa (equipo+tech+infra), cargado
opex_stage = {50:150_000, 100:250_000, 150:320_000, 250:450_000, 350:550_000}
# Escenario "micro-equipo" full-organico (2-3 personas) para el techo de 350:
opex_micro = 250_000
# CAC marca (B2B venta) USD
cac_brand = {"Conservador":700,"Base":450,"Optimista":300}
for name,s in scen.items():
    print(f"\n--- Escenario {name} ---")
    print(f"{'Marcas':>7} {'ARR USD':>9} {'AcqCons USD':>12} {'AcqMarca USD':>13} {'Opex USD':>9} {'EBITDA USD':>11} {'Margen':>7}")
    for n in brand_counts:
        arr = usd(n*SUB_Y)
        # consumer acq anual: sostener base; descargas pagadas ~ para servir ventas a n marcas
        sales = n*s['vpb']
        mau = sales/(s['conv']*s['items'])
        installs = mau/s['active']
        # anual: reponer churn de base activa ~ 1x base/ano (retencion baja) + sin crecer
        paid_inst_yr = installs*(1-s['organic'])
        acq_cons = usd(paid_inst_yr*s['cpi_meta']*FX)
        # acq marca: reponer churn anual de marcas
        acq_marca = n*s['churn']*cac_brand[name]
        opex = opex_stage[n]
        ebitda = arr - acq_cons - acq_marca - opex
        margin = ebitda/arr if arr else 0
        print(f"{n:>7} {arr:>9,.0f} {acq_cons:>12,.0f} {acq_marca:>13,.0f} {opex:>9,.0f} {ebitda:>11,.0f} {margin*100:>6.0f}%")

print()
print("="*70)
print("5) PUNTO DE EQUILIBRIO (solo suscripcion, escenario Base)")
print("="*70)
s = scen["Base"]
# marcas necesarias para cubrir opex+CAC. Aproximar a cada etapa de opex.
print("Marcas necesarias para EBITDA>=0 dado opex por etapa (Base):")
for n_opex,opex in opex_stage.items():
    # ingreso por marca neto de CAC consumidor marginal y CAC marca
    sales_pb = s['vpb']
    mau_pb = sales_pb/(s['conv']*s['items'])
    inst_pb = mau_pb/s['active']
    acq_cons_pb = usd(inst_pb*(1-s['organic'])*s['cpi_meta']*FX)
    acq_marca_pb = s['churn']*cac_brand['Base']
    net_pb = usd(SUB_Y) - acq_cons_pb - acq_marca_pb
    be_brands = opex/net_pb if net_pb>0 else float('inf')
    print(f"   opex ${opex:,.0f}: contribucion neta/marca=${net_pb:,.0f} -> BE={be_brands:,.0f} marcas")

print()
print("="*70)
print("6) VALORACION POTENCIAL (solo suscripcion)")
print("="*70)
print(f"{'Marcas':>7} {'ARR USD':>10} {'2.4x(Lyst)':>12} {'4x':>10} {'6x(SaaS med)':>13} {'10x(hi-growth)':>15}")
for n in brand_counts:
    arr = usd(n*SUB_Y)
    print(f"{n:>7} {arr:>10,.0f} {arr*2.4:>12,.0f} {arr*4:>10,.0f} {arr*6:>13,.0f} {arr*10:>15,.0f}")

print()
print("Comparacion: modelo con take-rate sobre GMV (12%) si Moder capturara comision")
print(f"{'Marcas':>7} {'GMV/mes USD':>12} {'GMV/ano USD':>13} {'Rev@12% USD':>13} {'EV@4xRev':>12}")
for n in brand_counts:
    sales = n*scen['Base']['vpb']
    gmv_m = usd(sales*PRENDA)
    gmv_y = gmv_m*12
    rev = gmv_y*0.12
    print(f"{n:>7} {gmv_m:>12,.0f} {gmv_y:>13,.0f} {rev:>13,.0f} {rev*4:>12,.0f}")

print()
print("="*70)
print("7) REALITY CHECK — TECHO REALISTA = 350 TIENDAS")
print("="*70)
CEIL = 350
arr_ceil = usd(CEIL*SUB_Y)
print(f"ARR maximo (350 tiendas, suscripcion): {CEIL*SUB_Y:,.0f} CLP = ${arr_ceil:,.0f}")
print(f"\nEscenario Base (CAC consumidor via paid) a 350 tiendas:")
s = scen["Base"]
sales = CEIL*s['vpb']; mau = sales/(s['conv']*s['items']); inst = mau/s['active']
acq_cons = usd(inst*(1-s['organic'])*s['cpi_meta']*FX)
acq_marca = CEIL*s['churn']*cac_brand['Base']
for label,opex in [("equipo normal $550k",550_000),("micro-equipo $250k",250_000)]:
    ebitda = arr_ceil - acq_cons - acq_marca - opex
    print(f"   {label}: ARR ${arr_ceil:,.0f} - acqCons ${acq_cons:,.0f} - acqMarca ${acq_marca:,.0f} - opex ${opex:,.0f} = EBITDA ${ebitda:,.0f}")
print(f"\nMEJOR CASO ABSOLUTO: full-organico (CAC consumidor ~0) + micro-equipo:")
for opex in [250_000, 180_000, 120_000]:
    contrib = arr_ceil - acq_marca  # sin acq consumidor
    ebitda = contrib - opex
    print(f"   opex ${opex:,.0f}: EBITDA ${ebitda:,.0f} (margen {ebitda/arr_ceil*100:.0f}%)")
print(f"\nValoracion a 350 tiendas (suscripcion):")
for mult,lbl in [(2.4,"2.4x Lyst"),(6,"6x SaaS"),(10,"10x hi-growth")]:
    print(f"   {lbl}: ${arr_ceil*mult:,.0f}")
print(f"\nBrecha de break-even: contribucion neta/marca (base) ~$277 -> ")
print(f"   marcas para cubrir opex $550k = {550_000/277:,.0f} (vs techo de 350)")
print(f"   marcas para cubrir opex $250k = {250_000/277:,.0f} (vs techo de 350)")
