# Propuesta comercial MODÈR v2 — fuente editable

- `build/deck.html`: los 15 slides (HTML + CSS). Edita los textos aquí.
- `assets/`: fotos del deck original y tipografías (Gilda Display e Inter, licencia OFL).
- Para regenerar el PDF (requiere Node + Playwright):
  `node render.js "$PWD/build/deck.html" "$PWD/../Moder_Propuesta_Comercial_v2.pdf" /tmp`
