dict_instance = {l1: [{s1:[{l2: [p2, p22, p222]}, {l3: [p3]}, {}, {}]}, s2, s3], l2: [], l3: []}
    dict_instance = {l1: [(1, abc, redline), s2, s3],
                     l2: [],
                     l3: []}

A = last_train
total_turn = turns_A_wait + turns_A_reach_end

turns_A_reach_end?? (min path for A)
turns_A_wait?? (number of branch,...)

ratio = turns_A_reach_end?? / turns_A_wait??

Conclusion:
Find path for 1st train so that last_train's turn is smallest (minimum of line changes)
total_turn = turns_last_train_wait + turns_that_last_train_move