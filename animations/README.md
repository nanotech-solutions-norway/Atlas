# Atlas AI Metric Animations

This directory currently keeps the `/animations/` entry point focused on the active 92% animation only, while also containing separate standalone Wix Custom Element animation files for additional values.

## Active demo entry point

- `index.html` — public demo entry point showing only the 92% animation.
- `metric-92.js` — Wix Custom Element server file for 92%.
- `metric-92-demo.html` — standalone preview page using the same 92% custom element.
- `metric-92.svg` — SVG backup/reference version.
- `animation-spec.json` — implementation metadata for the active 92% animation.

## Additional standalone circular animations

- `metric-99-9.js` — Wix Custom Element server file for 99.9%.
- `metric-99-9-demo.html` — standalone preview page for the 99.9% custom element.
- `metric-65.js` — Wix Custom Element server file for 65%.
- `metric-65-demo.html` — standalone preview page for the 65% custom element.

## Additional standalone text-only animations

- `metric-12-2.js` — Wix Custom Element server file for 12.2% text count only.
- `metric-12-2-demo.html` — standalone preview page for the 12.2% text-only custom element.
- `metric-gt-40.js` — Wix Custom Element server file for >40% text count only. The `>` symbol appears only after counting is completed.
- `metric-gt-40-demo.html` — standalone preview page for the >40% text-only custom element.
- `metric-25-1.js` — Wix Custom Element server file for 25.1% text count only.
- `metric-25-1-demo.html` — standalone preview page for the 25.1% text-only custom element.

## Wix Custom Element values

### 92%

Server URL:

`https://nanotech-solutions-norway.github.io/Atlas/animations/metric-92.js`

Tag name:

`atlas-metric-92`

### 99.9%

Server URL:

`https://nanotech-solutions-norway.github.io/Atlas/animations/metric-99-9.js`

Tag name:

`atlas-metric-99-9`

### 65%

Server URL:

`https://nanotech-solutions-norway.github.io/Atlas/animations/metric-65.js`

Tag name:

`atlas-metric-65`

### 12.2% text only

Server URL:

`https://nanotech-solutions-norway.github.io/Atlas/animations/metric-12-2.js`

Tag name:

`atlas-metric-12-2`

### >40% text only

Server URL:

`https://nanotech-solutions-norway.github.io/Atlas/animations/metric-gt-40.js`

Tag name:

`atlas-metric-gt-40`

### 25.1% text only

Server URL:

`https://nanotech-solutions-norway.github.io/Atlas/animations/metric-25-1.js`

Tag name:

`atlas-metric-25-1`

## Shared styling and behavior

### Circular animations

- Font: Inter Regular
- Fallback: Roboto
- Font size: 48px
- Font weight: 400
- Bold: false
- Background: transparent
- Circular bar: enabled
- Duration: 2.8 seconds, capped below 3.0 seconds
- Reveal behavior: animation starts only when the custom element is revealed in the viewport

### Text-only animations

- Font: Inter Regular
- Fallback: Roboto
- Font size: 64px
- Font weight: 400
- Bold: false
- Background: transparent
- Circular bar: disabled
- Duration: 2.8 seconds, capped below 3.0 seconds
- Reveal behavior: animation starts only when the custom element is revealed in the viewport

## Notes

The old multi-animation gallery has been removed from the active demo path. The `/animations/` URL now loads only the current 92% animation. Additional metric values are available through their standalone demo pages and server URLs.
