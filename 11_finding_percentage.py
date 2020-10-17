if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    the_query_marks = student_marks[query_name]

    theSum = 0

    for mark in the_query_marks:
        theSum = theSum + mark

    avg = theSum / len(the_query_marks)

    print('%.2f' % (avg))
