document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".toggle-list-button");

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            const itemId = this.getAttribute("data-id");
            const itemType = this.getAttribute("data-type");

            // Obtener el token CSRF desde el meta tag
            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute("content");

            fetch("/toggle_list_item/", { // Asegúrate de que la URL sea correcta
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify({ item_id: itemId, item_type: itemType }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === "added") {
                    this.textContent = "Quitar de Mi Lista";
                    this.classList.add("added");
                } else if (data.status === "removed") {
                    this.textContent = "Agregar a Mi Lista";
                    this.classList.remove("added");
                }
            })
            .catch(error => {
                console.error("Error:", error);
                alert("Hubo un problema al procesar tu solicitud. Por favor, intenta de nuevo.");
            });
        });
    });
});
