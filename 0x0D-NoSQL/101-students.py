#!/usr/bin/env python3
"""List all documents in a mongodb collection"""


def top_students(mongo_collection):
    """Return all students sorted by average score"""
    students = [x for x in mongo_collection.find()]
    for student in students:
        scores = [x.get('score', 0) for x in student.get('topics', [])]
        avg = 0
        for score in scores:
            avg = avg + score
        avg = avg / len(scores)
        student["averageScore"] = avg
    return sorted(students, key=lambda z: z["averageScore"])
