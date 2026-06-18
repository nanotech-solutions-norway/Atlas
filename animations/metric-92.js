class AtlasMetric92 extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.target = 92;
    this.duration = 2800;
    this._frame = null;
    this._observer = null;
    this._hasAnimated = false;
  }

  connectedCallback() {
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
          width: 100%;
          height: 100%;
          min-width: 120px;
          min-height: 120px;
          contain: content;
        }

        .atlas-metric {
          width: 100%;
          height: 100%;
          min-height: 120px;
          display: grid;
          place-items: center;
          background: #000000;
          overflow: hidden;
          font-family: "Roboto Slab", Roboto, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        .metric-visual {
          position: relative;
          width: min(100%, 420px);
          aspect-ratio: 1 / 1;
          display: grid;
          place-items: center;
        }

        svg {
          width: 100%;
          height: 100%;
          overflow: visible;
          transform: rotate(-90deg);
        }

        .track,
        .progress {
          fill: none;
          stroke-width: 58;
          stroke-linecap: butt;
        }

        .track {
          stroke: #e6eaf2;
        }

        .progress {
          stroke: #385bb8;
          stroke-dasharray: 100;
          stroke-dashoffset: 100;
          transition: stroke-dashoffset 90ms ease-out;
        }

        .label {
          position: absolute;
          inset: 0;
          display: flex;
          align-items: center;
          justify-content: center;
          color: #152243;
          font-weight: 700;
          letter-spacing: -0.065em;
          line-height: 1;
          white-space: nowrap;
          transform: translateY(-1px);
        }

        .number {
          font-size: clamp(46px, 18vw, 128px);
        }

        .suffix {
          margin-left: 0.02em;
          font-size: clamp(32px, 12vw, 82px);
        }

        @media (max-width: 480px) {
          .metric-visual {
            width: min(100%, 280px);
          }

          .track,
          .progress {
            stroke-width: 46;
          }

          .number {
            font-size: clamp(42px, 20vw, 92px);
          }

          .suffix {
            font-size: clamp(28px, 13vw, 62px);
          }
        }

        @media (prefers-reduced-motion: reduce) {
          .progress {
            transition: none;
          }
        }
      </style>

      <div class="atlas-metric" role="img" aria-label="92 percent circular progress animation">
        <div class="metric-visual">
          <svg viewBox="0 0 600 600" aria-hidden="true">
            <circle class="track" cx="300" cy="300" r="250" pathLength="100"></circle>
            <circle class="progress" cx="300" cy="300" r="250" pathLength="100"></circle>
          </svg>
          <div class="label" aria-live="polite">
            <span class="number">0</span><span class="suffix">%</span>
          </div>
        </div>
      </div>
    `;

    this.progressCircle = this.shadowRoot.querySelector('.progress');
    this.numberNode = this.shadowRoot.querySelector('.number');
    this.wrapper = this.shadowRoot.querySelector('.atlas-metric');
    this._startWhenVisible();
  }

  disconnectedCallback() {
    if (this._frame) cancelAnimationFrame(this._frame);
    if (this._observer) this._observer.disconnect();
  }

  _startWhenVisible() {
    if (!('IntersectionObserver' in window)) {
      this._animate();
      return;
    }

    this._observer = new IntersectionObserver((entries) => {
      const entry = entries[0];
      if (entry.isIntersecting && !this._hasAnimated) {
        this._hasAnimated = true;
        this._observer.disconnect();
        this._animate();
      }
    }, { threshold: 0.25 });

    this._observer.observe(this);
  }

  _clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  _easeOutQuint(t) {
    return 1 - Math.pow(1 - t, 5);
  }

  _setValue(rawValue) {
    const value = this._clamp(rawValue, 0, 100);
    const rounded = Math.round(value);

    if (this.progressCircle) {
      this.progressCircle.style.strokeDashoffset = String(100 - value);
    }

    if (this.numberNode) {
      this.numberNode.textContent = String(rounded);
    }

    if (this.wrapper) {
      this.wrapper.setAttribute('aria-label', `${rounded} percent circular progress animation`);
    }
  }

  _animate() {
    const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (reduceMotion) {
      this._setValue(this.target);
      return;
    }

    const duration = Math.min(this.duration, 3000);
    let startTime = null;
    this._setValue(0);

    const step = (timestamp) => {
      if (startTime === null) startTime = timestamp;
      const elapsed = timestamp - startTime;
      const progress = this._clamp(elapsed / duration, 0, 1);
      const current = this.target * this._easeOutQuint(progress);

      this._setValue(current);

      if (progress < 1) {
        this._frame = requestAnimationFrame(step);
      } else {
        this._setValue(this.target);
      }
    };

    this._frame = requestAnimationFrame(step);
  }
}

if (!customElements.get('atlas-metric-92')) {
  customElements.define('atlas-metric-92', AtlasMetric92);
}
