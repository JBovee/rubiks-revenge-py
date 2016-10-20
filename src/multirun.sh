CXPB="$1"
MUTPB="$2"
for GEN in 30 40 50 60 70 80 90 100
do
    echo "$GEN"
    python main.py $GEN $CXPB $MUTPB > sims/f1/f1_$CXPB.$MUTPB.$GEN
done
