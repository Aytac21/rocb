document.addEventListener("DOMContentLoaded", function () {
  console.log("Language switcher loaded");

  // Find all header containers instead of using IDs
  const headerContainers = document.querySelectorAll(".header-area");

  // Global current country state - shared across all headers
  let globalCurrentCountry = "uk";

  headerContainers.forEach((header, index) => {
    initializeLanguageSwitcher(header, index);
  });

  function initializeLanguageSwitcher(headerContainer, headerIndex) {
    const flagButton = headerContainer.querySelector(".flag");
    const dropdown = headerContainer.querySelector(".dropdown");
    const currentFlag = headerContainer.querySelector(
      '#currentFlag, [id*="currentFlag"]'
    );
    const dropdownItems = headerContainer.querySelectorAll(".dropdown-item");

    // Skip if elements not found
    if (!flagButton || !dropdown || !currentFlag || !dropdownItems.length) {
      console.warn(
        `Language switcher elements not found in header ${headerIndex}`
      );
      return;
    }

    // Toggle dropdown
    flagButton.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();

      const isOpen = dropdown.classList.contains("show");

      // Close all other dropdowns first
      closeAllDropdowns();

      if (!isOpen) {
        openDropdown();
      }
    });

    // Handle dropdown item clicks
    dropdownItems.forEach((item) => {
      item.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();

        const country = this.dataset.country;
        const langCode = this.dataset.lang;
        const flagSrc = this.dataset.flag;

        console.log("Selected country:", country, "Language:", langCode);

        if (country !== globalCurrentCountry) {
          // Update global state
          globalCurrentCountry = country;

          // Update all headers to show the same selection
          updateAllHeaders(country, flagSrc);

          // Show feedback
          showSelectionFeedback(langCode);

          // Switch language
          switchLanguage(langCode);
        }

        closeDropdown();
      });
    });

    function openDropdown() {
      flagButton.classList.add("active");
      dropdown.classList.add("show");
      updateSelectedState();
    }

    function closeDropdown() {
      flagButton.classList.remove("active");
      dropdown.classList.remove("show");
    }

    function updateSelectedState() {
      dropdownItems.forEach((item) => {
        if (item.dataset.country === globalCurrentCountry) {
          item.classList.add("selected");
        } else {
          item.classList.remove("selected");
        }
      });
    }

    // Initialize this header
    setActiveLanguageButton();
    updateSelectedState();

    // Store references for global access
    headerContainer._languageSwitcher = {
      flagButton,
      dropdown,
      currentFlag,
      dropdownItems,
      closeDropdown,
      updateSelectedState,
    };
  }

  // Global functions
  function closeAllDropdowns() {
    headerContainers.forEach((header) => {
      const switcher = header._languageSwitcher;
      if (switcher) {
        switcher.closeDropdown();
      }
    });
  }

  function updateAllHeaders(country, flagSrc) {
    // Update global state
    globalCurrentCountry = country;

    headerContainers.forEach((header) => {
      const switcher = header._languageSwitcher;
      if (switcher) {
        switcher.currentFlag.src = flagSrc;
        switcher.updateSelectedState();
      }
    });
  }

  function showSelectionFeedback(langCode) {
    const languageName = langCode === "en" ? "English" : "Русский";
    console.log(`Language changed to ${languageName}`);
  }

  // Updated language switching function
  function switchLanguage(langCode) {
    console.log("Switching to language:", langCode);

    // Get CSRF token
    let csrfValue = getCsrfToken();

    if (!csrfValue) {
      console.warn("CSRF token not found, using simple redirect");
      redirectWithLanguage(langCode);
      return;
    }

    console.log("CSRF token found:", csrfValue ? "Yes" : "No");

    // Calculate new path
    const newPath = calculateNewPath(langCode);
    console.log("New path will be:", newPath);

    // Create and submit form
    const form = document.createElement("form");
    form.method = "POST";
    form.action = "/i18n/setlang/";
    form.style.display = "none";

    const csrfInput = document.createElement("input");
    csrfInput.type = "hidden";
    csrfInput.name = "csrfmiddlewaretoken";
    csrfInput.value = csrfValue;
    form.appendChild(csrfInput);

    const langInput = document.createElement("input");
    langInput.type = "hidden";
    langInput.name = "language";
    langInput.value = langCode;
    form.appendChild(langInput);

    const nextInput = document.createElement("input");
    nextInput.type = "hidden";
    nextInput.name = "next";
    nextInput.value = newPath;
    form.appendChild(nextInput);

    document.body.appendChild(form);

    console.log("Submitting form with:", {
      csrf: csrfValue,
      language: langCode,
      next: newPath,
    });

    form.submit();
  }

  function getCsrfToken() {
    // Try meta tag first
    const csrfMeta = document.querySelector('meta[name="csrf-token"]');
    if (csrfMeta) {
      return csrfMeta.getAttribute("content");
    }

    // Try hidden input
    const csrfTokenInput = document.querySelector(
      'input[name="csrfmiddlewaretoken"]'
    );
    if (csrfTokenInput) {
      return csrfTokenInput.value;
    }

    // Try cookie
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      const [name, value] = cookie.trim().split("=");
      if (name === "csrftoken") {
        return value;
      }
    }

    // Try Django's built-in function if available
    if (window.django && window.django.csrf) {
      return window.django.csrf.getCookie("csrftoken");
    }

    return null;
  }

  function calculateNewPath(langCode) {
    const currentPath = window.location.pathname;
    let newPath = currentPath;

    // Remove existing language prefix
    if (currentPath.startsWith("/ru/")) {
      newPath = currentPath.substring(3);
    } else if (currentPath.startsWith("/en/")) {
      newPath = currentPath.substring(3);
    } else if (currentPath === "/ru" || currentPath === "/en") {
      newPath = "/";
    }

    // Add new language prefix
    if (langCode === "ru") {
      newPath = `/ru${newPath === "/" ? "" : newPath}`;
    } else if (langCode === "en") {
      newPath = `/en${newPath === "/" ? "" : newPath}`;
    } else {
      // Default language (probably English)
      newPath = newPath === "" ? "/" : newPath;
    }

    return newPath;
  }

  function redirectWithLanguage(langCode) {
    const newPath = calculateNewPath(langCode);
    console.log("Redirecting to:", newPath);
    window.location.href = newPath;
  }

  function setActiveLanguageButton() {
    const currentPath = window.location.pathname;
    let currentLang = "en";

    // Determine current language from URL
    if (currentPath.startsWith("/ru/") || currentPath === "/ru") {
      currentLang = "ru";
      globalCurrentCountry = "ru";
    } else if (currentPath.startsWith("/en/") || currentPath === "/en") {
      currentLang = "en";
      globalCurrentCountry = "uk";
    } else {
      // Default to English
      currentLang = "en";
      globalCurrentCountry = "uk";
    }

    console.log("Current language detected:", currentLang);

    // Update flag and selected state in all headers
    headerContainers.forEach((header) => {
      const switcher = header._languageSwitcher;
      if (switcher) {
        switcher.dropdownItems.forEach((item) => {
          if (item.dataset.lang === currentLang) {
            switcher.currentFlag.src = item.dataset.flag;
            item.classList.add("selected");
          } else {
            item.classList.remove("selected");
          }
        });
      }
    });
  }

  // Close dropdown when clicking outside
  document.addEventListener("click", function (e) {
    let clickedInside = false;

    headerContainers.forEach((header) => {
      const switcher = header._languageSwitcher;
      if (switcher) {
        if (
          switcher.flagButton.contains(e.target) ||
          switcher.dropdown.contains(e.target)
        ) {
          clickedInside = true;
        }
      }
    });

    if (!clickedInside) {
      closeAllDropdowns();
    }
  });

  // Close dropdown on Escape key
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closeAllDropdowns();
    }
  });
});
