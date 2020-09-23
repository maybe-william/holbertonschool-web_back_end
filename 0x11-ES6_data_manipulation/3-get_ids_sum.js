export default function getListStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  let val = 0;
  val = students.reduce((prev, x) => prev + x.id);
  return val;
}
