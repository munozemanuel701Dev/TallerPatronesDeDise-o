/**
 * Punto 2: Cotización de precio en cuotas.
 *
 * Usamos Strategy para encapsular la fórmula por marca de tarjeta
 * y una Factory (`FormulaFactory`) para crear la estrategia según
 * la marca recibida.
 *
 * La función `quoteInstallments` actúa como caso de uso y devuelve
 * el total financiado y el valor de la cuota sin modificar el precio
 * de contado original.
 */
export interface CreditCardFormula {
  name: string;
  calculate(totalCash: number, installments: number, bank: string, date: Date): number;
}

export class VisaFormula implements CreditCardFormula {
  name = "VISA";
  calculate(totalCash: number, installments: number, bank: string, date: Date): number {
    const weekdayFactor = [1.0, 1.01, 1.01, 1.02, 1.02, 1.03, 1.02][date.getDay()];
    const base = totalCash * (1 + 0.015 * installments) * weekdayFactor;
    return base;
  }
}

export class MasterFormula implements CreditCardFormula {
  name = "MASTERCARD";
  calculate(totalCash: number, installments: number, bank: string, date: Date): number {
    const bankAdj = bank.toLowerCase().includes("premium") ? 0.98 : 1.0;
    const base = totalCash * (1 + 0.0175 * installments);
    return base * bankAdj;
  }
}

export class FormulaFactory {
  /** Crea la estrategia según la marca. */
  static create(brand: string): CreditCardFormula {
    switch (brand.toUpperCase()) {
      case "VISA":
        return new VisaFormula();
      case "MASTERCARD":
        return new MasterFormula();
      default:
        throw new Error(`Marca no soportada: ${brand}`);
    }
  }
}

export function quoteInstallments(
  cashPrice: number,
  installments: number,
  brand: string,
  bank: string,
  date = new Date()
) {
  const formula = FormulaFactory.create(brand);
  const financedTotal = formula.calculate(cashPrice, installments, bank, date);
  const installmentAmount = financedTotal / Math.max(1, installments);
  return { cashPrice, financedTotal, installmentAmount };
}


