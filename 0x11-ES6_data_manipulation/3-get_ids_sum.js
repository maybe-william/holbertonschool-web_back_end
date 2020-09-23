export default function getListStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return 0;
  }
  let val = 0;
  val = students.reduce((prev, x) => prev + x.id);
  return val;
}
