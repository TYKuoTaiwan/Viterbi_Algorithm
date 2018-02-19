import sys

_STATE=['R', 'S']
_PI={'R':.7, 'S':.3}
_A={ 'R':{'R':.6, 'S':.4 }, 'S':{'R':.3,'S':.7} }
_B={'R':{'W':.2,'S':.4,'C':.4}, 'S':{'W':.5,'S':.4,'C':.1} }

def rec(obs, val_pre, qseq_pre):
    if len(obs) > 0:
        val={}
        qseq={}

        for q in _STATE:
            if len(val_pre) == 0:
                val.update({ q:_PI[q] * _B[q][obs[0]]})
                qseq.update({q:[]})
            else:
            	temp=[]
            	for q_pre in _STATE:
            	    temp.append((qseq_pre[q_pre]+[q_pre], val_pre[q_pre] * _A[q_pre][q] * _B[q][obs[0]]))

            	max_prob = temp[0]
            	for v in temp[1:]:
                    if v[1]>max_prob[1]:
                        max_prob = v
            	qseq.update({ q:max_prob[0] })
            	val.update({q:max_prob[1]})            
        return rec(obs[1:],val,qseq)
    else:
        temp = []
        for q in _STATE:
        	temp.append(( qseq_pre[q]+[q] , val_pre[q] ))

        max_prob = temp[0]
        for v in temp[1:]:
        	if v[1]>max_prob[1]:
        		max_prob = v
        print(''.join(max_prob[0]))

def main(args):
	rec(args[1], {},[])

if __name__ == '__main__':
	main(sys.argv)