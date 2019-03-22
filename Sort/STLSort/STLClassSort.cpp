#include <iostream>
#include <algorithm>

using namespace std;

class Student{
public:
    string name;
    int score;
    Student(string name, int score)
    {
        this -> name = name;
        this -> score = score;
    }
    //정렬 기준은 '점수가 작은 순서'
    bool operator <(Student &student)
    {
        return this->score < student.score;
    }
};

int main(void)
{
    Student students[] =
    {
        Student("김철수", 90),
        Student("이철민", 93),
        Student("한용훈", 97),
        Student("나한빈", 87),
        Student("이상현", 92)
    };

    sort(students, students);
    for(int i = 0; i < 5; i++)
    {
        cout << students[i].name << ' ';
    }
}
