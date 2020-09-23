export default function getListStudentsByLocation(students, loc) {
  if (!Array.isArray(students)) {
    return [];
  }
  let arr = [];
  arr = students.filter((x) => x.location === loc);
  return arr;
}
