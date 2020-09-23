export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  let val = 0;
  val = students.map((x) => x.id).reduce((prev, x) => prev + x);
  return val;
}
