"use strict";
(function () {
  var toggle = document.getElementById("navToggle");
  var links = document.getElementById("navLinks");
  function setOpen(open) {
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    links.hidden = !open;
  }
  function syncForViewport() {
    if (window.matchMedia("(max-width: 860px)").matches) {
      if (toggle.getAttribute("aria-expanded") !== "true") links.hidden = true;
    } else {
      links.hidden = false;
    }
  }
  toggle.addEventListener("click", function () {
    setOpen(toggle.getAttribute("aria-expanded") !== "true");
  });
  links.addEventListener("click", function (e) {
    if (e.target.closest("a") && window.matchMedia("(max-width: 860px)").matches) setOpen(false);
  });
  window.addEventListener("resize", syncForViewport);
  syncForViewport();
})();

document.getElementById("year").textContent = new Date().getFullYear();

(function () {
  var form = document.getElementById("bookForm");
  var ok = document.getElementById("formOk");
  var OFFICE_EMAIL = "office@gsaccounting.com";
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var name = form.name.value.trim();
    var email = form.email.value.trim();
    if (!name || !email) {
      (name ? form.email : form.name).focus();
      return;
    }
    var body =
      "Name: " + name + "\n" +
      "Email: " + email + "\n" +
      "Phone: " + form.phone.value.trim() + "\n" +
      "Needs help with: " + form.help.value + "\n\n" +
      (form.message.value.trim() || "(no additional details)");
    var href = "mailto:" + OFFICE_EMAIL +
      "?subject=" + encodeURIComponent("Consultation request — " + name) +
      "&body=" + encodeURIComponent(body);
    ok.hidden = false;
    window.location.href = href;
  });
})();
