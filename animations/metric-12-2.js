(() => {
  const TAG_NAME = 'atlas-metric-12-2';
  if (customElements.get(TAG_NAME)) return;

  class AtlasMetric12_2 extends HTMLElement {
    constructor() {
      super();
      this.attachShadow({ mode: 'open' });
      this.target = 12.2;
      this.decimalPlaces = 1;
      this.duration = 2800;
      this.revealThreshold = 0.35;
      this._frame = null;
      this._observer = null;
      this._hasAnimated = false;
      this._fallbackRevealHandler = null;
    }

    connectedCallback() {
      this.shadowRoot.innerHTML = `
        <style>
          @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap');

          :host {
            display: block;
            width: 100%;
            height: 100%;
            min-width: 90px;
            min-height: 70px;
            contain: content;
            background: transparent !important;
          }

          .atlas-metric {
            width: 100%;
            height: 100%;
            min-height: 70px;
            display: grid;
            place-items: center;
            background: transparent !important;
            overflow: hidden;
            font-family: Inter, Roboto, Arial, sans-serif !important;
          }

          .label,
          .number,
          .suffix {
            font-family: Inter, Roboto, Arial, sans-serif !important;
            font-size: 64px !important;
            font-weight: 400 !important;
            font-style: normal !important;
            font-variation-settings: 'wght' 400 !important;
            letter-spacing: 0 !important;
            line-height: 1 !important;
            text-rendering: geometricPrecision;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
          }

          .label {
            display: flex;
            align-items: center;
            justify-content: center;
            color: #152243;
            white-space: nowrap;
            transform: translateY(-1px);
          }

          .suffix { margin-left: 0.04em; }
        </style>

        <div class="atlas-metric" role="img" aria-label="0 percent text count animation with transparent background">
          <div class="label" aria-live="polite">
            <span class="number">0.0</span><span class="suffix">%</span>
          </div>
        </div>
      `;

      this.numberNode = this.shadowRoot.querySelector('.number');
      this.wrapper = this.shadowRoot.querySelector('.atlas-metric');
      this._setValue(0);
      this._startWhenRevealed();
    }

    disconnectedCallback() {
      if (this._frame) cancelAnimationFrame(this._frame);
      if (this._observer) this._observer.disconnect();
      if (this._fallbackRevealHandler) {
        window.removeEventListener('scroll', this._fallbackRevealHandler, true);
        window.removeEventListener('resize', this._fallbackRevealHandler, true);
      }
    }

    _startWhenRevealed() {
      if (this._hasAnimated) return;
      if ('IntersectionObserver' in window) {
        this._observer = new IntersectionObserver((entries) => {
          const entry = entries[0];
          if (entry.isIntersecting && entry.intersectionRatio >= this.revealThreshold) this._runOnce();
        }, {
          threshold: [0, 0.1, 0.25, this.revealThreshold, 0.5, 0.75, 1],
          root: null,
          rootMargin: '0px 0px -8% 0px'
        });
        this._observer.observe(this);
        return;
      }
      this._fallbackRevealHandler = () => { if (this._isElementRevealed()) this._runOnce(); };
      window.addEventListener('scroll', this._fallbackRevealHandler, true);
      window.addEventListener('resize', this._fallbackRevealHandler, true);
      this._fallbackRevealHandler();
    }

    _isElementRevealed() {
      const rect = this.getBoundingClientRect();
      const vh = window.innerHeight || document.documentElement.clientHeight;
      const vw = window.innerWidth || document.documentElement.clientWidth;
      const visibleWidth = Math.max(0, Math.min(rect.right, vw) - Math.max(rect.left, 0));
      const visibleHeight = Math.max(0, Math.min(rect.bottom, vh) - Math.max(rect.top, 0));
      return (visibleWidth * visibleHeight) / Math.max(rect.width * rect.height, 1) >= this.revealThreshold;
    }

    _runOnce() {
      if (this._hasAnimated) return;
      this._hasAnimated = true;
      if (this._observer) { this._observer.disconnect(); this._observer = null; }
      if (this._fallbackRevealHandler) {
        window.removeEventListener('scroll', this._fallbackRevealHandler, true);
        window.removeEventListener('resize', this._fallbackRevealHandler, true);
        this._fallbackRevealHandler = null;
      }
      this._animate();
    }

    _clamp(value, min, max) { return Math.min(Math.max(value, min), max); }
    _easeOutQuint(t) { return 1 - Math.pow(1 - t, 5); }
    _formatValue(value) { return value.toFixed(this.decimalPlaces); }

    _setValue(rawValue) {
      const value = this._clamp(rawValue, 0, this.target);
      const display = this._formatValue(value);
      if (this.numberNode) this.numberNode.textContent = display;
      if (this.wrapper) this.wrapper.setAttribute('aria-label', `${display} percent text count animation with transparent background`);
    }

    _animate() {
      const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (reduceMotion) { this._setValue(this.target); return; }
      const duration = Math.min(this.duration, 3000);
      let startTime = null;
      this._setValue(0);
      const step = (timestamp) => {
        if (startTime === null) startTime = timestamp;
        const progress = this._clamp((timestamp - startTime) / duration, 0, 1);
        this._setValue(this.target * this._easeOutQuint(progress));
        if (progress < 1) this._frame = requestAnimationFrame(step);
        else this._setValue(this.target);
      };
      this._frame = requestAnimationFrame(step);
    }
  }

  customElements.define(TAG_NAME, AtlasMetric12_2);
})();
