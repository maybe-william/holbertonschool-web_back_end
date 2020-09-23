export default function getListStudentIds(students) {
  const arr = [];
  students.forEach((x) => arr.push(x.id));
  return arr;
}
