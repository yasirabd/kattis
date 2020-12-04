n = int(input())
ans = input()

adrian_pattern = 'ABC'
bruno_pattern = 'BABC'
goran_pattern = 'CCAABB'

score_adrian = 0
score_bruno = 0
score_goran = 0
for i in range(len(ans)):
    if ans[i] == adrian_pattern[i%3]: score_adrian += 1
    if ans[i] == bruno_pattern[i%4]: score_bruno += 1
    if ans[i] == goran_pattern[i%6]: score_goran += 1

best_score = max(score_adrian, score_bruno, score_goran)
print(best_score)
if score_adrian == best_score: print('Adrian')
if score_bruno == best_score: print('Bruno')
if score_goran == best_score: print('Goran')