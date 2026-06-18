(() => {
  const gallery = document.querySelector('.animation-gallery');

  if (gallery && !document.getElementById('metric-92')) {
    const section = document.createElement('section');
    section.id = 'metric-92';
    section.className = 'metric-card metric-card--ring';
    section.setAttribute('aria-label', '92 percent circular progress animation');
    section.innerHTML = `
      <div class="metric-visual" data-kind="ring" data-target="92" data-duration="2800" data-suffix="%">
        <svg class="progress-ring" viewBox="0 0 600 600" role="img" aria-label="92 percent circular progress indicator">
          <circle class="progress-track" cx="300" cy="300" r="250" pathLength="100"></circle>
          <circle class="progress-value" cx="300" cy="300" r="250" pathLength="100"></circle>
        </svg>
        <div class="metric-label" aria-live="polite"><span class="metric-number">0</span><span class="metric-suffix">%</span></div>
      </div>
    `;
    gallery.insertBefore(section, document.getElementById('time-saving'));
  }

  const visuals = Array.from(document.querySelectorAll('[data-target]'));
  if (!visuals.length) return;

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

  const easeOutQuint = (t) => 1 - Math.pow(1 - t, 5);

  const formatNumber = (value, format) => {
    if (format === 'compact') {
      if (value >= 1000) return `${Math.round(value / 1000)}K`;
      return String(Math.round(value));
    }
    return String(Math.round(value));
  };

  const setProgress = (visual, rawValue) => {
    const target = Number.parseFloat(visual.dataset.target || '0');
    const suffix = visual.dataset.suffix || '';
    const format = visual.dataset.format || 'integer';
    const safeValue = clamp(rawValue, 0, Math.max(target, 100));
    const number = visual.querySelector('.metric-number');
    const suffixNode = visual.querySelector('.metric-suffix');
    const ring = visual.querySelector('.progress-value');

    if (ring) {
      const percentage = clamp(safeValue, 0, 100);
      ring.style.strokeDashoffset = String(100 - percentage);
    }

    if (number) number.textContent = formatNumber(safeValue, format);
    if (suffixNode) suffixNode.textContent = suffix;
    visual.setAttribute('aria-label', `${formatNumber(target, format)}${suffix}`);
  };

  const animateVisual = (visual) => {
    const target = Number.parseFloat(visual.dataset.target || '0');
    const configuredDuration = Number.parseInt(visual.dataset.duration || '2800', 10);
    const duration = Math.min(configuredDuration, 3000);

    if (reducedMotion) {
      setProgress(visual, target);
      return;
    }

    setProgress(visual, 0);
    let startTime = null;

    const animate = (timestamp) => {
      if (startTime === null) startTime = timestamp;
      const elapsed = timestamp - startTime;
      const progress = clamp(elapsed / duration, 0, 1);
      const current = target * easeOutQuint(progress);

      setProgress(visual, current);

      if (progress < 1) {
        window.requestAnimationFrame(animate);
      } else {
        setProgress(visual, target);
      }
    };

    window.requestAnimationFrame(animate);
  };

  visuals.forEach(animateVisual);
})();
