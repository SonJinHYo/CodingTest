#include<iostream>
#include<time.h>
#include <string>
#include <vector>
#include <algorithm>
#include<sstream>

using namespace std;
string new_answer(int now_clc, int now_min) 
{
    string s = "";  //리턴할 문자열
    if (now_clc >= 10) s += to_string(now_clc); //시간이 두 자리 수라면to_string함수로 입력받은 시간을 문자열에 추가한다.
    else s += "0" + to_string(now_clc);     // 시간이 한 자리 수라면 0을 먼저 추가한 후 to_string함수로 입력받은 시간을 추가한다.

    s += ":"; // 형식을 위해 ":" 추가

    if (now_min >= 10) s += to_string(now_min);     //입력받는 분도 시간과 같이 입력받는다
    else s += "0" + to_string(now_min);

    return s;
}
string solution(int n, int t, int m, vector<string> timetable) {
    string answer = "09:00";    //답을 저장할 변수. 아무런 제약이 없을 시 9시에 버스를 타므로 9시로 초기화

    sort(timetable.begin(), timetable.end());   //timetable을 오름차순으로 정렬해준다

    int hour = 9; // 버스 시간
    int min = 0; // 버스 분
    int inBusPerson = 0; //버스 안 사람 수
    int i = 0;  //버스 운행 횟수 카운트용 변수
    int now_pos = 0;  //timetable의 몇번째 사람인지 저장할 변수

    do  //(i+1)번째 버스 운행 시작
    {
        //timetable의 처음 값부터 탐색 시작
        while (now_pos < timetable.size())
        {
            int now_clc = stoi(timetable[now_pos].substr(0, 2));    //현재 timetable 학생의 시간과
            int now_min = stoi(timetable[now_pos].substr(3, 2));    //현재 timetable 학생의 분단위를 정수로 저장

            if (inBusPerson < m)  //버스에 자리가 있다면,
            {
                if (now_clc < hour || (now_clc == hour && now_min <= min)) //만약 현재 학생의 시간보다 answer이 남는다면 
                {
                    inBusPerson++;     //지금 timetable의 학생이 탄다.
                    if (inBusPerson == m && i + 1 == n)  //만약 버스 자리가 꽉 차면, 내가 못타기 때문에 내가 탈 시간을 수정한다
                    {
                        if (now_min == 0) answer = new_answer(now_clc - 1, 59);     //현재 분단위가 0분이면 시간을 줄이고 59분으로 답을 수정
                        else answer = new_answer(now_clc, now_min - 1);     //분단위가 0이 아니면 분단위를 1만 줄인다.
                        break;
                    }
                    else if (inBusPerson == m && i + 1 < n) //마지막 버스가 아니라면 다음 버스를 기다린다.
                    {
                        inBusPerson = 0;    //다음 버스의 사람은 0명
                        now_pos++;      //timetable의 다음 학생으로 이동
                        break;
                    }
                    else  //학생이 탄다면 timetable의 다음 학생으로 이동
                    {
                        now_pos++;
                    }
                }

                else //현재 학생의 시간보다 answer이 적다면 내가 탄다
                {
                    answer = new_answer(hour, min); //현재 답이 곧 정답
                    inBusPerson = 0;
                    break;
                }
            }

            else if (inBusPerson == m)  //버스 자리가 꽉 찼다면
            {
                inBusPerson = 0;    //다음 버스를 탐. 버스 사람 0명으로 수정
                break;
            }
        }
        if (now_pos == timetable.size()) // 만약 현재 학생이 마지막 학생이라면
            answer = new_answer(hour, min); // 무조건 타야하므로 현재 시간이 답이다.

        i++;    //운행 횟수 +1
        min += t;   //현재 시간에 다음 버스 도착시간 +t
        if (min >= 60)  //만약 60분이 넘어가면 시간까지 수정
        {
            hour++;
            min -= 60;
        }

    } while (i < n);    //n번 운행할 때 까지 반복

    return answer;      //결과 리턴
}