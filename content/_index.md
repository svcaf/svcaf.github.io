---
title: "Home"
---

<div class="hero-carousel" id="heroCarousel">
  <div class="slide active"><img src="/images/slide-17.jpg" alt="SVCAF Community"></div>
  <div class="slide"><img src="/images/slide-16.jpg" alt="SVCAF Event"></div>
  <div class="slide"><img src="/images/slide-15.jpg" alt="SVCAF Community"></div>
  <div class="slide"><img src="/images/slide-14.jpg" alt="SVCAF Event"></div>
  <div class="slide"><img src="/images/slide-13.jpg" alt="SVCAF Community"></div>
  <button class="carousel-btn prev" onclick="carouselMove(-1)" aria-label="Previous">&#8249;</button>
  <button class="carousel-btn next" onclick="carouselMove(1)" aria-label="Next">&#8250;</button>
  <div class="carousel-dots" id="carouselDots"></div>
</div>

<script>
(function() {
  var slides = document.querySelectorAll('#heroCarousel .slide');
  var dotsEl = document.getElementById('carouselDots');
  var current = 0;
  var timer;

  slides.forEach(function(_, i) {
    var d = document.createElement('button');
    d.className = 'dot' + (i === 0 ? ' active' : '');
    d.setAttribute('aria-label', 'Slide ' + (i + 1));
    d.addEventListener('click', function() { goTo(i); resetTimer(); });
    dotsEl.appendChild(d);
  });

  function goTo(n) {
    slides[current].classList.remove('active');
    dotsEl.children[current].classList.remove('active');
    current = (n + slides.length) % slides.length;
    slides[current].classList.add('active');
    dotsEl.children[current].classList.add('active');
  }

  window.carouselMove = function(dir) { goTo(current + dir); resetTimer(); };

  function resetTimer() {
    clearInterval(timer);
    timer = setInterval(function() { goTo(current + 1); }, 5000);
  }

  resetTimer();
})();
</script>

## Empowering Chinese Americans

**Silicon Valley Chinese Association Foundation** (SVCAF) is a 501(c)(3) nonprofit dedicated to empowering Chinese Americans through education, civic engagement, and community action since 2015.
