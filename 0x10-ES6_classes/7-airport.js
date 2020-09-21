export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
    this.toString = this._toString;
  }

  _toString() {
    return `[object] ${this._code}]`;
  }
}
