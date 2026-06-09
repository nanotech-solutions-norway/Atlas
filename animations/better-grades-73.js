(() => {
  const visual = document.querySelector('[data-target]');
  const ring = document.querySelector('.progress-value');
  const number = document.querySelector('.progress-number');

  if (!visual || !ring || !number) return;

  const target = Number.parseFloat(visual.dataset.target || '73');
  const configuredDuration = Number.parseInt(visual.dataset.duration || '2800', 10);
  const duration = Math.min(configuredDuration, 3000);
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

  // Strong ease-out curve: fast initial movement with a clear slowdown toward the final 73% state.
  const easeOutQuint = (t) => 1 - Math.pow(1 - t, 5);

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
    const current = target * easeOutQuint(progress);

    setProgress(current);

    if (progress < 1) {
      window.requestAnimationFrame(animate);
    } else {
      setProgress(target);
    }
  };

  window.requestAnimationFrame(animate);
})();
