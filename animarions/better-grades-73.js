(() => {
  const visual = document.querySelector('[data-target]');
  const ring = document.querySelector('.progress-value');
  const number = document.querySelector('.progress-number');

  if (!visual || !ring || !number) return;

  const target = Number.parseFloat(visual.dataset.target || '73');
  const duration = Number.parseInt(visual.dataset.duration || '1700', 10);
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const clamp = (value, min, max) => Math.min(Math.max(value, min), max);
  const eased = (t) => 1 - Math.pow(1 - t, 3);

  const setProgress = (value) => {
    const safeValue = clamp(value, 0, 100);
    ring.style.strokeDashoffset = String(100 - safeValue);
    number.textContent = String(Math.round(safeValue));
    visual.setAttribute('aria-label', `${Math.round(safeValue)} percent`);
  };

  if (reducedMotion) {
    setProgress(target);
    return;
  }

  setProgress(0);

  let startTime = null;

  const animate = (timestamp) => {
    if (startTime === null) startTime = timestamp;
    const elapsed = timestamp - startTime;
    const progress = clamp(elapsed / duration, 0, 1);
    const current = target * eased(progress);

    setProgress(current);

    if (progress < 1) {
      window.requestAnimationFrame(animate);
    } else {
      setProgress(target);
    }
  };

  window.requestAnimationFrame(animate);
})();
