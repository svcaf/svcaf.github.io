---
title: "Photo Gallery"
description: "A visual journey through SVCAF's community events, advocacy programs, and milestones since 2015."
---

<p class="gallery-intro">Explore highlights from SVCAF's community events, advocacy work, annual galas, and youth programs across the years.</p>

<div class="gallery-section">
<h2>🏛️ Advocacy &amp; Civic Engagement</h2>
<div class="gallery-grid">

<div class="gallery-item" onclick="openLightbox(0)">
<img src="/images/slide-22.jpg" loading="lazy" alt="Rally at U.S. Supreme Court">
<div class="gallery-caption-overlay">U.S. Supreme Court Rally, 2022</div>
</div>

<div class="gallery-item" onclick="openLightbox(1)">
<img src="/images/slide-23.jpg" loading="lazy" alt="Calligraphy Banner Presentation">
<div class="gallery-caption-overlay">Presenting SVCAF Calligraphy Banner, 2017</div>
</div>

<div class="gallery-item" onclick="openLightbox(2)">
<img src="/images/slide-16.jpg" loading="lazy" alt="PPE Donation to Frontline Workers">
<div class="gallery-caption-overlay">PPE Donation to USPS Carrier, 2020</div>
</div>

</div>
</div>

<div class="gallery-section">
<h2>🎓 Youth Programs &amp; Awards</h2>
<div class="gallery-grid">

<div class="gallery-item" onclick="openLightbox(3)">
<img src="/images/slide-13.jpg" loading="lazy" alt="California Youth Legislature Certificate">
<div class="gallery-caption-overlay">2019 California Youth Legislature Certificate, 2019</div>
</div>

<div class="gallery-item" onclick="openLightbox(4)">
<img src="/images/slide-14.jpg" loading="lazy" alt="Voice of Asian Americans Scholarship">
<div class="gallery-caption-overlay">Voice of Asian Americans Scholarship Award</div>
</div>

</div>
</div>

<div class="gallery-section">
<h2>🎉 Annual Galas</h2>
<div class="gallery-grid">

<div class="gallery-item" onclick="openLightbox(5)">
<img src="/images/slide-19.jpg" loading="lazy" alt="SVCAF Annual Gala 2017">
<div class="gallery-caption-overlay">SVCAF Annual Gala Group Photo, 2017</div>
</div>

<div class="gallery-item" onclick="openLightbox(6)">
<img src="/images/slide-20.jpg" loading="lazy" alt="Volunteers of the Year 2017">
<div class="gallery-caption-overlay">Volunteers of the Year Award, 2017</div>
</div>

<div class="gallery-item" onclick="openLightbox(7)">
<img src="/images/slide-23.jpg" loading="lazy" alt="Gala Civic Partnership">
<div class="gallery-caption-overlay">Civic Partnership Recognition, 2017</div>
</div>

</div>
</div>

<div class="gallery-section">
<h2>🤝 Community Gatherings</h2>
<div class="gallery-grid">

<div class="gallery-item" onclick="openLightbox(8)">
<img src="/images/slide-18.jpg" loading="lazy" alt="Community Gathering 2022">
<div class="gallery-caption-overlay">Community Gathering with SVCAF Banners, 2022</div>
</div>

<div class="gallery-item" onclick="openLightbox(9)">
<img src="/images/slide-17.jpg" loading="lazy" alt="SVCAF Outdoor Group Photo">
<div class="gallery-caption-overlay">SVCAF Members &amp; Leaders Outdoor Group Photo</div>
</div>

<div class="gallery-item" onclick="openLightbox(10)">
<img src="/images/slide-21.jpg" loading="lazy" alt="Board Outdoor Lunch 2023">
<div class="gallery-caption-overlay">Board &amp; Members Outdoor Gathering, 2023</div>
</div>

<div class="gallery-item" onclick="openLightbox(11)">
<img src="/images/slide-15.jpg" loading="lazy" alt="SVCAF Annual Meeting Group Photo">
<div class="gallery-caption-overlay">SVCAF Annual Meeting, Community Group Photo</div>
</div>

</div>
</div>

