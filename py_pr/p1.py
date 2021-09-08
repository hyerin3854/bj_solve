def solution(table, languages, preference):
    arr = []

    for score in table:
        type = score.split(" ")[0]
        score = score.split(" ")[1:]
        score.reverse()
        sum = 0
        for languageIdx in range(len(languages)) :
            if languages[languageIdx] in score :
                idx = score.index(languages[languageIdx])+1
                sum+=(idx*preference[languageIdx])
        arr.append((sum,type))

    arr.sort(key=lambda x: (-x[0], x[1]))
    answer = arr[0][1]

    return answer

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["PYTHON", "C++", "SQL"],[7, 5, 5]))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],["JAVA", "JAVASCRIPT"],[7, 5]))