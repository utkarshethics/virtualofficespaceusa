document.addEventListener("DOMContentLoaded", () => {
  // Modal Elements
  const modalOverlay = document.getElementById("leadModal");
  const modalClose = document.getElementById("modalClose");
  const modalTitle = document.getElementById("modalTitle");
  const serviceSelect = document.getElementById("leadService");
  const leadForm = document.getElementById("leadForm");
  const successBox = document.getElementById("leadSuccessMsg");

  // Dual-Tab Switcher
  const tabButtons = document.querySelectorAll(".modal-tabs .tab-btn");
  const tabContents = document.querySelectorAll(".modal .tab-content");

  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      tabButtons.forEach(b => b.classList.remove("active"));
      tabContents.forEach(c => c.classList.remove("active"));
      btn.classList.add("active");
      const target = document.getElementById(btn.getAttribute("data-tab"));
      if (target) target.classList.add("active");
    });
  });

  // Open Modal function
  window.openLeadModal = function(intent, state) {
    if (leadForm) leadForm.style.display = "block";
    if (successBox) successBox.style.display = "none";
    if (modalTitle && intent) {
      modalTitle.textContent = intent.startsWith("Order") ? intent : "Get Your US Virtual Office";
    }
    const stateSelect = document.getElementById("leadState");
    if (stateSelect && state) {
      stateSelect.value = state;
    } else if (serviceSelect && state) {
      serviceSelect.value = state;
    }
    if (modalOverlay) {
      modalOverlay.classList.add("active");
    }
  };

  // Close Modal
  if (modalClose) {
    modalClose.addEventListener("click", () => {
      modalOverlay.classList.remove("active");
    });
  }

  if (modalOverlay) {
    modalOverlay.addEventListener("click", (e) => {
      if (e.target === modalOverlay) {
        modalOverlay.classList.remove("active");
      }
    });
  }

  // Frictionless Inquiry Submission
  if (leadForm) {
    leadForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const email = document.getElementById("leadEmail")?.value || "";
      const state = document.getElementById("leadState")?.value || "";

      try {
        const stored = JSON.parse(localStorage.getItem("vos_inquiries") || "[]");
        stored.push({ email, state, date: new Date().toISOString() });
        localStorage.setItem("vos_inquiries", JSON.stringify(stored));
      } catch (err) {
        console.warn(err);
      }

      leadForm.style.display = "none";
      if (successBox) successBox.style.display = "block";
      leadForm.reset();
    });
  }

  // Open the FAQ answer targeted by a #faq-... link (footer / search deep links)
  const openFaqFromHash = () => {
    const item = location.hash && document.getElementById(location.hash.slice(1));
    if (item && item.classList.contains("faq-item")) {
      const btn = item.querySelector(".faq-question");
      if (btn && btn.getAttribute("aria-expanded") !== "true") btn.click();
    }
  };
  window.addEventListener("hashchange", openFaqFromHash);

  // FAQ Accordion
  document.querySelectorAll(".faq-question").forEach(qBtn => {
    qBtn.addEventListener("click", () => {
      const answer = qBtn.nextElementSibling;
      const isOpen = answer.style.display === "block";

      // Close all other answers
      document.querySelectorAll(".faq-answer").forEach(ans => {
        ans.style.display = "none";
      });
      document.querySelectorAll(".faq-question").forEach(b => {
        b.setAttribute("aria-expanded", "false");
      });

      if (!isOpen) {
        answer.style.display = "block";
        qBtn.setAttribute("aria-expanded", "true");
      }
    });
  });

  // Open initial FAQ if URL has a hash matching an item
  openFaqFromHash();
}); document.getElementById("modalClose");
  const modalTitle = document.getElementById("modalTitle");
  const serviceSelect = document.getElementById("leadService");
  const leadForm = document.getElementById("leadForm");

  // Open Modal function
  window.openLeadModal = function(intent, preselectService) {
    if (modalTitle && intent) {
      modalTitle.textContent = intent.startsWith("Order") ? intent : "Get Your US Virtual Office";
    }
    if (serviceSelect && preselectService) {
      serviceSelect.value = preselectService;
    }
    if (modalOverlay) {
      modalOverlay.classList.add("active");
    }
  };

  // Close Modal
  if (modalClose) {
    modalClose.addEventListener("click", () => {
      modalOverlay.classList.remove("active");
    });
  }

  if (modalOverlay) {
    modalOverlay.addEventListener("click", (e) => {
      if (e.target === modalOverlay) {
        modalOverlay.classList.remove("active");
      }
    });
  }

  // Trigger buttons
  document.querySelectorAll(".open-lead-btn").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const intent = btn.getAttribute("data-intent") || "US Virtual Office Inquiry";
      const service = btn.getAttribute("data-service") || "Business Pro Plan";
      window.openLeadModal(intent, service);
    });
  });

  // Lead Form Submit
  if (leadForm) {
    leadForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const name = document.getElementById("leadName").value.trim();
      const email = document.getElementById("leadEmail").value.trim();
      const phone = document.getElementById("leadPhone").value.trim();
      const state = document.getElementById("leadState").value;
      const service = document.getElementById("leadService").value;

      const leadData = {
        name,
        email,
        phone,
        state,
        service,
        date: new Date().toISOString(),
        domain: "virtualofficespaceusa.online"
      };

      // Save locally
      try {
        const stored = JSON.parse(localStorage.getItem("vos_usa_leads") || "[]");
        stored.push(leadData);
        localStorage.setItem("vos_usa_leads", JSON.stringify(stored));
      } catch (err) {
        console.warn("Storage error", err);
      }

      // Whatsdocument.addEventListener("DOMContentLoaded", () => {
  // Modal Elements
  const modalOverlay = document.getElementById("leadModal");
  const modalClose = document.getElementById("modalClose");
  const modalTitle = document.getElementById("modalTitle");
  const serviceSelect = document.getElementById("leadService");
  const leadForm = document.getElementById("leadForm");
  const successBox = document.getElementById("leadSuccessMsg");

  // Dual-Tab Switcher
  const tabButtons = document.querySelectorAll(".modal-tabs .tab-btn");
  const tabContents = document.querySelectorAll(".modal .tab-content");

  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      tabButtons.forEach(b => b.classList.remove("active"));
      tabContents.forEach(c => c.classList.remove("active"));
      btn.classList.add("active");
      const target = document.getElementById(btn.getAttribute("data-tab"));
      if (target) target.classList.add("active");
    });
  });

  // Open Modal function
  window.openLeadModal = function(intent, state) {
    if (leadForm) leadForm.style.display = "block";
    if (successBox) successBox.style.display = "none";
    if (modalTitle && intent) {
      modalTitle.textContent = intent.startsWith("Order") ? intent : "Get Your US Virtual Office";
    }
    const stateSelect = document.getElementById("leadState");
    if (stateSelect && state) {
      stateSelect.value = state;
    } else if (serviceSelect && state) {
      serviceSelect.value = state;
    }
    if (modalOverlay) {
      modalOverlay.classList.add("active");
    }
  };

  // Close Modal
  if (modalClose) {
    modalClose.addEventListener("click", () => {
      modalOverlay.classList.remove("active");
    });
  }

  if (modalOverlay) {
    modalOverlay.addEventListener("click", (e) => {
      if (e.target === modalOverlay) {
        modalOverlay.classList.remove("active");
      }
    });
  }

  // Frictionless Inquiry Submission
  if (leadForm) {
    leadForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const email = document.getElementById("leadEmail")?.value || "";
      const state = document.getElementById("leadState")?.value || "";

      try {
        const stored = JSON.parse(localStorage.getItem("vos_inquiries") || "[]");
        stored.push({ email, state, date: new Date().toISOString() });
        localStorage.setItem("vos_inquiries", JSON.stringify(stored));
      } catch (err) {
        console.warn(err);
      }

      leadForm.style.display = "none";
      if (successBox) successBox.style.display = "block";
      leadForm.reset();
    });
  }

  // Open the FAQ answer targeted by a #faq-... link (footer / search deep links)
  const openFaqFromHash = () => {
    const item = location.hash && document.getElementById(location.hash.slice(1));
    if (item && item.classList.contains("faq-item")) {
      const btn = item.querySelector(".faq-question");
      if (btn && btn.getAttribute("aria-expanded") !== "true") btn.click();
    }
  };
  window.addEventListener("hashchange", openFaqFromHash);

  // FAQ Accordion
  document.querySelectorAll(".faq-question").forEach(qBtn => {
    qBtn.addEventListener("click", () => {
      const answer = qBtn.nextElementSibling;
      const isOpen = answer.style.display === "block";

      // Close all other answers
      document.querySelectorAll(".faq-answer").forEach(ans => {
        ans.style.display = "none";
      });
      document.querySelectorAll(".faq-question").forEach(b => {
        b.setAttribute("aria-expanded", "false");
      });

      if (!isOpen) {
        answer.style.display = "block";
        qBtn.setAttribute("aria-expanded", "true");
      }
    });
  });

  // Open initial FAQ if URL has a hash matching an item
  openFaqFromHash();
});App message encoding
      const text = `Hi Virtual Office Space USA!%0A%0A*New Lead Request*%0A*Name:* ${encodeURIComponent(name)}%0A*Email:* ${encodeURIComponent(email)}%0A*Phone:* ${encodeURIComponent(phone)}%0A*Preferred State:* ${encodeURIComponent(state)}%0A*Service:* ${encodeURIComponent(service)}%0A%0APlease share available addresses and onboarding details.`;
      
      const whatsappUrl = `https://api.whatsapp.com/send?phone=919244240917&text=${text}`;

      // Close modal
      modalOverlay.classList.remove("active");

      // Redirect to WhatsApp
      window.open(whatsappUrl, "_blank");

      leadForm.reset();
    });
  }

  // Open the FAQ answer targeted by a #faq-... link (footer / search deep links)
  const openFaqFromHash = () => {
    const item = location.hash && document.getElementById(location.hash.slice(1));
    if (item && item.classList.contains("faq-item")) {
      const btn = item.querySelector(".faq-question");
      if (btn && btn.getAttribute("aria-expanded") !== "true") btn.click();
    }
  };
  window.addEventListener("hashchange", openFaqFromHash);

  // FAQ Accordion
  document.querySelectorAll(".faq-question").forEach(qBtn => {
    qBtn.addEventListener("click", () => {
      const answer = qBtn.nextElementSibling;
      const isOpen = answer.style.display === "block";

      // Close others
      document.querySelectorAll(".faq-answer").forEach(ans => ans.style.display = "none");
      document.querySelectorAll(".faq-question span.arrow").forEach(arr => arr.textContent = "+");
      document.querySelectorAll(".faq-question").forEach(b => b.setAttribute("aria-expanded", "false"));

      if (!isOpen) {
        answer.style.display = "block";
        qBtn.querySelector("span.arrow").textContent = "−";
        qBtn.setAttribute("aria-expanded", "true");
      }
    });
  });

  openFaqFromHash();
});
