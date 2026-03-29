---
title: "Home"
date: 2026-03-15T21:49:01
slug: home-2
type: page
---

.svcaf-slideshow-hero {
  position: relative;
  width: 100%;
  display: flex;
  flex-direction: column;
  background: #0d1b2a;
  overflow: hidden;
}
.svcaf-hero-top {
  background: #0d1b2a;
  padding: 28px 20px 14px;
  text-align: center;
  z-index: 2;
}
.svcaf-hero-top h1 {
  color: #ffffff;
  font-size: 1.9rem;
  font-weight: 700;
  margin: 0 0 6px;
  line-height: 1.2;
}
.svcaf-hero-top p {
  color: #b0bec5;
  font-size: 1rem;
  margin: 0;
  line-height: 1.4;
}
.svcaf-hero-slides {
  position: relative;
  width: 100%;
  aspect-ratio: 17/6;
  flex-shrink: 0;
}
.svcaf-hero-slides .slide {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  opacity: 0;
  transition: opacity 1.5s ease-in-out;
}
.svcaf-hero-slides .slide.active { opacity: 1; }
.svcaf-hero-slides .slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center center;
}
.svcaf-hero-bottom {
  background: #0d1b2a;
  padding: 14px 20px 18px;
  text-align: center;
  z-index: 2;
}
.svcaf-hero-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}
.svcaf-hero-buttons a {
  display: inline-block;
  padding: 10px 28px;
  border-radius: 4px;
  font-size: 0.95rem;
  font-weight: 600;
  text-decoration: none;
  transition: opacity 0.2s;
}
.svcaf-hero-buttons a:hover { opacity: 0.85; }
.svcaf-hero-buttons .btn-primary {
  background: #ffffff;
  color: #0d1b2a;
}
.svcaf-hero-buttons .btn-secondary {
  background: transparent;
  color: #ffffff;
  border: 2px solid #ffffff;
}
.svcaf-slide-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 10px;
}
.svcaf-slide-dots span {
  width: 8px; height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,0.3);
  cursor: pointer;
  transition: background 0.3s;
}
.svcaf-slide-dots span.active { background: #ffffff; }

@media (min-width: 769px) {
  .svcaf-hero-top h1 { font-size: 2.4rem; }
  .svcaf-hero-top p { font-size: 1.15rem; }
  .svcaf-hero-top { padding: 36px 40px 18px; }
  .svcaf-hero-bottom { padding: 18px 40px 24px; }
}

  
    # Silicon Valley Chinese Association Foundation
    Empowering Chinese Americans through education, civic engagement, and community action since 2015

  
  
  
    
      ![](/wp-content/uploads/2026/03/svcaf-slide-17-1.jpg)
    
    
      ![](/wp-content/uploads/2026/03/svcaf-slide-15-1.jpg)
    
    
      ![](/wp-content/uploads/2026/03/svcaf-slide-14-1.jpg)
    
    
      ![](/wp-content/uploads/2026/03/svcaf-slide-13-1.jpg)
    
    
      ![](/wp-content/uploads/2026/03/svcaf-slide-16-1.jpg)
    
  
  
  
    
      [Our Programs](/education/)
      [Donate](/donations/)
    
    
      
      
      
      
      
    
  

(function() {
  var c = 0;
  var s = document.querySelectorAll('.svcaf-hero-slides .slide');
  var d = document.querySelectorAll('.svcaf-slide-dots span');
  var t = s.length;
  window.svcafSlide = function(n) {
    s[c].classList.remove('active');
    d[c].classList.remove('active');
    c = n;
    s[c].classList.add('active');
    d[c].classList.add('active');
  };
  setInterval(function() { window.svcafSlide((c + 1) % t); }, 4000);
})();

## What We Do

### 🎓

### [Education & Advocacy](/education/)

Fighting for educational equity — from the Harvard admissions case to local school board advocacy. We filed amicus briefs and mobilized communities for fair admissions policies.

[Learn More →](/education/)

### 🏛️

### [Civic Engagement](/about-us/)

Promoting active participation in public affairs. From voter education to community forums with elected officials, we bridge the gap between Chinese Americans and civic life.

[Learn More →](/about-us/)

### 🤖

### [AI4Legislation](/posts/call-for-volunteers-for-ai4legislation-using-ai-to-enhance-civic-awareness-and-action/)

Our innovative program using AI to analyze legislation and empower informed civic participation. Seminars, student competitions, and tools for community advocacy.

[Learn More →](/posts/call-for-volunteers-for-ai4legislation-using-ai-to-enhance-civic-awareness-and-action/)

## Latest News

- [OpenClaw Seminar: AI Workflows for Civic Engagement — Tony Guan | April 4, 2026](/posts/openclaw-seminar-ai-workflows-for-civic-engagement-tony-guan-april-4-2026/)March 21, 2026
- [SVCAF OpenClaw Seminar Recap: AI Agents, Automation & What’s Possible](/posts/svcaf-openclaw-seminar-recap-ai-agents-automation-whats-possible/)March 7, 2026
- [Forum: What Should You Do If UC Turned You Down? — April 5, 2026](/posts/forum-what-should-you-do-if-uc-turned-you-down-april-5-2026/)March 6, 2026

[View All News →](/categories/svcaf/)

## Support Our Mission

SVCAF is a 501(c)(3) nonprofit. Your tax-deductible donation directly supports education advocacy, civic engagement programs, and community empowerment for Chinese Americans in Silicon Valley and beyond.

[Donate Now](/donate/)