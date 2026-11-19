const { chromium } = require('playwright');
(async () => {
  const [,, html, pdf, prevDir] = process.argv;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1333, height: 750 }, deviceScaleFactor: 1 });
  await page.goto('file://' + html, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: pdf, width: '1333px', height: '750px', printBackground: true, preferCSSPageSize: true });
  const n = await page.locator('section.slide').count();
  for (let i = 0; i < n; i++) {
    await page.locator('section.slide').nth(i).screenshot({ path: `${prevDir}/s${String(i+1).padStart(2,'0')}.png` });
  }
  const fonts = await page.evaluate(() => [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+f.weight));
  console.log('slides', n, 'fonts', fonts.join(','));
  await browser.close();
})();
