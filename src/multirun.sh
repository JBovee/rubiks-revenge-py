MUTPB=0.01
for GEN in 30 40 50 60; do for CXPB in 0.65 0.7 0.75 0.8;
do
    echo "fitness1, $GEN, $CXPB, $MUTPB"
    python main.py $GEN $CXPB $MUTPB "f1" >> sims/f1/f1_test1
    python main.py $GEN $CXPB $MUTPB "f1" >> sims/f1/f1_test2
done
done
