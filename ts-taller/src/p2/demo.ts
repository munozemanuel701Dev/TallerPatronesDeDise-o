/**
 * Demostración del Punto 2.
 * Prueba dos marcas con distintos parámetros para ver los cambios
 * en el total financiado y el valor de la cuota.
 */
import { quoteInstallments } from "./model.js";

export function runP2Demo() {
  const r1 = quoteInstallments(1000, 6, "VISA", "BancoX", new Date("2025-08-27"));
  console.log("P2 - VISA 6 cuotas:", r1);
  const r2 = quoteInstallments(1000, 12, "MASTERCARD", "Banco Premium", new Date("2025-08-28"));
  console.log("P2 - MASTERCARD 12 cuotas:", r2);
}


