export default function updateStudentGradeByCity(students, loc, newGrades) {
  if (!Array.isArray(students)) {
    return [];
  }
  if (!Array.isArray(newGrades)) {
    return [];
  }
  let arr = [];
  arr = students.filter((x) => x.location === loc).map((x) => {
    let newGrade = newGrades.filter((y) => y.studentId === x.id);
    if (newGrade.length === 0) {
      newGrade = 'N/A';
    } else {
      newGrade = newGrade[0].grade;
    }
    const z = Object.assign(x);
    z.grade = newGrade;
    return z;
  });

  return arr;
}
