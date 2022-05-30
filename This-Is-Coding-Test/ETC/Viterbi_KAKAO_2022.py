#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
viterbi test for goorm
"""

###########
# imports #
###########
import sys

#############
# functions #
#############
def eval(output, gold):
    """
    *** 수정하지 마시오
    테스트 평가 함수 (테스트 결과를 체크할수 있는 함수입니다.)
    :param output:      result of tagging(list of str)
    :param gold:        reference of input data(gold data)
    :return accuracy:   accuracy of test
    """
    golds = [_.split() for _ in gold]
    outs = [_.split() for _ in output]
    if len(golds) != len(outs):
        print('numbers of sentences are different %d vs %d' % (len(golds), len(outs)), file=sys.stderr)
        return False
    correct_num = 0
    for line_num, (gold, out) in enumerate(zip(golds, outs), start=1):
        if len(gold) != len(out):
            print('numbers of tokens in %d-th sentence are different %d vs %d' % \
                   (line_num, len(gold), len(out)), file=sys.stderr)
            return False
        correct_num += sum([(1 if g == o else 0) for g, o in zip(gold, out)])
    total_num = sum([len(_) for _ in golds])
    accuracy = 100.0 * correct_num / total_num
    print('Accuracy: %.1f%%' % accuracy)
    return accuracy


########
# main #
########
def main(inp, ref):
    """
    part-of-speech tagging (reference code)
    """

    results = [] # 결과값을 입력합니다.
    """
    비터비 코드 개발
    """
    datas = []
    with open(inp, 'rt') as rh:
        for text in rh.readlines():
            datas.append(text.strip())

    # 전체 데이터 받기
    all_nodes = ([data.split("\t") for data in datas])
    
    # 클래스 만들기
    HMM = Viterbi(all_nodes)
    print("프로그램 시작")
    for text in HMM.graph():
        results.append(" ".join(text))
    print(results)

    """
    *** 수정하지 마시오
    결과 비교 코드 (수정하지 마시오)
    ref 파일을 refs에 저장하고. 이를 results에 값과 비교하여 정확도를 계산합니다.
    """
    refs = []
    with open(ref, 'rt') as rh:
        for text in rh.readlines():
            refs.append(text.strip())

    if len(results) == len(refs):
        eval(results, refs)
    return True

##########
# clsass #
##########
class Viterbi(object):
    def __init__(self, all_nodes ):
        # 선 데이터
        line_nodes = []
        line_num = 0
        # 값 데이터
        value_nodes = []
        value_num = 0
        # 마무리 데이터
        observations = []
        end_num = 0

        for nodes in all_nodes:
            if len(nodes) == 1:
                if line_num == 0:
                    line_num = int(nodes[0])
                elif value_num == 0:
                    value_num = int(nodes[0])
                elif end_num == 0:
                    end_num = int(nodes[0])

        #print(line_num, value_num, end_num)
        # 데이터 구축 완료
        line_nodes = all_nodes[1:line_num+1]
        value_nodes  = all_nodes[line_num+2:line_num+2+value_num]
        observations = all_nodes[-end_num:]
        observations = [nodes[0].split() for nodes in observations]
        # 먼저 맵을 만든다.
        line_nodes2 = [l[:2] for l in line_nodes]
        # 처음 맵
        states = list(set(sum(line_nodes2, [])))
        del(states[states.index('<s>')])
        del(states[states.index('</s>')])
        self.states = states
        #print(states)
        
        # 단어 발생 확률 체크
        emission_probability = {}
        for value_node in value_nodes:
            #print(value_node[0])
            try: 
                emission_probability[value_node[0]]
            except:
                emission_probability[value_node[0]] = {value_node[1] : float(value_node[2])}
            else:
                emission_probability[value_node[0]][value_node[1]] = float(value_node[2])
        #print("bo1", emission_probability)
        self.emission_probability = emission_probability
        
        transition_probability = {}
        for line_node in line_nodes:
            try: 
                transition_probability[line_node[0]]
            except:
                transition_probability[line_node[0]] = {line_node[1] : float(line_node[2])}
            else:
                transition_probability[line_node[0]][line_node[1]] = float(line_node[2])

        #print("bo2", transition_probability)
        self.transition_probability = transition_probability
        
        # 변수들
        self.states = tuple(self.states)

        self.end_num = end_num
        self.line_num = line_num
        self.value_num = value_num

        self.observations = observations 
        self.line_nodes = line_nodes
        self.value_nodes = value_nodes
    
    
    def graph(self):
        results = []
        # print('======states======\n', self.states) # states
        # print("======self.emission_probability======\n",self.emission_probability) # emissions
        # print("self.transition_probability : ", self.transition_probability) # transition_probability
        # print(self.observations) # observations: [['x', 'target_s', 'target_s']]

        start_probability = {}
        for nodes in self.transition_probability['<s>']:
            start_probability[nodes] = self.transition_probability['<s>'][nodes]
        del(self.transition_probability["<s>"])

        # 값 전부 가져오기
        for observation in self.observations: 
            V = [{}]
            path = {}
            # print(observation) # x target_s target_s
            i = 0
            # 첫번째꺼
            #print("헤", self.transition_probability['<s>'])
            
            # start_probability 찾기 함
            for nodes in start_probability:
                # print('nodes', nodes)
                V[0][nodes] = start_probability[nodes]
                path[nodes] = nodes
            # print(V) 
            # print(path)
            # 나머지꺼

            # print('===============다음 step!!!===============')

            for t, node in enumerate(observation):
                t = t+1 # 1 ~ 3
                if len(observation) <= t:
                    break
                # print("go : ", node)
                V.append({})
                temp_path = {}
                
                # 확률을 구하고자 하는 state
                for target_s in self.states: # A, B
                    temp = []
                    # 이전 경로 state
                    for from_s in self.states:
                        if from_s not in V[t-1]: # 시작확률 존재하는지
                            V[t-1]['from_s'] = 1e-06
                        if from_s not in self.transition_probability:
                            continue
                        if target_s not in self.transition_probability[from_s]: # 전이확률이 존재하지 않으면 최소값으로 넣어줌 
                            self.transition_probability[from_s][target_s] = 1e-06
                        if from_s not in self.emission_probability or observation[t-1] not in self.emission_probability[from_s]: # 방출확률 존재하는지
                            continue
                        probability = V[t-1][from_s] * self.transition_probability[from_s][target_s] * self.emission_probability[from_s][observation[t-1]]
                        # print('probability', probability)
                        temp.append((probability, from_s))

                    # 값이 없을 때는 디폴트값을 태깅하고, 낮은 확률값을 입력해줌
                    if not temp:
                        # temp.append((1, 'NN'))
                        temp.append((1e-06, 'NN'))
                        # continue
                    # print(temp)
                    if len(temp) == 1:
                        (probability, from_s) = temp[0]
                    else:
                        (probability, from_s) = max(temp)

                    # print("p, w:", (probability, from_s))
                    # print("path", [(path[from_s])] + [target_s]) # path['B'] + ['A']
                    # print("temp_path", temp_path)
                    V[t][target_s] = probability
                    # V[t][target_s] = 1
                    try:
                        temp_path[target_s] = (path[from_s]) + [target_s]
                    except:
                        temp_path[target_s] = [(path[from_s])] + [target_s]
                path = temp_path
            t = t-1

            # (V[2]['A'], 'A'), (V[2]['B'], 'B')
            temp = []
            for target_s in self.states:
                if target_s not in V[t]:
                    continue
                temp.append((V[t][target_s], target_s))
            
            # 빈 리스트 건너뛰기
            if not temp:
                continue
            # print('temp', temp)
                    
            if len(temp) == 1:
                (probability, from_s) = temp[0]
            else:
                (probability, from_s) = max(temp)

            # 마지막 테그는 보통 .으로 끝남
            path[from_s][-1] ="."

            # print(path)
            results.append(path[from_s])
        return results

#######
# RUN #
#######
if __name__ == '__main__':
    # input_file : 입력 텍스트 파일
    # ref_file : 레퍼런스 텍스트 파일, 결과값과 비교하여 정확도를 계산하는데 이용합니다.
    input_file = "data/sample.in"
    ref_file = "data/sample.ref"

    main(input_file, ref_file)