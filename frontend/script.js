// ConvoLens Theme Toggle

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
