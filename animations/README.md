# Atlas AI Metric Count Animations

This directory contains the Atlas website metric animation assets based on the uploaded visual references:

- `Better_grades_01.png` → circular count animation to `73%`
- `Active_user_01.png` → text count animation to `12K+`
- `Faster_work_01.png` → text count animation to `3X`
- `Satisfied_customers_01.png` → circular count animation to `91%`
- `Timesaving_01.png` → circular count animation to `87%`
- `Up-time_01.png` → text count animation to `98%`
- `User_satifaction_01.png` → text count animation to `94%`

## Assets

- `index.html` — standalone gallery page for preview or iframe embedding.
- `better-grades-73.css` — shared visual styling for the metric animations.
- `better-grades-73.js` — shared count-up and circular progress animation logic.
- `animation-spec.json` — implementation metadata and animation parameters.

## Behaviour

Each animation starts at `0` and counts up to the designated value from the uploaded reference image. Circular metrics also fill the blue circular progress ring clockwise from the top position. Text-only metrics count the value without a circular bar.

## Current animation settings

- Maximum duration: `2.8 seconds`
- Hard JavaScript cap: `3.0 seconds`
- Easing: `easeOutQuint`, so the count and ring movement slow down toward the end
- Primary font: `Roboto Slab`, selected as the closest matching web-safe font family for the uploaded reference images
- Fallback font: `Roboto`

## Implementation notes

- The visuals are HTML/CSS/SVG-based for sharp rendering at large sizes.
- No new images are generated or required.
- The animation respects `prefers-reduced-motion` by showing the final state immediately when reduced motion is enabled.
