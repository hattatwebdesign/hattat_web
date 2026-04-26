  // Cookie Consent Banner
  (function() {
    const banner = document.getElementById("cookie-banner");
    const acceptBtn = document.getElementById("cookie-accept");
    const declineBtn = document.getElementById("cookie-decline");

    // Prüfen ob bereits entschieden wurde
    const consentGiven = localStorage.getItem("cookieConsent");

    if (!consentGiven) {
      banner.classList.add("show");
    }

    acceptBtn.addEventListener("click", () => {
      localStorage.setItem("cookieConsent", "accepted");
      banner.classList.remove("show");
      // Hier kannst du z. B. nicht-notwendige Scripts nachladen
      // z. B. Google Maps, Analytics etc.
    });

    declineBtn.addEventListener("click", () => {
      localStorage.setItem("cookieConsent", "declined");
      banner.classList.remove("show");
      // Keine nachträglichen Cookies setzen
    });
  })();
