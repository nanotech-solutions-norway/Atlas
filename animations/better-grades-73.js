(() => {
  const visuals = Array.from(document.querySelectorAll('[data-target]'));
  if (!visuals.length) return;

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

  // Strong ease-out curve: fast initial movement with a clear slowdown toward the final state.
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
