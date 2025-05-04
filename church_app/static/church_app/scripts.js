document.addEventListener("DOMContentLoaded", function () {
    // Apply fade-in effect to elements
    const elements = document.querySelectorAll(".fade-in");
    elements.forEach((el) => {
        el.style.opacity = 0;
        el.style.transition = "opacity 2s";
        setTimeout(() => {
            el.style.opacity = 1;
        }, 500);
    });

    // Auto-hide success message after 3 seconds
    const successMessage = document.querySelector(".alert-success");
    if (successMessage) {
        setTimeout(() => {
            successMessage.style.display = "none";
        }, 3000);
    }
});