<!-- Lightbox -->
<div class="lightbox-overlay" id="lightbox">
  <button class="lightbox-close" onclick="closeLightbox()" aria-label="Close">&#x2715;</button>
  <button class="lightbox-nav prev" onclick="shiftLightbox(-1)" aria-label="Previous">&#8249;</button>
  <div class="lightbox-inner">
    <img id="lightbox-img" src="" alt="">
    <div class="lightbox-caption" id="lightbox-caption"></div>
    <div class="lightbox-counter" id="lightbox-counter"></div>
  </div>
  <button class="lightbox-nav next" onclick="shiftLightbox(1)" aria-label="Next">&#8250;</button>
</div>

<script>
var galleryPhotos = [
  { src: "/images/slide-22.jpg", caption: "SVCAF members and supporters rally at the U.S. Supreme Court in support of equal education rights and against race-based admissions discrimination, 2022." },
  { src: "/images/slide-23.jpg", caption: "SVCAF presents a hand-crafted calligraphy banner to a California state official at the 2017 Annual Gala, celebrating civic partnership and community recognition." },
  { src: "/images/slide-16.jpg", caption: "An SVCAF volunteer delivers PPE and care packages to a USPS mail carrier during the COVID-19 pandemic, 2020. SVCAF organized donations for frontline workers across Silicon Valley." },
  { src: "/images/slide-13.jpg", caption: "A student participant in SVCAF's 2019 California Youth Legislature program receives a Certificate of Recognition at a formal civic ceremony, honoring her leadership and public service." },
  { src: "/images/slide-14.jpg", caption: "Nathaniel Yu receives the SVCAF Voice of Asian Americans Scholarship — a $2,000 award recognizing outstanding academic achievement and commitment to the Chinese American community." },
  { src: "/images/slide-19.jpg", caption: "Board members, sponsors, and community leaders gather for a group photo at the SVCAF Annual Gala, February 2017, at an elegant Silicon Valley venue." },
  { src: "/images/slide-20.jpg", caption: "SVCAF honors its Volunteers of the Year at the 2017 Annual Gala, presenting awards and orchids to members who gave exceptional service to the community." },
  { src: "/images/slide-23.jpg", caption: "SVCAF leaders present a traditional Chinese calligraphy artwork to a state official at the 2017 Gala, symbolizing SVCAF's commitment to civic engagement and cross-cultural partnership." },
  { src: "/images/slide-18.jpg", caption: "More than 40 SVCAF members and community supporters gather for a group photo at a 2022 community event, with SVCAF banners proudly displayed." },
  { src: "/images/slide-17.jpg", caption: "SVCAF members and organizational leaders pose for a group photo outside a community event venue, celebrating another year of civic service and community building." },
  { src: "/images/slide-21.jpg", caption: "SVCAF board members and community partners enjoy an outdoor gathering in 2023, reflecting the warm bonds built through years of shared mission and service." },
  { src: "/images/slide-15.jpg", caption: "SVCAF members, volunteers, community leaders, and their families gather on stage for a group photo at an annual meeting, celebrating the strength and unity of Silicon Valley's Chinese American community." }
];

var currentIndex = 0;

function openLightbox(index) {
  currentIndex = index;
  updateLightbox();
  document.getElementById('lightbox').classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('active');
  document.body.style.overflow = '';
}

function shiftLightbox(dir) {
  currentIndex = (currentIndex + dir + galleryPhotos.length) % galleryPhotos.length;
  updateLightbox();
}

function updateLightbox() {
  var photo = galleryPhotos[currentIndex];
  document.getElementById('lightbox-img').src = photo.src;
  document.getElementById('lightbox-img').alt = photo.caption;
  document.getElementById('lightbox-caption').textContent = photo.caption;
  document.getElementById('lightbox-counter').textContent = (currentIndex + 1) + ' / ' + galleryPhotos.length;
}

document.getElementById('lightbox').addEventListener('click', function(e) {
  if (e.target === this) closeLightbox();
});

document.addEventListener('keydown', function(e) {
  var lb = document.getElementById('lightbox');
  if (!lb.classList.contains('active')) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') shiftLightbox(-1);
  if (e.key === 'ArrowRight') shiftLightbox(1);
});
</script>
