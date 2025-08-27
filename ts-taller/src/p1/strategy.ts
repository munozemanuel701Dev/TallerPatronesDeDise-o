/**
 * Punto 1: Ordenación con patrón Strategy.
 *
 * Este módulo define:
 * - La interfaz `SortStrategy` que encapsula un algoritmo de ordenación.
 * - Tres estrategias concretas: `BubbleSort`, `InsertionSort`, `QuickSort`.
 * - El contexto `SortContext` que permite cambiar la estrategia en tiempo de ejecución.
 *
 * El parámetro `order` permite ejecutar cada estrategia en sentido ascendente o descendente
 * sin duplicar código. Las estrategias no mutan el arreglo recibido; trabajan sobre copias.
 */
export type SortOrder = "asc" | "desc";

export interface SortStrategy {
  /** Ordena y devuelve una nueva lista sin modificar el argumento original. */
  sort(values: number[], order: SortOrder): number[];
}

export class BubbleSort implements SortStrategy {
  /** Implementación didáctica de Bubble Sort O(n^2). */
  sort(values: number[], order: SortOrder): number[] {
    const arr = [...values];
    const compare = (a: number, b: number) => (order === "asc" ? a > b : a < b);
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr.length - i - 1; j++) {
        if (compare(arr[j], arr[j + 1])) {
          [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        }
      }
    }
    return arr;
  }
}

export class InsertionSort implements SortStrategy {
  /** Insertion Sort O(n^2) pero eficiente para listas casi ordenadas. */
  sort(values: number[], order: SortOrder): number[] {
    const arr = [...values];
    const before = (a: number, b: number) => (order === "asc" ? a < b : a > b);
    for (let i = 1; i < arr.length; i++) {
      const key = arr[i];
      let j = i - 1;
      while (j >= 0 && before(key, arr[j])) {
        arr[j + 1] = arr[j];
        j--;
      }
      arr[j + 1] = key;
    }
    return arr;
  }
}

export class QuickSort implements SortStrategy {
  /** Quick Sort promedio O(n log n), establecemos comparador según el orden. */
  sort(values: number[], order: SortOrder): number[] {
    const arr = [...values];
    const cmp = (a: number, b: number) => (order === "asc" ? a - b : b - a);
    const qs = (a: number[], l: number, r: number) => {
      if (l >= r) return;
      const pivot = a[Math.floor((l + r) / 2)];
      let i = l;
      let j = r;
      while (i <= j) {
        while (cmp(a[i], pivot) < 0) i++;
        while (cmp(a[j], pivot) > 0) j--;
        if (i <= j) {
          [a[i], a[j]] = [a[j], a[i]];
          i++;
          j--;
        }
      }
      if (l < j) qs(a, l, j);
      if (i < r) qs(a, i, r);
    };
    qs(arr, 0, arr.length - 1);
    return arr;
  }
}

export class SortContext {
  /**
   * El contexto conoce una `SortStrategy` y delega en ella el algoritmo.
   * Se puede reemplazar durante la ejecución para cambiar el comportamiento.
   */
  constructor(private strategy: SortStrategy) {}
  setStrategy(strategy: SortStrategy) {
    this.strategy = strategy;
  }
  execute(values: number[], order: SortOrder): number[] {
    return this.strategy.sort(values, order);
  }
}


