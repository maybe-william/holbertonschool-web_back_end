export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw TypeError('name must be a String');
    }
    this._name = name;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw TypeError('length must be a Number');
    }
    this._length = length;
  }

  set students(students) {
    if (!Array.isArray(students) || (students.length > 0 && typeof students[0] !== 'string')) {
      throw TypeError('students must be an Array of String');
    }
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }
}
