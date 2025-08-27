/**
 * Demostración del Punto 1.
 * Cambiamos dinámicamente la estrategia de ordenación sin tocar el cliente.
 */
import { BubbleSort, InsertionSort, QuickSort, SortContext } from "./strategy.js";

export function runP1Demo() {
  const data = [5, 2, 9, 1, 5, 6];
  const context = new SortContext(new BubbleSort());
  console.log("P1 - Bubble asc:", context.execute(data, "asc"));
  console.log("P1 - Bubble desc:", context.execute(data, "desc"));
  context.setStrategy(new InsertionSort());
  console.log("P1 - Insertion asc:", context.execute(data, "asc"));
  context.setStrategy(new QuickSort());
  console.log("P1 - Quick desc:", context.execute(data, "desc"));
}


