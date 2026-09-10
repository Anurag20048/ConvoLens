// ConvoLens Theme Toggle

// API bridge: GitHub Pages is static, so connected features call the public Django API.
// Override window.CONVOLENS_API_BASE before this script for local development or another backend.
const CONVOLENS_API_BASE = window.CONVOLENS_API_BASE || "https://convolens-api.onrender.com";
const originalFetch = window.fetch.bind(window);

window.fetch = (input, init) => {
  const url = typeof input === "string" ? input : input?.url;
  if (!url) return originalFetch(input, init);

  if (url === "http://localhost:5005/webhooks/rest/webhook") {
    return originalFetch(`${CONVOLENS_API_BASE}/api/chat/`, init);
  }

  if (url === "http://127.0.0.1:8000/api/feedback/") {
    return originalFetch(`${CONVOLENS_API_BASE}/api/feedback/`, init);
  }

  return originalFetch(input, init);
};

document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const toggleBtn = document.getElementById("theme-toggle");
  const icon = toggleBtn ? toggleBtn.querySelector("i") : null;

  body.style.transition = "background-color 0.3s, color 0.3s";
  const savedTheme = localStorage.getItem("theme") || "light";
  body.classList.remove("light-mode", "dark-mode");
  body.classList.add(savedTheme + "-mode");

  if (icon) {
    if (savedTheme === "dark") icon.classList.replace("bi-moon-fill", "bi-sun-fill");
    else icon.classList.replace("bi-sun-fill", "bi-moon-fill");
  }

  toggleBtn?.addEventListener("click", () => {
    body.classList.toggle("dark-mode");
    body.classList.toggle("light-mode");
    if (body.classList.contains("dark-mode")) {
      if (icon) icon.classList.replace("bi-moon-fill", "bi-sun-fill");
      localStorage.setItem("theme", "dark");
    } else {
      if (icon) icon.classList.replace("bi-sun-fill", "bi-moon-fill");
      localStorage.setItem("theme", "light");
    }
  });
});
