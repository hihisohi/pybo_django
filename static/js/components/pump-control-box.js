export class PumpControlBox {
  constructor(target, pumpId, runtime) {
    this.target = target;
    this.pumpId = pumpId;
    this.controlboxId = 'controlbox-' + Math.random().toString(16).substring(2, 10);

    const cntrlBoxDiv = document.createElement('div');
    cntrlBoxDiv.classList.add('pump-controlbox', `box${pumpId}`);
    cntrlBoxDiv.id = this.controlboxId;
    cntrlBoxDiv.innerText = '펌프' + pumpId + '번 ' + runtime;

    this.target.append(cntrlBoxDiv);
  }
}
