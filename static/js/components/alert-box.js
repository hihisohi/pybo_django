export class AlertBox {
  constructor(target, type) {
    this.target = target;
    this.type = type;
    this.alertBoxId = 'alertbox-' + Math.random().toString(16).substring(2, 10);

    const alertBoxDiv = document.createElement('div');
    alertBoxDiv.classList.add('alertbox');
    alertBoxDiv.id = this.alertBoxId;
    alertBoxDiv.innerText = type + '타입 alert박스';

    this.target.append(alertBoxDiv);

    this._draggable(alertBoxDiv);
  }

  _draggable(element) {
    let initX = 0,
      initY = 0,
      movedX = 0,
      movedY = 0;

    element.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
      e.preventDefault();
      initX = e.clientX;
      initY = e.clientY;
      document.onmouseup = closeDragElement;
      document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
      e.preventDefault();
      movedX = initX - e.clientX;
      movedY = initY - e.clientY;
      initX = e.clientX;
      initY = e.clientY;

      element.style.top = element.offsetTop - movedY + 'px';
      element.style.left = element.offsetLeft - movedX + 'px';
    }

    function closeDragElement() {
      document.onmouseup = null;
      document.onmousemove = null;
    }
  }
}
