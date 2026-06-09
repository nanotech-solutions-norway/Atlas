# Better Grades 73% Circular Progress Animation

This directory contains the Atlas website animation asset based on the uploaded `Better_grades_01.png` reference image.

## Asset

- `index.html` — standalone animation page for preview or iframe embedding.
- `better-grades-73.css` — visual styling for the circular bar chart.
- `better-grades-73.js` — count-up and circular progress animation logic.
- `animation-spec.json` — implementation metadata and animation parameters.

## Behaviour

The animation starts at `0%`, counts up to `73%`, and fills the blue circular progress ring clockwise from the top position until the target value is reached.

## Implementation notes

- No external libraries are used.
- The visual is SVG-based for sharp rendering at large sizes.
- The directory name `animarions` follows the requested GitHub folder name exactly.
- The animation respects `prefers-reduced-motion` by showing the final 73% state immediately when reduced motion is enabled.
