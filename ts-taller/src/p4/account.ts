/**
 * Punto 4: Reglas nuevas sobre un módulo de caja existente usando Decorator.
 *
 * Mantiene el contrato `Account` sin modificar la implementación base
 * `SavingsAccount`. Las nuevas restricciones se apilan como decoradores:
 * - `WeeklyWithdrawLimit`: máximo N retiros por semana.
 * - `LargeWithdrawAuthorization`: autorización para retiros mayores a umbral.
 * - `AMLDepositNotifier`: notificación AML para depósitos grandes.
 */
export interface Account {
  deposit(amount: number): void;
  withdraw(amount: number): void;
  balance(): number;
}

export class SavingsAccount implements Account {
  private current = 0;
  deposit(amount: number): void { this.current += amount; }
  withdraw(amount: number): void { if (this.current < amount) throw new Error("Fondos insuficientes"); this.current -= amount; }
  balance(): number { return this.current; }
}

export abstract class AccountDecorator implements Account {
  constructor(protected readonly account: Account) {}
  deposit(amount: number): void { this.account.deposit(amount); }
  withdraw(amount: number): void { this.account.withdraw(amount); }
  balance(): number { return this.account.balance(); }
}

export class WeeklyWithdrawLimit extends AccountDecorator {
  private withdrawals: number[] = [];
  constructor(acc: Account, private limitPerWeek: number) { super(acc); }
  withdraw(amount: number): void {
    const now = Date.now();
    const weekMs = 7 * 24 * 60 * 60 * 1000;
    this.withdrawals = this.withdrawals.filter(t => now - t < weekMs);
    if (this.withdrawals.length >= this.limitPerWeek) throw new Error("Límite de retiros semanales excedido");
    super.withdraw(amount);
    this.withdrawals.push(now);
  }
}

export class LargeWithdrawAuthorization extends AccountDecorator {
  constructor(acc: Account, private threshold: number, private authorize: (amount: number) => boolean) { super(acc); }
  withdraw(amount: number): void {
    if (amount > this.threshold && !this.authorize(amount)) throw new Error("Retiro requiere autorización");
    super.withdraw(amount);
  }
}

export class AMLDepositNotifier extends AccountDecorator {
  constructor(acc: Account, private threshold: number, private notify: (amount: number) => void) { super(acc); }
  deposit(amount: number): void {
    if (amount > this.threshold) this.notify(amount);
    super.deposit(amount);
  }
}


