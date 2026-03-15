const form = document.querySelector("#lead-form");
const statusEl = document.querySelector("#form-status");

if (form && statusEl) {
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const payload = {
      name: String(formData.get("name") || "").trim(),
      email: String(formData.get("email") || "").trim(),
    };

    statusEl.textContent = "Sending...";
    statusEl.className = "form-status";

    try {
      const response = await fetch("/api/leads", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const result = await response.json();

      if (!response.ok) {
        throw new Error(result.error || "Something went wrong.");
      }

      form.reset();
      statusEl.textContent = "Thanks. We got it and will reach out soon.";
      statusEl.className = "form-status is-success";
    } catch (error) {
      statusEl.textContent =
        error instanceof Error
          ? error.message
          : "Something went wrong. Please try again.";
      statusEl.className = "form-status is-error";
    }
  });
}
