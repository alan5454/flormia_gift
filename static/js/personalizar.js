// Suma el precio de los extras marcados.
(function () {
  const total = document.getElementById("total-extras");
  const casillas = document.querySelectorAll(".extra input");
  if (!total) return;
  const formato = new Intl.NumberFormat("es-MX", { maximumFractionDigits: 2 });
  function actualizar() {
    let suma = 0;
    casillas.forEach((c) => { if (c.checked) suma += parseFloat(c.dataset.precio) || 0; });
    total.textContent = "$" + formato.format(suma);
  }
  casillas.forEach((c) => c.addEventListener("change", actualizar));
})();
