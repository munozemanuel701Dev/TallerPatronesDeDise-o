/**
 * Demostración del Punto 3.
 * Con la misma estructura de inventario probamos dos algoritmos.
 */
import { BalanceWarehouses, InventoryContext, SimpleReorder } from "./inventory.js";

export function runP3Demo() {
  const structure = {
    products: 1200,
    warehouses: 4,
    shelves: 200,
    distributionCenters: 2,
    factories: 1,
  };
  const ctx = new InventoryContext(new SimpleReorder());
  console.log("P3 - Simple:", ctx.run(structure));
  ctx.setAlgorithm(new BalanceWarehouses());
  console.log("P3 - Balance:", ctx.run(structure));
}


