MUTPB=0.01
CXPB=0.8
OUTPATH=simsV3
mkdir -p -- "$OUTPATH"
OUTFILE=moves_div_20_under_20_moves
echo "$OUTFILE"
for GEN in 40 50 60;
do
    echo "fitness2, $GEN, $CXPB, $MUTPB"
    echo "fitness2, $GEN, $CXPB, $MUTPB" >> $OUTPATH/$OUTFILE
    echo "First"
    echo "First" >> $OUTPATH/$OUTFILE
    python main.py $GEN $CXPB $MUTPB "f2" >> $OUTPATH/$OUTFILE
    echo "Second"
    echo "Second" >> $OUTPATH/$OUTFILE
    python main.py $GEN $CXPB $MUTPB "f2" >> $OUTPATH/$OUTFILE
    echo "Third"
    echo "Third" >> $OUTPATH/$OUTFILE
    python main.py $GEN $CXPB $MUTPB "f2" >> $OUTPATH/$OUTFILE
    echo "Fourth"
    echo "Fourth" >> $OUTPATH/$OUTFILE
    python main.py $GEN $CXPB $MUTPB "f2" >> $OUTPATH/$OUTFILE
    echo ""
done
