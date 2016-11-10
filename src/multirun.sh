MUTPB=0.01
CXPB=0.8
FUNC="f7"
OUTPATH=simsV3.2
mkdir -p -- "$OUTPATH"
OUTFILE=3_part_fitness_faces_centers_moves
echo "$OUTFILE"
for GEN in 40 50 60;
do
    echo "$FUNC, $GEN, $CXPB, $MUTPB"
    echo "*********************" >> $OUTPATH/$OUTFILE
    echo "fitness2, $GEN, $CXPB, $MUTPB" >> $OUTPATH/$OUTFILE
    echo "First"
    echo "First" >> $OUTPATH/$OUTFILE
    python main.py $GEN $CXPB $MUTPB $FUNC >> $OUTPATH/$OUTFILE
    echo "Second"
    echo "Second" >> $OUTPATH/$OUTFILE
    python main.py $GEN $CXPB $MUTPB $FUNC >> $OUTPATH/$OUTFILE
    echo "Third"
    echo "Third" >> $OUTPATH/$OUTFILE
    python main.py $GEN $CXPB $MUTPB $FUNC >> $OUTPATH/$OUTFILE
    echo "Fourth"
    echo "Fourth" >> $OUTPATH/$OUTFILE
    python main.py $GEN $CXPB $MUTPB $FUNC >> $OUTPATH/$OUTFILE
    echo "Fifth"
    echo "Fifth" >> $OUTPATH/$OUTFILE
    python main.py $GEN $CXPB $MUTPB $FUNC >> $OUTPATH/$OUTFILE
    echo "Sixth"
    echo "Sixth" >> $OUTPATH/$OUTFILE
    python main.py $GEN $CXPB $MUTPB $FUNC >> $OUTPATH/$OUTFILE
    echo "*********************" >> $OUTPATH/$OUTFILE
    echo ""
done
