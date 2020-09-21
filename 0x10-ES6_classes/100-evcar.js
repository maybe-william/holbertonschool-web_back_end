import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  cloneCar() {
    const obj = Car(this._brand, this._motor, this._color);
    obj._range = this._range;
    return obj;
  }
}
