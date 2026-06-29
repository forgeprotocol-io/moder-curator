#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modelo financiero Moder — moneda principal: PESOS CHILENOS (CLP).
Los CPI de adquisicion vienen en USD (benchmarks globales) y se convierten a CLP a FX.
Todas las cifras de salida estan en CLP (M = millones de CLP).
"""

FX = 950.0               # CLP por USD (promedio 2025 ~951)
SUB_M = 100_000          # suscripcion mensual CLP
SUB_Y = SUB_M * 12       # 1.200.000 CLP/ano
PRENDA = 50_000          # precio prenda promedio CLP
MM = 1_000_000.0         # 1 millon CLP

def mm(clp): return clp/MM   # a millones de CLP

print("="*74)
print("1) ECONOMIA UNITARIA DEL LADO MARCA (markup -> margen bruto) — CLP")
print("="*74)
print(f"{'Markup':>7} {'GM%':>6} {'Util/prenda':>12} {'BE prendas':>11} {'ROI3x prendas':>14} {'GMV BE':>10} {'TakeRate@BE':>12}")
for mk in [1.5, 2.0, 2.5]:
    costo = PRENDA/mk; util = PRENDA - costo; gm = util/PRENDA
    be = SUB_M/util; roi3 = 3*SUB_M/util; gmv_be = be*PRENDA; take_be = SUB_M/gmv_be
    print(f"{mk:>6}x {gm*100:>5.0f}% {util:>12,.0f} {be:>11.1f} {roi3:>14.1f} {gmv_be:>10,.0f} {take_be*100:>11.0f}%")

print()
GM_REAL = 0.55; util_real = PRENDA*GM_REAL
print(f"Take rate efectivo (suscripcion/GMV) por ventas/mes (margen base 55%, util/prenda={util_real:,.0f} CLP):")
print(f"{'Ventas/mes':>10} {'GMV/mes CLP':>13} {'Util bruta CLP':>15} {'TakeRate':>9} {'Cubre sub?':>10}")
for v in [1,2,4,7,11,13,20,30]:
    gmv = v*PRENDA; ub = v*util_real; tr = SUB_M/gmv
    print(f"{v:>10} {gmv:>13,.0f} {ub:>15,.0f} {tr*100:>8.0f}% {('si' if ub>=SUB_M else 'no'):>10}")

print()
print("="*74)
print("2) INGRESO MODER POR # MARCAS (solo suscripcion) — CLP")
print("="*74)
print(f"{'Marcas':>7} {'MRR (CLP)':>14} {'ARR (CLP)':>16} {'ARR (M CLP)':>12}")
brand_counts = [50,100,150,250,350]
for n in brand_counts:
    print(f"{n:>7} {n*SUB_M:>14,.0f} {n*SUB_Y:>16,.0f} {mm(n*SUB_Y):>12,.1f}")

print()
print("="*74)
print("3) FUNNEL DE CONSUMIDOR — escenarios (para 50 marcas felices) — CLP")
print("="*74)
scen = {
  "Conservador": dict(active=0.15, conv=0.02, items=1.2, stick=0.12, vpb=6,  cpi_meta=2.0, cpi_tt=3.0, organic=0.30, churn=0.40),
  "Base":        dict(active=0.22, conv=0.03, items=1.3, stick=0.15, vpb=10, cpi_meta=1.5, cpi_tt=2.5, organic=0.50, churn=0.25),
  "Optimista":   dict(active=0.30, conv=0.04, items=1.5, stick=0.20, vpb=15, cpi_meta=1.0, cpi_tt=1.75,organic=0.65, churn=0.15),
}
N0 = 50
for name,s in scen.items():
    sales = N0*s['vpb']; mau = sales/(s['conv']*s['items']); installs = mau/s['active']; dau = mau*s['stick']
    print(f"\n[{name}] ventas/marca={s['vpb']} -> ventas/mes={sales:,.0f} | MAU={mau:,.0f} | DAU={dau:,.0f} | descargas acum.={installs:,.0f}")
    cpi_meta_clp = s['cpi_meta']*FX; cpi_tt_clp = s['cpi_tt']*FX
    cost_meta = installs*cpi_meta_clp; cost_tt = installs*cpi_tt_clp
    paid_inst = installs*(1-s['organic']); cost_meta_org = paid_inst*cpi_meta_clp
    print(f"   CPI Meta={cpi_meta_clp:,.0f} CLP | CPI TikTok={cpi_tt_clp:,.0f} CLP")
    print(f"   Costo 100% Meta: {cost_meta:,.0f} CLP ({mm(cost_meta):,.1f} M)")
    print(f"   Costo 100% TikTok: {cost_tt:,.0f} CLP ({mm(cost_tt):,.1f} M)")
    print(f"   Con {s['organic']*100:.0f}% organico (pagadas={paid_inst:,.0f}): Meta {cost_meta_org:,.0f} CLP ({mm(cost_meta_org):,.1f} M)")
    buyers = sales/s['items']; cac_buyer = cost_meta/buyers
    print(f"   Compradores/mes={buyers:,.0f} | CAC/comprador (Meta, sin organico)={cac_buyer:,.0f} CLP")

print()
print("="*74)
print("4) P&L MODER — escenarios x # marcas (solo suscripcion) — M CLP")
print("="*74)
# opex y CAC marca definidos en USD (benchmarks) -> convertidos a CLP
opex_stage_usd = {50:150_000, 100:250_000, 150:320_000, 250:450_000, 350:550_000}
opex_stage = {k:v*FX for k,v in opex_stage_usd.items()}
cac_brand_usd = {"Conservador":700,"Base":450,"Optimista":300}
cac_brand = {k:v*FX for k,v in cac_brand_usd.items()}
for name,s in scen.items():
    print(f"\n--- Escenario {name} (M CLP) ---")
    print(f"{'Marcas':>7} {'ARR':>8} {'AcqCons':>9} {'AcqMarca':>9} {'Opex':>8} {'EBITDA':>9} {'Margen':>7}")
    for n in brand_counts:
        arr = n*SUB_Y
        sales = n*s['vpb']; mau = sales/(s['conv']*s['items']); installs = mau/s['active']
        acq_cons = installs*(1-s['organic'])*s['cpi_meta']*FX
        acq_marca = n*s['churn']*cac_brand[name]
        opex = opex_stage[n]
        ebitda = arr - acq_cons - acq_marca - opex
        print(f"{n:>7} {mm(arr):>8,.1f} {mm(acq_cons):>9,.1f} {mm(acq_marca):>9,.1f} {mm(opex):>8,.1f} {mm(ebitda):>9,.1f} {ebitda/arr*100:>6.0f}%")

print()
print("="*74)
print("5) PUNTO DE EQUILIBRIO (suscripcion, escenario Base) — CLP")
print("="*74)
s = scen["Base"]
sales_pb = s['vpb']; mau_pb = sales_pb/(s['conv']*s['items']); inst_pb = mau_pb/s['active']
acq_cons_pb = inst_pb*(1-s['organic'])*s['cpi_meta']*FX
acq_marca_pb = s['churn']*cac_brand['Base']
net_pb = SUB_Y - acq_cons_pb - acq_marca_pb
print(f"Contribucion neta por marca (Base) = {net_pb:,.0f} CLP/ano")
for n_opex,opex in opex_stage.items():
    be = opex/net_pb if net_pb>0 else float('inf')
    print(f"   opex {mm(opex):,.1f} M CLP: BE = {be:,.0f} marcas")

print()
print("="*74)
print("6) VALORACION POTENCIAL (suscripcion) — M CLP")
print("="*74)
print(f"{'Marcas':>7} {'ARR':>8} {'2.4x(Lyst)':>11} {'6x(SaaS)':>10} {'10x(hi)':>9}")
for n in brand_counts:
    arr = n*SUB_Y
    print(f"{n:>7} {mm(arr):>8,.1f} {mm(arr*2.4):>11,.1f} {mm(arr*6):>10,.1f} {mm(arr*10):>9,.1f}")
print("\nModelo con take-rate 12% sobre GMV (M CLP):")
print(f"{'Marcas':>7} {'GMV/ano':>9} {'Rev@12%':>9} {'EV@4x':>8}")
for n in brand_counts:
    gmv_y = n*scen['Base']['vpb']*PRENDA*12; rev = gmv_y*0.12
    print(f"{n:>7} {mm(gmv_y):>9,.1f} {mm(rev):>9,.1f} {mm(rev*4):>8,.1f}")

print()
print("="*74)
print("7) REALITY CHECK — TECHO REALISTA = 350 TIENDAS — CLP")
print("="*74)
CEIL = 350; arr_ceil = CEIL*SUB_Y
print(f"ARR maximo (350 tiendas): {arr_ceil:,.0f} CLP ({mm(arr_ceil):,.1f} M CLP)")
s = scen["Base"]
sales = CEIL*s['vpb']; mau = sales/(s['conv']*s['items']); inst = mau/s['active']
acq_cons = inst*(1-s['organic'])*s['cpi_meta']*FX
acq_marca = CEIL*s['churn']*cac_brand['Base']
print("\nA 350 tiendas (M CLP):")
for label,opex in [("Base, equipo normal", 550_000*FX),("Base, micro-equipo", 250_000*FX)]:
    ebitda = arr_ceil - acq_cons - acq_marca - opex
    print(f"   {label}: ARR {mm(arr_ceil):,.1f} - AcqCons {mm(acq_cons):,.1f} - AcqMarca {mm(acq_marca):,.1f} - Opex {mm(opex):,.1f} = EBITDA {mm(ebitda):,.1f} ({ebitda/arr_ceil*100:.0f}%)")
print("\nMEJOR CASO: full-organico (CAC consumidor ~0) + micro-equipo (M CLP):")
for opex_usd in [250_000, 180_000, 120_000]:
    opex = opex_usd*FX; ebitda = arr_ceil - acq_marca - opex
    print(f"   opex {mm(opex):,.1f} M: EBITDA {mm(ebitda):,.1f} M ({ebitda/arr_ceil*100:.0f}%)")
print("\nValoracion a 350 tiendas (M CLP):")
for mult,lbl in [(2.4,"2.4x Lyst"),(6,"6x SaaS"),(10,"10x hi-growth")]:
    print(f"   {lbl}: {mm(arr_ceil*mult):,.1f} M CLP")
print(f"\nBrecha break-even: contrib neta/marca (base) ~{net_pb:,.0f} CLP")
print(f"   marcas para opex 550k USD = {550_000*FX/net_pb:,.0f}; para 250k USD = {250_000*FX/net_pb:,.0f} (vs techo 350)")
