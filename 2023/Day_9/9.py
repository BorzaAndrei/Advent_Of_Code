# 0 3 6 9 12 15

with open("2023/Day_9/input.txt") as r:
    s = 0
    for line in r.readlines():
        seq = list(map(int, line.strip('\n').split()))
        
        seqs = [seq]

        stop_cond = False
        current_seq_ind = 0
        while not stop_cond:
            seq = []
            for ind in range(len(seqs[current_seq_ind]) - 1):
                seq.append(seqs[current_seq_ind][ind + 1] - seqs[current_seq_ind][ind])
            if all(x == 0 for x in seq):
                stop_cond = True
            else:
                current_seq_ind += 1
            seqs.append(seq)
        # seqs[-1].append(0)
        seqs[-1].insert(0, 0)

        for ind in range(len(seqs) - 2, -1, -1):
            # seqs[ind].append(seqs[ind + 1][-1] + seqs[ind][-1])
            seqs[ind].insert(0, seqs[ind][0] - seqs[ind + 1][0])
        
        s += seqs[0][0]
    print(s)
