document.addEventListener("DOMContentLoaded", () => {
  // Modal Elements
  const modalOverlay = document.getElementById("leadModal");
  const modalClose = document.getElementById("modalClose");
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

      // WhatsApp message encoding
      const text = `Hi Virtual Office Space USA!%0A%0A*New Lead Request*%0A*Name:* ${encodeURIComponent(name)}%0A*Email:* ${encodeURIComponent(email)}%0A*Phone:* ${encodeURIComponent(phone)}%0A*Preferred State:* ${encodeURIComponent(state)}%0A*Service:* ${encodeURIComponent(service)}%0A%0APlease share available addresses and onboarding details.`;
      
      const whatsappUrl = `https://api.whatsapp.com/send?phone=919244240917&text=${text}`;

      // Close modal
      modalOverlay.classList.remove("active");

      // Redirect to WhatsApp
      window.open(whatsappUrl, "_blank");

      leadForm.reset();
    });
  }

  // FAQ Accordion
  document.querySelectorAll(".faq-question").forEach(qBtn => {
    qBtn.addEventListener("click", () => {
      const answer = qBtn.nextElementSibling;
      const isOpen = answer.style.display === "block";

      // Close others
      document.querySelectorAll(".faq-answer").forEach(ans => ans.style.display = "none");
      document.querySelectorAll(".faq-question span.arrow").forEach(arr => arr.textContent = "+");

      if (!isOpen) {
        answer.style.display = "block";
        qBtn.querySelector("span.arrow").textContent = "−";
      }
    });
  });
});
