# import sys                                                                  // input 입력보다 훨씬 빠름 문자열로 읽음
# sys.setrecursionlimit(10**6)                                            // 재귀식 깊이 늘림
# from string import ascii_uppercase                                  // list(ascii_uppercase) 대문자리스트 만듬 (low 는 소문자)
# from collections import Counter                                     // 빈도 구하기 Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
# 					          // ** Counter 은 list 끼리 빼기가 가능하다!!!!(중복제거!!!효율좋음)
# from itertools import permutations                                 //  list 의 모든 가능 배열 만듬
# from itertools import combinations                                 //  list 의 모든 가능 배열 만듬  list(combination( list자료 , 배열크기)
# from itertools import product                                        //   복수 list 사용가능   (product( list1 , repeat= (반복횟수)))
# import math                                                               //  ceil  floor round sqrt 사용가능 math.ceil( )
# from collections import deque                                      // deque([]) 데크식활용
# list 뒤집기                                                                 //  list.reverse()
# 람다식활용                                                                //  tuple_list.sort(key=lambda x : (x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능
#  ''.join(리스트)                                                            // 리스트 합침   ''.join(['a', 'b', 'c'])   ->  "abc"
#  '구분자'.join(리스트)                                                   //                   '_'.join(['a', 'b', 'c'])   ->  "a_b_c"
# =sorted(정렬할 데이터)                                                //
# sorted(정렬할 데이터, reverse 파라미터)                          //
# sorted(정렬할 데이터, key 파라미터)                               //
# sorted(정렬할 데이터, key 파라미터, reverse 파라미터)      //
# print("%양식문자" %(값)) 형식으로  함수안에 일정한 양식을 제공  // '%02d:%02d:%02d' % (maxIdx/3600, maxIdx/60%60, maxIdx%60)  카카오코테 2021-5 답안참조.
#                                                                                         // %s 문자열 , %d10진수 정수, %c 단일문자열, %f 실수 , %o 8진수 정수, %x 16진수정수
# **list 활용**
# list[0_for in range(5)] = [0, 0, 0, 0, 0] list=[0]*5= [0,0,0,0,0]
# list = [1,2,3,4,5,6,7,8,9,10]
# list[:5]  [1,2,3,4,5]     앞의 다섯개자료를 가짐
# list[-5:] [6,7,8,9,10]   뒤의 다섯개자료를가짐
# list[::2]  [1,3,5,7,9,]    [0]부터 두칸 간격으로 출력
# list[1::2] [2,4,6,8,10]   [1]을 넘기고 두칸 간격으로 출력
# list[::-1]                  리스트 뒤에서부터 출력
# import re                                                                 // 정규표현식 함수  st = re.sub('[^a-z0-9\-_.]', '', st)  //  re.sub('^[.]|[.]$', '', st)
# alt+ctrl+shift 클릭 = 여러 곳 한번에 수정
#
#
# enumerate                                                               //반복문의 인덱스 및 원소 값을 튜플형태로 반환
# t = [1, 5, 7, 33, 39, 52]   for p in enumerate(t):
#  print(p)        (0, 1) (1, 5) (2, 7) (3, 33)(4, 39) (5, 52)
# import heapq 					//  heapq[0] 자리엔 heapq 의 최소값이 들어간다. 그렇다고 전체가 정렬되어있진 않음.
# heapq.heapify(list명) -> 기존의리스트를 heap화 함	//  heapq.heapop(list명) 가장작은 원소 추출 , heapq.heappush(list명 , 값)
#
# zip                             				//  list 묶기
# from collections import defaultdict			//
#
#
# starmap 						// map 은 iterable 의 각 item 을 다루고 starmap은 iterable 의 각 iterable을 다룸